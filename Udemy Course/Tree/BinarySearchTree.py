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


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


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


def zigzagTraversal(rootNode):
    # Base Case
    if not rootNode:
        return

    # Create two stacks to store current
    # and next level
    currLevel = []
    nextLevel = []

    # if flag is true push nodes from
    # left to right otherwise from
    # right to left
    flag = True

    # append rootNode to currLevel stack
    currLevel.append(rootNode)

    # Check if stack is empty
    while len(currLevel) > 0:
        # pop from stack
        temp = currLevel.pop(-1)
        # print the data
        print(temp.data, " ", end="")

        if flag:
            # if flag is true push left
            # before right
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            # else push right before left
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currLevel) == 0:
            # reverse flag to push node in
            # opposite order
            flag = not flag
            # swapping of stacks
            currLevel, nextLevel = nextLevel, currLevel


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
