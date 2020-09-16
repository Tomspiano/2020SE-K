# -*- coding: utf-8 -*-
"""
Created on 2020/9/17

@author: Tomspiano

@email: wengenhui.gracie@foxmail.com

@description: preprocess documents
"""
import jieba


def get_stopwords(_path):
    """ Load stop words. """

    with open(_path, 'r', encoding='utf-8') as _doc:
        _stoplist = set(_doc.read().split())

    return _stoplist


def segment(_path, _stoplist):
    """ Segment the document(s) into words. """

    # remove stop words and tokenize
    _texts = []
    for document in _path:
        with open(document, 'r', encoding='utf-8') as _doc:
            lines = _doc.read().split()
            tokens = []
            for line in lines:
                tokens.extend(jieba.lcut_for_search(line))
            _texts.append([token for token in tokens if token not in _stoplist])

    return _texts



if __name__ == '__main__':
    stoplist = get_stopwords('../stopwords.txt')
    with open('stoplist.txt', 'w', encoding='utf-8') as f:
        for word in stoplist:
            f.write("'{}', ".format(word))
