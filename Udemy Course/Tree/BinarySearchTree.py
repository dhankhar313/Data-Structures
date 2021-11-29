import BinaryTree as bt
from collections import deque


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def insertNode(rootNode, value):
    if not rootNode.data:
        rootNode.data = value
    elif value <= rootNode.data:
        if not rootNode.lChild:
            rootNode.lChild = BSTNode(value)
        else:
            insertNode(rootNode.lChild, value)
    else:
        if not rootNode.rChild:
            rootNode.rChild = BSTNode(value)
        else:
            insertNode(rootNode.rChild, value)


def searchNode(rootNode, value):
    if rootNode.data == value:
        print("Found in Tree")
    elif value < rootNode.data:
        if rootNode.lChild:
            if rootNode.lChild.data == value:
                print("Found in Tree")
            else:
                searchNode(rootNode.lChild, value)
    else:
        if rootNode.rChild:
            if rootNode.rChild.data == value:
                print("Found in Tree")
            else:
                searchNode(rootNode.rChild, value)


def minValueNode(rootNode):
    node = rootNode
    while node.lChild:
        node = node.lChild
    return node


def deleteNode(rootNode, value):
    if not rootNode:
        return rootNode
    if value <= rootNode.data:
        pass
    # Incomplete 


def invertBST(rootNode):
    if not rootNode:
        return
    queue = [rootNode]
    while len(queue) > 0:
        node = queue.pop(0)
        node.lChild, node.rChild = node.rChild, node.lChild
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)


def deleteTree(rootNode):
    rootNode.data = None
    rootNode.lChild = None
    rootNode.rChild = None
    return 'Tree Deleted'


def rightView(rootNode):
    if not rootNode:
        return
    queue = deque()
    queue.append(rootNode)
    while queue:
        n = len(queue)
        while n:
            n -= 1
            node = queue.popleft()
            if n == 0:
                print(node.data, end=' ')
            if node.lChild:
                queue.append(node.lChild)
            if node.rChild:
                queue.append(node.rChild)


def leftView(rootNode):
    if not rootNode:
        return
    queue = deque()
    queue.append(rootNode)
    while queue:
        n = len(queue)
        flag = True
        while n:
            node = queue.popleft()
            if flag:
                print(node.data, end=" ")
                flag = False
            if node.lChild:
                queue.append(node.lChild)
            if node.rChild:
                queue.append(node.rChild)
            n -= 1


if __name__ == "__main__":
    tree = BSTNode(None)
    insertNode(tree, 70)
    insertNode(tree, 50)
    insertNode(tree, 90)
    insertNode(tree, 30)
    insertNode(tree, 60)
    insertNode(tree, 80)
    insertNode(tree, 100)
    insertNode(tree, 20)
    insertNode(tree, 40)
    # bt.preOrder(tree)
    # bt.inOrder(tree)
    # bt.postOrder(tree)
    # bt.levelOrder(tree)
    # searchNode(tree, 100)
    # searchNode(tree, 213)
    # bt.levelOrder(tree)
    # invertBST(tree)
    leftView(tree)
    rightView(tree)
    # bt.levelOrder(tree)
