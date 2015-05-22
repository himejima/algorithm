#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListNodeForList:
    def __init__(self, data):
        self.data = data

    # 後の要素 
    next = None 

    # 前の要素
    prev = None

def intReader():
    try:
        return int(raw_input())
    except:
        return 0

if __name__ == '__main__':
    firstNode = None
    lastNode = None
    buf = 1
    print '整数を入力してください (0を入力すると終了):'


    while buf != 0:
        buf = intReader()

        if buf != 0:
            # 新しいノードを作成
            newNode = ListNodeForList(buf)
            newNode.next = None

            if lastNode != None:
                # すでにあるリストの末尾に新しいノードをつなげる
                # 最後のNodeの次を新しく作成したNodeにする
                lastNode.next = newNode
                # 新しく作成したNodeの前を最後の作成したNodeにする
                newNode.prev = lastNode
                # 最後のNodeを新しく作成したNodeにする
                lastNode = newNode
            else:
                # これが最初の要素だった
                firstNode = lastNode = newNode
                newNode.prev = None
    

    # 合計値を算出
    sum = 0
    print '--入力されたのは以下の数です--'
    thisNode = firstNode
    while thisNode != None:
        print '%s ' % (thisNode.data)
        sum += thisNode.data
        thisNode = thisNode.next

    print '\n以上の数の合計値は %sです' % (sum)
