class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, child):
        self.children.append(child)


if __name__ == '__main__':
    tree = TreeNode('Drinks', [])
    cold = TreeNode('Cold', [])
    hot = TreeNode('Hot', [])
    tea = TreeNode('Tea', [])
    coffee = TreeNode('Coffee', [])
    coke = TreeNode('Coke', [])
    pepsi = TreeNode('Pepsi', [])
    tree.add_child(cold)
    tree.add_child(hot)
    hot.add_child(coffee)
    hot.add_child(tea)
    cold.add_child(coke)
    cold.add_child(pepsi)
    print(tree)
