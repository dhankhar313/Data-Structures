class TreeNode:
    def __init__(self, data):
        self.value = data
        self.lChild = None
        self.rChild = None


def iterative_check(root, target):
    if not root:
        return False
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.value == target:
            return True
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)
    return False


def recursive_check(root, target):
    if not root:
        return False
    if root.value == target:
        return True
    return recursive_check(root.lChild, target) or recursive_check(root.rChild, target)


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

    print(recursive_check(tree, 'Coke'))
    print(iterative_check(tree, 'Coke'))
    print(recursive_check(tree, 'Code'))
    print(iterative_check(tree, 'Code'))

