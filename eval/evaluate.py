from .parser import *


def evaluateExpr(node: ExprNode):
    if node.typ == NodeType_Number:
        return node.value
    elif node.typ == NodeType_Positive:
        return evaluateExpr(node.value)
    elif node.typ == NodeType_Negative:
        return -evaluateExpr(node.value)
    elif node.typ == NodeType_Add:
        return evaluateExpr(node.left) + evaluateExpr(node.right)
    elif node.typ == NodeType_Sub:
        return evaluateExpr(node.left) - evaluateExpr(node.right)
    elif node.typ == NodeType_Mul:
        return evaluateExpr(node.left) * evaluateExpr(node.right)
    elif node.typ == NodeType_Div:
        return evaluateExpr(node.left) / evaluateExpr(node.right)
    elif node.typ == NodeType_Pow:
        return evaluateExpr(node.left) ** evaluateExpr(node.right)
    else:
        print("Error: Unknown node type")


def printTree(tree: ExprNode, depth=0):
    for i in range(depth):
        if i == depth - 1:
            print(" |-", end="")
        else:
            print(" | ", end="")

    if tree.typ == NodeType_Number:
        print("Num:", tree.value)
    elif tree.typ == NodeType_Positive:
        print("Positive")
        printTree(tree.value, depth + 1)
    elif tree.typ == NodeType_Negative:
        print("Negative")
        printTree(tree.value, depth + 1)
    elif tree.typ == NodeType_Add:
        print("Add")
        printTree(tree.left, depth + 1)
        printTree(tree.right, depth + 1)
    elif tree.typ == NodeType_Sub:
        print("Sub")
        printTree(tree.left, depth + 1)
        printTree(tree.right, depth + 1)
    elif tree.typ == NodeType_Mul:
        print("Mul")
        printTree(tree.left, depth + 1)
        printTree(tree.right, depth + 1)
    elif tree.typ == NodeType_Div:
        print("Div")
        printTree(tree.left, depth + 1)
        printTree(tree.right, depth + 1)
    elif tree.typ == NodeType_Pow:
        print("Pow")
        printTree(tree.left, depth + 1)
        printTree(tree.right, depth + 1)
    else:
        print("Error: Unknown node type")


def evaluate(expr: str, print_tree=False):
    pa = Parser(expr)
    tree = pa.parseExpression()
    if print_tree:
        printTree(tree)
    return evaluateExpr(tree)

