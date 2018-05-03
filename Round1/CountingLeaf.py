tree = [1, 5, 5, 2, 2, -1, 3]
#          5
#        /  \
#       1    2
#      /    / \
#     0    3   4
#         /
#       6
# 5
# -1 0 0 1 1
# 2
tree = [-1, 0, 0, 1, 1]
#      0
#
#    1   2
#
#  3  4

tree = "2 0 -1 1 1 2 1 3"
delNode = 2

tree = tree.split(" ")
tree = [int(i) for i in tree]

def deleteNode(tree, delNode):
    if tree[delNode] == -1:
        return 0
    for i in range(len(tree)):
        if tree[i] == delNode:
            tree[i] = -99
            deleteNode(tree, i)


cnt = 0
def findLeaf(tree, p):
    c = deleteNode(tree, delNode)
    if c == 0:
        return 0
    global cnt
    flag = 0
    for i in range(len(tree)):
        if tree[i] == p:
            flag = 1
            findLeaf(tree, i)
        if flag == 0 and i == len(tree)-1:
            cnt += 1
    return cnt

count = findLeaf(tree, -1)
print(tree)
print(count)
