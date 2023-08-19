import random


# TODO: Random Expressions.
class TreeNode:
    def __init__(self, op, a, b=None):
        self.op = op
        if b is None:
            self.left = None
            self.right = None
            self.val = a
        else:
            self.left = a
            self.right = b
            self.val = None

    def toString(self):
        if self.op == ' ':
            return str(self.val)
        else:
            return '(' + self.left.toString() + self.op + self.right.toString() + ')'


ops = ['+', '-', '*', '/']

def randfloat(a, b):
    return random.uniform(a, b)


def buildTree(numNodes) -> TreeNode:
    if numNodes == 1:
        return TreeNode(' ', randfloat(-100, 100))

    nleft = numNodes >> 1
    nright = numNodes - nleft
    left = buildTree(nleft)
    right = buildTree(nright)
    op = random.choice(ops)
    return TreeNode(op, left, right)