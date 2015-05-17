#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

NOT_FOUND = -1
N = 10

def linearSearchV2(x, a, num):
    n = 0

    # 最後の値を入れ替える
    t = a[num - 1]
    a[num - 1] = x

    # 配列の範囲内で目的の値を探す
    while a[n] != x:
        n = n + 1

    a[num - 1] = t

    if n < num - 1:
        return n

    if x == t:
        return n
    
    return NOT_FOUND

if __name__ == '__main__':
    array = []
    # 配列を作成する
    print 'array '
    for i in range(N):
        number = random.randint(0, 20) 
        array.append(number)
        print '[%d]:%d ' % (i, number)

    # print array

    # 探す配列を入力 TODO: 数値以外を入力した場合の例外チェック
    print '\n何を探しますか:'
    i = int(raw_input())

    # リニアサーチ(番兵)
    r = linearSearchV2(i, array, N)

    if r == NOT_FOUND:
        print '%dは見つかりません\n' % (i)
    else:
        print '%dは%d番目です\n' % (i,r)
