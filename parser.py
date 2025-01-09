import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from LPMSLexer import LPMSLexer
from LPMSParser import LPMSParser
from LPMSListener import LPMSListener


class ASTPrinter(LPMSListener):
    def enterProgram(self, ctx):
        print("Entering Program: ", ctx.getText())

    def exitProgram(self, ctx):
        print("Exiting Program: ", ctx.getText())

    def enterStatement(self, ctx):
        print("Entering Statement: ", ctx.getText())

    def exitStatement(self, ctx):
        print("Exiting Statement: ", ctx.getText())


def test_parser(input_file):
    # Lê o código fonte
    input_stream = FileStream(input_file)
    lexer = LPMSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LPMSParser(token_stream)

    # Realiza a análise sintática
    tree = parser.program()

    # Caminha pela árvore com um listener
    walker = ParseTreeWalker()
    printer = ASTPrinter()
    walker.walk(printer, tree)

    # Exibe a árvore gerada (opcional)
    print("\nAST Tree (Raw):")
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    test_parser("input.txt")
