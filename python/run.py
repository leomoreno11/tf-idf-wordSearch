# -*- coding: utf-8 -*-
import os
from tfidf_funcs import *

filelist, bloblist = [], []
def read_files (file_path, bloblist):
    with open(file_path, 'r') as file:
        bloblist += [tb('{}'.format(file.read().upper()))]

with open('directory.txt') as file:
    blobspath = file.read()
    os.chdir(blobspath)

for file in os.listdir():
    if file.endswith('.txt'):
        file_path = "{}/{}".format(blobspath, file)
        filelist.append(file)
        read_files(file_path, bloblist)

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(filelist[i]))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {} | TF-IDF {} ".format(word, round(score, 5)))