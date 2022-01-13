from math import inf


class Node:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def recursive_function(root):
    if not root:
        return -float(inf)
    if not root.lChild and not root.rChild:
        return root.data
    return root.data + max(recursive_function(root.lChild), recursive_function(root.rChild))


if __name__ == '__main__':
    tree = Node(25)
    hot = Node(12)
    cold = Node(-5)
    tea = Node(41)
    coffee = Node(-300)
    coke = Node(212)
    pepsi = Node(0)
    '''
            25
           /  \
         12   -5
         /\    /\
      41 -300 212 0
    '''

    tree.lChild = hot
    tree.rChild = cold
    hot.lChild = tea
    hot.rChild = coffee
    cold.lChild = coke
    cold.rChild = pepsi

    print(recursive_function(tree))
