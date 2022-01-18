class Node:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def preOrder(root):
    if not root:
        return
    print(root.data, end=' ')
    preOrder(root.lChild)
    preOrder(root.rChild)


def inOrder(root):
    if not root:
        return
    inOrder(root.lChild)
    print(root.data, end=' ')
    inOrder(root.rChild)


def postOrder(root):
    if not root:
        return
    postOrder(root.lChild)
    postOrder(root.rChild)
    print(root.data, end=' ')


if __name__ == '__main__':
    tree = Node(25)
    hot = Node(12)
    cold = Node(-5)
    tea = Node(41)
    coffee = Node(-300)
    coke = Node(212)
    pepsi = Node(0)

    tree.lChild = hot
    tree.rChild = cold
    hot.lChild = tea
    hot.rChild = coffee
    cold.lChild = coke
    cold.rChild = pepsi

    preOrder(tree)
    print('\n')
    inOrder(tree)
    print('\n')
    postOrder(tree)
