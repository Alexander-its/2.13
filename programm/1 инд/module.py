# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

def fun1(type_='max'):
    def fun2(lst):
        return eval(f'{type_}(lst)')

    return fun2
