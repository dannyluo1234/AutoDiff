class TreeNode:
    def __init__(self, key, *, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return self._pretty(self)

    @staticmethod
    def _pretty(node):
        if node.left is None and node.right is None:
            return f'{node.key}'
        if node.left is not None and node.right is None:
            return f'{node.key}({node._pretty(node.left)})'
        return f'{node.key}({node._pretty(node.left)}, {node._pretty(node.right)})'

    def __add__(self, other):
        return TreeNode('add', left=self, right=other)
    def __sub__(self, other):
        return TreeNode('sub', left=self, right=other)
    def __mul__(self, other):
        return TreeNode('mul', left=self, right=other)
    def __truediv__(self, other):
        return TreeNode('div', left=self, right=other)

def main():
    a, b, c, d, e, f = [TreeNode(k) for k in list('abcdef')]
    tree = a - b * (c / d + e / f)
    print(tree)

if __name__ == "__main__":
    main()
