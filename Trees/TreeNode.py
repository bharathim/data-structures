class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert_iter(self, data):
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

    def insert_rec(self, data):
        if data < self.data:
            if self.left:
                self.left.insert_rec(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.insert_rec(data)
            else:
                self.right = TreeNode(data)

    def search_rec(self, data):
        if data < self.data:
            if self.left:
                if self.left.search_rec(data):
                    return True
                else:
                    return False
        elif data > self.data:
            if self.right:
                if self.right.search_rec(data):
                    return True
                else:
                    return False
        else:
            return True
