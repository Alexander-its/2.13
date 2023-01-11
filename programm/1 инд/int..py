#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import sys
from module import fun1

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 65, 6, ]
    max_fun = fun1()
    min_fun = fun1('min')
    print(max_fun(a))
    print(min_fun(a))
