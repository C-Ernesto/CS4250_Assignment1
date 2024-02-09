# -------------------------------------------------------------------------
# AUTHOR: Christopher Ernesto
# FILENAME: indexing
# SPECIFICATION: A program that calculates tf-idf from collections.csv
# FOR: CS 4250- Assignment #1
# TIME SPENT: 1 hour
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

# Importing some Python libraries
import csv
import math

documents = []

# Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])

#print(documents)

# Conducting stopword removal. Hint: use a set to define your stopwords.
# --> add your Python code here
stopWords = {"I", "and", "She", "her", "They", "their"}

stoppedDocument = []
for doc in documents:
    wordsArr = doc.split(" ")
    result = [word for word in wordsArr if word not in stopWords]
    stoppedDocument.append(' '.join(result))

#print(stoppedDocument)

# Conducting stemming. Hint: use a dictionary to map word variations to their stem.
# --> add your Python code here
steeming = {"loves": "love",
            "cats": "cat",
            "dogs": "dog"}

stemmedDocument = []
for doc in stoppedDocument:
    wordsArr = doc.split(" ")
    result = [steeming[word] if word in steeming else word for word in wordsArr]
    stemmedDocument.append(' '.join(result))

#print(stemmedDocument)

# Identifying the index terms.
# --> add your Python code here
terms = []

for doc in stemmedDocument:
    wordsArr = doc.split(" ")
    for word in wordsArr:
        if word not in terms:
            terms.append(word)

#print(terms)


# Building the document-term matrix by using the tf-idf weights.

def calculate_tf(term, document):
    words = document.split(" ")
    return document.count(term) / len(words)


def calculate_idf(term, corpus):
    df = 0
    for document in corpus:
        if term in document:
            df += 1
    return math.log10(len(corpus) / df)


def calculate_tfidf(term, document, corpus):
    tf = calculate_tf(term, document)
    idf = calculate_idf(term, corpus)
    return tf * idf


docTermMatrix = []
for doc in stemmedDocument:
    row = [calculate_tfidf(term, doc, stemmedDocument) for term in terms]
    docTermMatrix.append(row)

#print(docTermMatrix)

# Printing the document-term matrix.
# print term header
print('         ' + ''.join('{:>10}'.format(i) for i in terms))
count = 0
for row in docTermMatrix:
    print("document " + str(count), end='')
    print(''.join('{:>10.3f}'.format(i) for i in row))
    count += 1
