class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, data):
        current = self
        parent = None
        while current:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        if data < parent.data:
            parent.left = TreeNode(data)
        else:
            parent.right = TreeNode(data)

