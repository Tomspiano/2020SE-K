# -*- coding: utf-8 -*-
"""
Created on 2020/9/17

@author: Tomspiano

@email: wengenhui.gracie@foxmail.com

@description: utilities for comparing documents
"""
from collections import defaultdict


def get_tf(_text):
    """ Get term frequency of the document(s). """

    _frequency = [defaultdict(int)] * len(_text)
    for _i, text in enumerate(_text):
        for token in text:
            _frequency[_i][token] += 1

    return _frequency


if __name__ == '__main__':
    pass
