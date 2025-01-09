import sys
from antlr4 import *
from LPMSLexer import LPMSLexer
from LPMSParser import LPMSParser
from LPMSListener import LPMSListener
from SemanticAnalyzer import SemanticAnalyzer
from antlr4.tree.Tree import ParseTreeWalker


class ASTPrinter(LPMSListener):
    def enterProgram(self, ctx):
        print("Entering Program: ", ctx.getText())

    def exitProgram(self, ctx):
        print("Exiting Program: ", ctx.getText())

    def enterStatement(self, ctx):
        print("Entering Statement: ", ctx.getText())

    def exitStatement(self, ctx):
        print("Exiting Statement: ", ctx.getText())


def main(code):
    # Lê o código fonte
    print(f"Iniciando a análise do código: {code}")
    input_stream = FileStream(code)
    lexer = LPMSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Gerar o parser
    parser = LPMSParser(token_stream)

    # Realiza a análise sintática
    print("Iniciando a análise sintática...")
    tree = parser.program()  # Inicia a análise a partir da regra 'program'

    print("Análise sintática realizada com sucesso!")

    # Caminha pela árvore com um listener para imprimir os detalhes da AST
    print("\nIniciando a impressão da Árvore de Sintaxe Abstrata (AST):")
    walker = ParseTreeWalker()
    printer = ASTPrinter()
    walker.walk(printer, tree)

    # Exibe a árvore gerada (raw format)
    print("\nAST Tree (Raw):")
    print(tree.toStringTree(recog=parser))

    # Inicia a análise semântica
    print("\nIniciando a análise semântica...")
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.visit(tree)

    errors = semantic_analyzer.get_errors()

    # Verifica se houve erros semânticos
    if errors:
        for error in errors:
            print(f"Erro semântico: {error}")
    else:
        print("Análise semântica concluída com sucesso!")


if __name__ == '__main__':
    main("input.txt")
