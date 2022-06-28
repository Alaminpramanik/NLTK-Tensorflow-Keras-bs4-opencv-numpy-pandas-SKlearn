import nltk
# nltk.download('omw-1.4')
# nltk.download('wordnet')
from nltk.corpus import wordnet

synonyms = []
antonyms = []
input='As such, we can populate some lists like'
data =set(input.split(' '))
print('data',data)
for datas in data:
    for syn in wordnet.synsets(datas):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

print('syn',set(synonyms))
print('atn',set(antonyms))

# arr_syn=[]
# arr_ant=[]

# syn = wordnet.synsets("computer")
# print(syn[0].name)
# print(syn[0].lemmas()[0].name())
# print(syn[0].definition())
# print(syn[0].examples())
