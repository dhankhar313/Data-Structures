class Node:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def leftViewRecursive(root, curr_level, max_level):
    if not root:
        return
    if curr_level > max_level[0]:
        print(root.data, end=' ')
        max_level[0] = curr_level
    leftViewRecursive(root.lChild, curr_level + 1, max_level)
    leftViewRecursive(root.rChild, curr_level + 1, max_level)


def leftViewIterative(root):
    if not root:
        return
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            if i == 0:
                print(node.data, end=' ')
            if node.lChild:
                queue.append(node.lChild)
            if node.rChild:
                queue.append(node.rChild)


def rightViewRecursive(root, curr_level, max_level):
    if not root:
        return
    if curr_level > max_level[0]:
        print(root.data, end=' ')
        max_level[0] = curr_level
    rightViewRecursive(root.rChild, curr_level + 1, max_level)
    rightViewRecursive(root.lChild, curr_level + 1, max_level)


def rightViewIterative(root):
    if not root:
        return
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            if i == n - 1:
                print(node.data, end=' ')
            if node.lChild:
                queue.append(node.lChild)
            if node.rChild:
                queue.append(node.rChild)


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
    leftViewRecursive(tree, 1, [0])
    print('\n')
    leftViewIterative(tree)
    print('\n')
    rightViewRecursive(tree, 1, [0])
    print('\n')
    rightViewIterative(tree)
