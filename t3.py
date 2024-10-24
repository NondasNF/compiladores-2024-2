import re

token_specification = [
    ('NUMBER',      r'\b\d+\b'),           # Constantes numéricas
    ('ASSIGN',      r'(<-|=)'),             # Operadores de atribuição
    ('REL_OP',      r'=='),                # Operador relacional
    ('ID',          r'[a-zA-Z_]\w*'),      # Identificadores
    ('OP',          r'[+\-*]'),            # Operadores aritméticos
    ('LPAREN',      r'\('),                # Parêntese esquerdo
    ('RPAREN',      r'\)'),                # Parêntese direito
    ('NEWLINE',     r'\n'),                # Nova linha
    ('SKIP',        r'[ \t]+'),            # Espaços e tabulações
    ('MISMATCH',    r'.'),                 # Caracteres não reconhecidos
]

token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def lexer(code):
    line_num = 1
    line_start = 0
    tokens = []
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} inesperado na linha {line_num}')
        tokens.append((kind, value, line_num, column))
    return tokens

def main():
    with open('t3-input.txt', 'r', encoding='utf-8') as f:
        code = f.read()

    tokens = lexer(code)

    for token in tokens:
        print(token)

if __name__ == '__main__':
    main()