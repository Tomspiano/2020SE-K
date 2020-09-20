# -*- coding: utf-8 -*-
"""
Created on 2020/9/17
@Author: Tomspiano
@Email: wengenhui.gracie@foxmail.com
@Project: 2020SE-K
@Product: PyCharm
@Description: utilities for comparing documents
"""
import numpy as np
from dcheck import process as pc
from gensim import corpora


def get_jac_idx(s1, s2):
    """ Get Jaccard index.

    :param s1: word set 1
    :param s2: word set 2
    :return: whether both of the sets are empty and Jaccard index
    """

    if len(s1) == 0 and len(s2) == 0:
        return True, 1.0

    inter = s1 & s2
    union = s1 | s2
    return False, len(inter) / len(union)


def get_tf(texts, inter):
    """ Get term frequency.

    :param texts: lists of words
    :param inter: word domain
    :return: lists of term frequency
    """

    dictionary = corpora.Dictionary(texts)
    total = [len(text) for text in texts]

    corpus = [dictionary.doc2bow(text) for text in texts]
    tf = np.zeros((len(texts), len(dictionary)))
    for i, vec in enumerate(corpus):
        for word in vec:
            if dictionary[word[0]] in inter:
                tf[i][word[0]] = word[1] / total[i]

    return tf


def get_cos_sim(s1, s2, texts):
    """ Get cosine similarity.

    :param s1: word set 1
    :param s2: word set 2
    :param texts: lists of words
    :return: whether both of the sets are not empty and cosine similarity
    """

    inter = s1 & s2
    if len(inter) == 0:
        return False, 0.0

    tf = get_tf(texts, inter)

    cs = np.dot(tf[0], tf[1]) / (np.linalg.norm(tf[0]) * np.linalg.norm(tf[1]))
    return True, cs


def get_sim(texts):
    """ Get similarity.

    :param texts: lists of words
    :return: similarity of the two sets
    """

    ori_dic, smp_dic = pc.word2dic(texts)
    ori_set = set(ori_dic.token2id.keys())
    smp_set = set(smp_dic.token2id.keys())

    f1, jc = get_jac_idx(ori_set, smp_set)
    f2, cs = get_cos_sim(ori_set, smp_set, texts)

    if f1:
        return 1.0
    elif not f2:
        return 0.0
    else:
        return jc * cs


if __name__ == '__main__':
    pass
