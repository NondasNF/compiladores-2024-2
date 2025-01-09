import sys
from antlr4 import FileStream, CommonTokenStream
from LPMSLexer import LPMSLexer


def test_lexer(input_code):
    # Lê o código de entrada
    input_stream = FileStream(input_code)
    # Cria o Lexer
    lexer = LPMSLexer(input_stream)
    # Itera sobre os tokens gerados
    tokens = lexer.getAllTokens()

    for token in tokens:
        print(f"Token: {token.text} | Type: {lexer.symbolicNames[token.type]}")


if __name__ == "__main__":
    test_lexer("input.txt")
