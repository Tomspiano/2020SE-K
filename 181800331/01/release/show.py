# -*- coding: utf-8 -*-
"""
Created on 2020/9/17

@author: Tomspiano

@email: wengenhui.gracie@foxmail.com

@description: show performance analysis result
"""
import pstats

if __name__ == '__main__':
    p = pstats.Stats("profile.stats")
    p.strip_dirs()
    p.sort_stats("cumulative")

    p.print_stats(0.2)
