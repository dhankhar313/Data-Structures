class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0
        self.level = 0


# function should print the topView
# of the binary tree

def levelOrder(rootNode):
    if not rootNode:
        return
    queue = [rootNode]
    print('Level Order Traversal: ')
    while len(queue) > 0:
        print(queue[0].data, queue[0].hd)
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def topview(root):
    if not root:
        return
    root.hd = 0
    queue = [root]
    while len(queue):
        node = queue.pop()
        if node.left:
            node.left.hd = node.hd - 1
            queue.append(node.left)
        if node.right:
            node.right.hd = node.hd + 1
            queue.append(node.right)


# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.right = newNode(4)
    root.left.right.right = newNode(5)
    root.left.right.right.right = newNode(6)
    print("Following are nodes in top",
          "view of Binary Tree")
    topview(root)
    levelOrder(root)
