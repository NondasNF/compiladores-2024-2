import sys
from antlr4 import *
from LPMSLexer import LPMSLexer
from LPMSParser import LPMSParser
from LPMSListener import LPMSListener
from SemanticAnalyzer import SemanticAnalyzer
from antlr4.tree.Tree import ParseTreeWalker


class ASTPrinter(LPMSListener):
    def enterProgram(self, ctx):
        print(f"Entering program: {ctx.getText()}")

    def exitProgram(self, ctx):
        print(f"Exiting program: {ctx.getText()}")

    def enterEveryRule(self, ctx):
        rule_name = LPMSParser.ruleNames[ctx.getRuleIndex()]

        # Ignorar o "program" porque já tratamos separadamente
        if rule_name == "program":
            return

        # Formatar texto para melhorar legibilidade
        formatted_text = " ".join(ctx.getText().replace("{", " { ").replace("}", " } ").split())

        print(f"Entering {rule_name}: {formatted_text}")

    def exitEveryRule(self, ctx):
        rule_name = LPMSParser.ruleNames[ctx.getRuleIndex()]

        if rule_name == "program":
            return

        formatted_text = " ".join(ctx.getText().replace("{", " { ").replace("}", " } ").split())

        print(f"Exiting {rule_name}: {formatted_text}")

def main(code):
    # Lê o código fonte
    print(f"Iniciando a análise do código: {code}")
    input_stream = FileStream(code, encoding="utf-8")
    lexer = LPMSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Etapa 1: Análise Léxica
    print("1ª etapa: análise léxica (scanner)")
    token_stream.fill()  # Garante que todos os tokens sejam processados
    for token in token_stream.tokens:
        token_name = lexer.symbolicNames[token.type]
        print(f"<{token_name}, {token.text}>")

    # Gerar o parser
    parser = LPMSParser(token_stream)

    # Realiza a análise sintática
    print("\nIniciando a análise sintática...")
    tree = parser.program()  # Inicia a análise a partir da regra 'program'

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Erro na análise sintática! Verifique a estrutura do código.")
        return

    print("Análise sintática realizada com sucesso!")

    # # Caminha pela árvore com um listener para imprimir os detalhes da AST
    # print("\nIniciando a impressão da Árvore de Sintaxe Abstrata (AST):")
    # walker = ParseTreeWalker()
    # printer = ASTPrinter()
    # walker.walk(printer, tree)

    # Exibe a árvore gerada (raw format)
    print("\n2ª etapa: AST Tree (Raw):")
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
