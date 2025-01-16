import sys
from antlr4 import *
from LPMSLexer import LPMSLexer
from LPMSParser import LPMSParser
from SemanticAnalyzer import SemanticAnalyzer


def format_ast(node, parser):
    """ Formata a AST de maneira detalhada com operandos e operadores. """
    if node is None:
        return ""

    indent = " "
    if isinstance(node, TerminalNode):
        return f"{indent}{parser.symbolicNames[node.getSymbol().type]}: {node.getText()}"

    rule_name = parser.ruleNames[node.getRuleIndex()]
    formatted_children = ",".join([format_ast(child, parser) for child in node.children])
    return f"{indent}{rule_name}:{formatted_children}"


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

    # Exibe a árvore gerada (detalhada)
    print("\n2ª etapa: AST Tree (Detalhada):")
    print(format_ast(tree, parser))

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
