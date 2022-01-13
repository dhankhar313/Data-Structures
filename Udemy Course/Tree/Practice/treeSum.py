class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def iterative_function(root):
    if not root:
        return
    queue = [root]
    res = ''
    while queue:
        node = queue.pop(0)
        res += node.data
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)
    return res


def recursive_function(root):
    return '' if not root else root.data + recursive_function(root.lChild) + recursive_function(root.rChild)


if __name__ == '__main__':
    tree = TreeNode('Drinks')
    hot = TreeNode('Hot')
    cold = TreeNode('Cold')
    tea = TreeNode('Tea')
    coffee = TreeNode('Coffee')
    coke = TreeNode('Coke')
    pepsi = TreeNode('Pepsi')

    tree.lChild = hot
    tree.rChild = cold
    hot.lChild = tea
    hot.rChild = coffee
    cold.lChild = coke
    cold.rChild = pepsi

    print(iterative_function(tree))
    print(recursive_function(tree))
