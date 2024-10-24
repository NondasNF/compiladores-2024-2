# Calculadora Memorizada com Lexer e Parser Preditivo

Este projeto implementa um lexer e um parser preditivo para processar expressões aritméticas básicas de uma calculadora. O lexer converte o código fonte em tokens, enquanto o parser interpreta os tokens e avalia as expressões. 

### Arquivos

- **t3.py**: Implementa o analisador léxico (lexer) para converter o código de entrada em tokens.
- **t4.py**: Implementa o parser preditivo que processa os tokens e calcula o resultado da expressão.
- **t3-input.txt**: Contém a expressão que o lexer irá processar.
- **t4-input.txt**: Contém a expressão que o parser irá processar.

## Como Executar

Siga os passos abaixo para rodar o projeto em sua máquina:

### Pré-requisitos

- **Python 3.x** deve estar instalado em sua máquina.
  
### Passo a Passo

1. Clone o repositório ou faça download dos arquivos do projeto.
2. Navegue até o diretório onde os arquivos estão salvos:

    ```bash
    cd /Compiladores-2024-2
    ```

3. Abra o arquivo `input.txt` e insira a expressão aritmética que deseja avaliar. Exemplo de conteúdo:

    ```
    1 + 2 - 9
    ```

4. Execute o arquivo `parser.py` no terminal:

    ```bash
    python t4.py
    ```

5. O resultado da expressão será exibido no terminal. Por exemplo:

    ```
    Resultado: -6
    ```

### Detalhes Técnicos

- **Lexer**: O lexer em `t3.py` utiliza expressões regulares para identificar e classificar diferentes partes da expressão como tokens, como números, operadores e identificadores.
- **Parser**: O parser preditivo em `t4.py` implementa uma análise sintática recursiva para interpretar a expressão e calcular o resultado final.

### Estrutura dos Tokens

Os tokens gerados pelo lexer têm o seguinte formato:

- **NUMBER**: Representa números inteiros.
- **OP**: Operadores como `+` e `-`.
- **ASSIGN**: Operadores de atribuição, como `=`.
- **ID**: Identificadores que representam variáveis.
- **REL_OP**: Operadores de comparação como `==`.
- **PAREN**: Parênteses para agrupar expressões.
