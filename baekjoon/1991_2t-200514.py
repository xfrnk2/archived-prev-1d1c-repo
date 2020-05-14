def pre_order(node):
    print(node.item, end=' ')
    if node.left_child != '.':
        pre_order(tree[node.left_child])
    if node.right_child != '.':
        pre_order(tree[node.right_child])

def in_order(node):

    if node.left_child != '.':
        in_order(tree[node.left_child])
    print(node.item, end=' ')
    if node.right_child != '.':
        in_order(tree[node.right_child])

def post_order(node):

    if node.left_child != '.':
        post_order(tree[node.left_child])
    if node.right_child != '.':
        post_order(tree[node.right_child])
    print(node.item, end=' ')
class Node:
    def __init__(self, item, left_child, right_child):
        self.item = item
        self.left_child = left_child
        self.right_child = right_child

if __name__ == '__main__':
    tree = {}
    for _ in range(int(input())):
        data = input().split()
        tree[data[0]] = Node(item=data[0], left_child=data[1], right_child=data[2])
    pre_order(tree['A'])
    print()
    in_order(tree['A'])
    print()
    post_order(tree['A'])