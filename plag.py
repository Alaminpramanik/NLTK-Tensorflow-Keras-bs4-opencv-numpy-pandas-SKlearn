import re
import nltk
nltk.download('punkt')
from nltk.util import ngrams, pad_sequence, everygrams
from nltk.tokenize import word_tokenize
from nltk.lm import MLE, WittenBellInterpolated
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter

# Training data file
train_data_file = "That is where email-validator comes in. Whether you are creating a registration form for your website or you just need to delete all invalid email addresses from your mailing list, you can't help but perform the process of email validation. You need to validate if an email address is real by checking"

# read training data
# with open(train_data_file) as f:
#     train_text = f.read().lower()

# apply preprocessing (remove text inside square and curly brackets and rem punc)
train_text = re.sub(r"\[.*\]|\{.*\}", "", train_data_file)
train_text = re.sub(r'[^\w\s]', "", train_data_file)

# set ngram number
n = 4

# pad the text and tokenize
training_data = list(pad_sequence(word_tokenize(train_data_file), n, 
                                  pad_left=True, 
                                  left_pad_symbol="<s>"))

# generate ngrams
ngrams = list(everygrams(training_data, max_len=n))
print("Number of ngrams:", len(ngrams))

# build ngram language models
model = WittenBellInterpolated(n)
model.fit([ngrams], vocabulary_text=training_data)
print('vocab',model.vocab)

# testing data file
test_data_file = "The plagiarized example, in which the text is taken from Wikipedia with sporadic replacement of words here and there. The lighter colored pixels correspond to the modified words. This method makes it easier to tell which parts of a text were plagiarized. Image by Author."

# Read testing data
# with open(test_data_file) as f:
#     test_text = f.read().lower()
test_text = re.sub(r'[^\w\s]', "", train_data_file)

# Tokenize and pad the text
testing_data = list(pad_sequence(word_tokenize(train_data_file), n, 
                                 pad_left=True,
                                 left_pad_symbol="<s>"))
print("Length of test data:", len(testing_data))

# assign scores
scores = []
for i, item in enumerate(testing_data[n-1:]):
    s = model.score(item, testing_data[i:i+n-1])
    scores.append(s)

scores_np = np.array(scores)

# set width and height
width = 8
height = np.ceil(len(testing_data)/width).astype("int32")
print("Width, Height:", width, ",", height)

# copy scores to rectangular blank array
a = np.zeros(width*height)
a[:len(scores_np)] = scores_np
diff = len(a) - len(scores_np)

# apply gaussian smoothing for aesthetics
a = gaussian_filter(a, sigma=1.0)

# reshape to fit rectangle
a = a.reshape(-1, width)

# format labels
labels = [" ".join(testing_data[i:i+width]) for i in range(n-1, len(testing_data), width)]
labels_individual = [x.split() for x in labels]
labels_individual[-1] += [""]*diff
labels = [f"{x:60.60}" for x in labels]

# create heatmap
fig = go.Figure(data=go.Heatmap(
                z=a, x0=0, dx=1,
                y=labels, zmin=0, zmax=1,
                customdata=labels_individual,
                hovertemplate='%{customdata} <br><b>Score:%{z:.3f}<extra></extra>',
                colorscale="burg"))
fig.update_layout({"height":height*28, "width":1000, "font":{"family":"Courier New"}})
fig['layout']['yaxis']['autorange'] = "reversed"
fig.show()