from random import randint

from Trees.TreeNode import TreeNode


class BinarySearchTree(object):
    def __init__(self, data):
        self.root = TreeNode(data)

    def insert_iter(self, data):
        if self.root:
            self.root.insert_iter(data)
        else:
            self.root = TreeNode(data)

    def insert_rec(self, data):
        if self.root:
            self.root.insert_rec(data)
        else:
            self.root = TreeNode(data)

    def search_rec(self, data):
        return self.root.search_rec(data) if self.root else False

    def display(self, node):
        lines, _, _, _ = self._display_aux(node)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """
        Returns list of strings, width, height,
        and horizontal coordinate of the root.
        """
        # No child.
        if node.right is None and node.left is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.data)
            u = len(s)
            #        first_line = s + x * '_' + (n - x) * ' '
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == "__main__":
    bst = BinarySearchTree(50)
    for _ in range(15):
        e = randint(0, 100)
        bst.insert_rec(e)
    bst.display(bst.root)

    #print(bst.search_rec(50))
    print(bst.search_rec(28))

