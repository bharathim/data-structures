from Trees.TreeNode import TreeNode


class BinarySearchTree(object):
    def __init__(self, data):
        self.root = TreeNode(data)


if __name__ == "__main__":
    bst = BinarySearchTree(1)
    print(bst.root.data)
