import sys
from antlr4 import FileStream, CommonTokenStream
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser

def main():
    # Carrega o arquivo de entrada
    input_file = "input.txt"
    input_stream = FileStream(input_file)

    # Passa pelo lexer
    lexer = CalculadoraLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Passa pelo parser
    parser = CalculadoraParser(token_stream)
    tree = parser.programa()  # Inicia o parsing a partir da regra 'programa'

    print("Parsing concluído. A árvore sintática foi construída.")
    print(tree.toStringTree(recog=parser))  # Imprime a árvore sintática

if __name__ == "__main__":
    main()