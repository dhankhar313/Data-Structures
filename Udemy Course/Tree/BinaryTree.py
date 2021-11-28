class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.lChild)
    preOrder(rootNode.rChild)


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.lChild)
    print(rootNode.data)
    inOrder(rootNode.rChild)


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.lChild)
    postOrder(rootNode.rChild)
    print(rootNode.data)


def levelOrder(rootNode):
    if not rootNode:
        return
    queue = [rootNode]
    print('Level Order Traversal: ')
    while len(queue) > 0:
        print(queue[0].data)
        node = queue.pop(0)
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)


def searchBTUsingLevelOrder(rootNode, target):
    if not rootNode:
        return
    queue = [rootNode]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.data == target:
            return 'Found in Tree'
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)
    return 'Not Found in Tree'


def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return
    queue = [rootNode]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.lChild:
            queue.append(node.lChild)
        else:
            node.lChild = newNode
            return 'Inserted'
        if node.rChild:
            queue.append(node.rChild)
        else:
            node.rChild = newNode
            return 'Inserted'


def getDeepestNode(rootNode):
    if not rootNode:
        return
    queue = [rootNode]
    node = None
    while len(queue) > 0:
        node = queue.pop(0)
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)
    print('Deepest node is: ' + node.data)
    return node


def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    queue = [rootNode]
    while len(queue) > 0:
        node = queue.pop(0)
        if node is deepestNode:
            # print('Matched1: ', node, deepestNode)
            node.data = None
            return
        if node.lChild:
            if node.lChild is deepestNode:
                # print('Matched2: ', node.lChild, deepestNode)
                node.lChild = None
                return
            queue.append(node.lChild)
        if node.rChild:
            if node.rChild is deepestNode:
                # print('Matched3: ', node.rChild, deepestNode)
                node.rChild = None
                return
            queue.append(node.rChild)


def deleteNode(rootNode, target):
    if not rootNode:
        return
    queue = [rootNode]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.data == target:
            deepestNode = getDeepestNode(rootNode)
            node.data = deepestNode.data
            deleteDeepestNode(rootNode, deepestNode)
            print('Deleted the target node')
            return
        if node.lChild:
            queue.append(node.lChild)
        if node.rChild:
            queue.append(node.rChild)
    print('Element not found')


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
    # print('Preorder Traversal:')
    # preOrder(tree)
    # print('\nInorder Traversal:')
    # inOrder(tree)
    # print('\nPostOrder Traversal:')
    # postOrder(tree)
    # print('\nLevelOrder Traversal:')
    # levelOrder(tree)
    # print(searchBTUsingLevelOrder(tree, 'Tea'))
    # print(searchBTUsingLevelOrder(tree, 'Slice'))
    # print(searchBTUsingLevelOrder(tree, 'Coke'))
    # print(searchBTUsingLevelOrder(tree, 'Warm'))
    # newNode = TreeNode('Slice')
    # print(insertNode(tree, newNode))
    # print(getDeepestNode(tree))
    # deleteDeepestNode(tree, getDeepestNode(tree))
    levelOrder(tree)
    deleteNode(tree, 'Coffee')
    levelOrder(tree)
