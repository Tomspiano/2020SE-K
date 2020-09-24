# -*- coding: utf-8 -*-
"""
Created on 2020/9/17
@Author: Tomspiano
@Email: wengenhui.gracie@foxmail.com
@Project: plagiarism-checker
@Product: PyCharm
@Description: preprocess documents
"""
import jieba
from gensim import corpora


def get_stopwords(path):
    """ Load stop words.

    :param path: path of the stopwords file
    :return: stopwords set
    """

    with open(path, 'r', encoding='utf-8') as doc:
        stoplist = set(doc.read().split())

    return stoplist


def segment(path, stoplist):
    """ Segment the documents into words.

    :param path: path of the documents
    :param stoplist: stopwords set
    :return: lists of processed words
    """

    # remove stopwords and tokenize
    texts = []
    for document in path:
        with open(document, 'r', encoding='utf-8') as doc:
            tokens = []
            lines = doc.readlines()
            for line in lines:
                tokens.extend(jieba.lcut_for_search(line.strip()))
            texts.append([token for token in tokens if token not in stoplist])

    return texts


def word2dic(texts):
    """ Convert every lists of words into dictionary.

    :param texts: lists of processed words
    :return: word dictionary
    """

    ori_dic = corpora.Dictionary([texts[0]])
    smp_dic = corpora.Dictionary([texts[1]])

    return ori_dic, smp_dic


if __name__ == '__main__':
    stopwords = get_stopwords('../stopwords.txt')
    with open('stoplist.txt', 'w', encoding='utf-8') as f:
        for word in stopwords:
            f.write("'{}', ".format(word))
