import sys
from antlr4 import *
from LPMSLexer import LPMSLexer
from LPMSParser import LPMSParser
from SemanticAnalyzer import SemanticAnalyzer
from TACGenerator import TACGenerator


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
    print(f"Iniciando a análise do código: {code}")
    input_stream = FileStream(code, encoding="utf-8")
    lexer = LPMSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Etapa 1: Análise Léxica
    print("1ª etapa: análise léxica (scanner)")
    token_stream.fill()
    for token in token_stream.tokens:
        token_name = lexer.symbolicNames[token.type]
        print(f"<{token_name}, {token.text}>")

    # Gerar o parser
    parser = LPMSParser(token_stream)

    # Realiza a análise sintática
    print("\nIniciando a análise sintática...")
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Erro na análise sintática! Verifique a estrutura do código.")
        return

    print("Análise sintática realizada com sucesso!")

    # Exibe a árvore gerada
    print("\n2ª etapa: AST Tree (Raw):")
    print(tree.toStringTree(recog=parser))

    # Inicia a análise semântica
    print("\nIniciando a análise semântica...")
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.visit(tree)
    errors = semantic_analyzer.get_errors()

    if errors:
        for error in errors:
            print(f"Erro semântico: {error}")
    else:
        print("Análise semântica concluída com sucesso!")

    # Geração do Código Intermediário
    print("\n3ª etapa: Geração de Código de Três Endereços (TAC):")
    tac_generator = TACGenerator()
    tac_code = tac_generator.generate_TAC(tree)  # Chamada correta para gerar o código
    for instruction in tac_code:
        print(instruction)

if __name__ == '__main__':
    main("input.txt")
