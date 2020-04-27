# 링크 : https://www.acmicpc.net/problem/1991
# 참고한 곳 : https://home-body.tistory.com/424

def preorder(node):
    print(node.item, end='')
    if node.lchild != '.':
        preorder(tree[node.lchild])
    if node.rchild != '.':
        preorder(tree[node.rchild])

def inorder(node):
    if node.lchild != '.':
        inorder(tree[node.lchild])
    print(node.item, end='')
    if node.rchild != '.':
        inorder(tree[node.rchild])

def postorder(node):
    if node.lchild != '.':
        postorder(tree[node.lchild])
    if node.rchild != '.':
        postorder(tree[node.rchild])
    print(node.item, end='')

class Node:
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

if __name__ == '__main__':
    n = int(input())
    tree = {}
    for _ in range(n):
        data = input().split()
        tree[data[0]] = Node(item = data[0], lchild=data[1], rchild=data[2])
    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
