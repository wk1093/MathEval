from .lexer import *


NodeType_Error = 0
NodeType_Number = 1
NodeType_Positive = 2
NodeType_Negative = 3
NodeType_Add = 4
NodeType_Sub = 5
NodeType_Mul = 6
NodeType_Div = 7
NodeType_Pow = 8


class ExprNode:
    def __init__(self, typ, value=None, left=None, right=None):
        self.typ = typ
        self.value = value
        self.left = left
        self.right = right


Prec_Min = 0
Prec_Term = 1
Prec_Factor = 2
Prec_Exp = 3
Prec_Max = 4


precLookup = {
    TokenType_Plus: Prec_Term,
    TokenType_Minus: Prec_Term,
    TokenType_Star: Prec_Factor,
    TokenType_Slash: Prec_Factor,
    TokenType_Caret: Prec_Exp,
    0: Prec_Min
}


class Parser:
    def __init__(self, expression):
        self.curr = None
        self.lexer = Lexer(expression)
        self.advance()

    def advance(self):
        self.curr = self.lexer.next_token()

    def parseNumber(self):
        node = ExprNode(NodeType_Number, float(self.curr.lexeme))
        self.advance()
        return node

    def parseInfixExpr(self, op: Token, left: ExprNode):
        node = ExprNode(NodeType_Error)
        if op.typ == TokenType_Plus:
            node.typ = NodeType_Add
        elif op.typ == TokenType_Minus:
            node.typ = NodeType_Sub
        elif op.typ == TokenType_Star:
            node.typ = NodeType_Mul
        elif op.typ == TokenType_Slash:
            node.typ = NodeType_Div
        elif op.typ == TokenType_Caret:
            node.typ = NodeType_Pow
        else:
            print(f"Infix operator invalid, got: {op.typ}: '{op.lexeme}'")
        node.left = left
        node.right = self.parseExpression(precLookup.get(op.typ, Prec_Min))
        return node

    def parseTerminalExpr(self):
        node = ExprNode(NodeType_Error)
        if self.curr.typ == TokenType_Number:
            node = self.parseNumber()
        elif self.curr.typ == TokenType_OpenParen:
            self.advance()
            node = self.parseExpression(Prec_Min)
            if self.curr.typ == TokenType_CloseParen:
                self.advance()
        elif self.curr.typ == TokenType_Plus:
            self.advance()
            node = ExprNode(NodeType_Positive, self.parseTerminalExpr())
        elif self.curr.typ == TokenType_Minus:
            self.advance()
            node = ExprNode(NodeType_Negative, self.parseTerminalExpr())
        else:
            print(f"Terminal expression invalid, got: {self.curr.typ}: '{self.curr.lexeme}'")
        if self.curr.typ == TokenType_Number or self.curr.typ == TokenType_OpenParen:
            next_n = ExprNode(NodeType_Mul)
            next_n.left = node
            next_n.right = self.parseExpression(Prec_Factor)
            node = next_n
        return node

    def parseExpression(self, prec=Prec_Min):
        left = self.parseTerminalExpr()
        currOp = self.curr
        curPrec = precLookup.get(currOp.typ, Prec_Min)
        while curPrec != Prec_Min:
            if prec >= curPrec:
                break
            else:
                self.advance()
                left = self.parseInfixExpr(currOp, left)
                currOp = self.curr
                curPrec = precLookup.get(currOp.typ, Prec_Min)
        return left
