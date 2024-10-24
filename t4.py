from t3 import lexer
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.lookahead = self.tokens[self.pos] if self.tokens else None

    def expr(self):
        result = self.term()
        while self.lookahead and self.lookahead[0] == 'OP':
            if self.lookahead[1] == '+':
                self.match('OP')
                result += self.term()
            elif self.lookahead[1] == '-':
                self.match('OP')
                result -= self.term()
        return result

    def term(self):
        if self.lookahead[0] == 'NUMBER':
            value = self.lookahead[1]
            self.match('NUMBER')
            return value
        else:
            raise SyntaxError(f"Erro de sintaxe: {self.lookahead}")

    def match(self, token_type):
        if self.lookahead and self.lookahead[0] == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.lookahead = self.tokens[self.pos]
            else:
                self.lookahead = None
        else:
            raise SyntaxError(f"Erro de sintaxe: esperado {token_type}, encontrado {self.lookahead}")


def main():
    with open('t4-input.txt', 'r', encoding='utf-8') as f:
        code = f.read()

    tokens = lexer(code)

    parser = Parser(tokens)

    result = parser.expr()
    print(f"Resultado: {result}")


if __name__ == '__main__':
    main()
