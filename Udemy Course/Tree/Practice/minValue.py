from math import inf


class Node:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def iterative_function(root):
    if not root:
        return
    queue = [root]
    res = float(inf)
    while queue:
        node = queue.pop(0)
        if node.data < res:
            res = node.data
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)
    return res


def recursive_function(root):
    if not root:
        return float(inf)
    lMin = recursive_function(root.lChild)
    rMin = recursive_function(root.rChild)
    return min(root.data, lMin, rMin)


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

    print(iterative_function(tree))
    print(recursive_function(tree))
