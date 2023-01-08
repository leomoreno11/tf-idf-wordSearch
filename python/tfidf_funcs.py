# -*- coding: utf-8 -*-
import math
from textblob import TextBlob as tb

# A blob is a document, a blob of text. The blobs contains words.

# Return the number of documents containing a word
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

# Computes term frequency (number of times a word appears in the document blob, normalizing by the total of words in the blob)
# By normalizin the result (dividing the result by quantity of words in the blob), we maintain the values between 0 and 1, thus generating a easier scale for weighting words
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

# Computes Inverse Document Frequency, which measures how common a word is among all documents in bloblist. The more common a word is, the lower its IDF. This is used to prevent words such as "the" to appear as top values.
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

# Comuputes the product of td and idf, thus generating the TF-IDF Score.
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)