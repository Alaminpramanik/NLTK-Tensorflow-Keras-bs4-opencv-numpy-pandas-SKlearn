import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

file='The plagiarized example, in which the text is taken from Wikipedia with sporadic replacement of words here and there. The lighter colored pixels correspond to the modified words. This method makes it easier to tell which parts of a text were plagiarized. Image by Author.'
student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes =[open(File).read() for File in  student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(filegpt).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))

def check_plagiarism():
    plagiarism_results = set()
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors =s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1],sim_score)
            plagiarism_results.add(score)
    return plagiarism_results

for data in check_plagiarism():
    print(data)