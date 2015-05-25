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

    print '検索する値を入力してください(0を入力すると終了):'

    buf = 1
    while buf != 0:
        buf = intReader()

        if buf != 0:
            # 検索して見つかったら削除する
            thisNode = firstNode
            while thisNode != None:
                if  thisNode.data == buf:
                    print '入力された値のなかに%sが見つかりました。ノードを削除します。' % (buf)

                    if thisNode.prev != None:
                        thisNode.prev.next = thisNode.next
                    else:
                        firstNode = thisNode.next

                    if thisNode.next != None:
                        thisNode.next.prev = thisNode.prev
                    else:
                        lastNode = thisNode.prev


                thisNode = thisNode.next

            if thisNode == None:
                print '%sは入力されていないか、あるいはすでに削除されています。' % (buf)
