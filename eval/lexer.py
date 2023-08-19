from dataclasses import dataclass  # Basically a struct in C


TokenType_EOF = 0
TokenType_Error = 1
TokenType_Ident = 2
TokenType_Number = 3
TokenType_Plus = 4
TokenType_Minus = 5
TokenType_Star = 6
TokenType_Slash = 7
TokenType_Caret = 8
TokenType_OpenParen = 9
TokenType_CloseParen = 10
TokenType_Max = 11


class CStr:  # represents a C string (char*)
    def __init__(self, s: str):
        self.s = s  # the string in memory
        self.i = 0  # the index of the current character

    def get(self) -> str:
        if self.i >= len(self.s):
            return '\0'
        return self.s[self.i]


# Basically a struct in C
@dataclass
class Token:
    typ: int
    lexeme: str


class Lexer:
    start: CStr  # actually a char*, but python doesn't have those
    current: CStr

    def __init__(self, source: str):
        self.start = CStr(source)
        self.current = CStr(source)

    def next_token(self) -> Token:
        while self.current.get().isspace():
            self.current.i += 1
        self.start.i = self.current.i
        if self.current.get() == '\0':
            return self.make_token(TokenType_EOF)
        a = self.current.get()
        self.current.i += 1
        if a == '+':
            return self.make_token(TokenType_Plus)
        elif a == '-':
            return self.make_token(TokenType_Minus)
        elif a == '*':
            return self.make_token(TokenType_Star)
        elif a == '/':
            return self.make_token(TokenType_Slash)
        elif a == '^':
            return self.make_token(TokenType_Caret)
        elif a.isdigit():
            return self.number()
        elif a == '(':
            return self.make_token(TokenType_OpenParen)
        elif a == ')':
            return self.make_token(TokenType_CloseParen)
        else:
            if a.isalpha():
                return self.identifier()
            return self.make_token(TokenType_Error)

    def number(self) -> Token:
        while self.current.get().isdigit():
            self.current.i += 1
        if self.current.get() == '.':
            self.current.i += 1
            while self.current.get().isdigit():
                self.current.i += 1
        return self.make_token(TokenType_Number)

    def identifier(self) -> Token:
        while self.current.get().isalpha():
            self.current.i += 1
        return self.make_token(TokenType_Ident)

    def make_token(self, typ: int) -> Token:
        return Token(typ, self.start.s[self.start.i:self.current.i])
