#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

NOT_FOUND = -1
N = 10


def binarySearch(x, a, left, right):
    while left <= right:
        mid = (left + right) / 2
        if a[mid] == x:
            return mid

        # 配列はソート済みで並んでいるという前提
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return NOT_FOUND

if __name__ == '__main__':
    array = []
    # 配列を作成する
    print 'array '
    for i in range(N):
        number = random.randint(0, 20) 
        array.append(number)

    array.sort()

    for i in range(N):
        print '[%d]:%d ' % (i, array[i])

    # print array

    # 探す配列を入力 TODO: 数値以外を入力した場合の例外チェック
    print '\n何を探しますか:'
    i = int(raw_input())

    # バイナリサーチ 
    r = binarySearch(i, array, 0, N - 1)

    if r == NOT_FOUND:
        print '%dは見つかりません\n' % (i)
    else:
        print '%dは%d番目です\n' % (i,r)
