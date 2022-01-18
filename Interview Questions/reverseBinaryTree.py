class Node:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def solution(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    solution(root.left)
    solution(root.right)


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

    solution(tree)
