# Compilador LPMS

## Descrição
Este projeto é um compilador para a linguagem LPMS, implementado utilizando a ferramenta ANTLR4 para realizar a análise léxica, sintática e semântica.

## Estrutura do Projeto
- `main.py` - Arquivo principal que orquestra as etapas do compilador.
- `LPMSLexer.py` - Gerado pelo ANTLR4, responsável pela análise léxica.
- `LPMSParser.py` - Gerado pelo ANTLR4, realiza a análise sintática.
- `LPMSListener.py` - Listener para percorrer a Árvore de Sintaxe Abstrata (AST).
- `SemanticAnalyzer.py` - Responsável pela análise semântica.
- `input.txt` - Arquivo de entrada contendo o código-fonte a ser analisado.

## Execução
Para executar o compilador, utilize o seguinte comando:
```sh
python main.py
```
O arquivo `input.txt` deve conter o código a ser analisado.

## Etapas do Compilador

### 1. Análise Léxica (Scanner)
Na primeira etapa, o compilador transforma o código-fonte em uma lista de tokens lexicais.

**Exemplo de Saída:**
```
1ª etapa: análise léxica (scanner)
<PROGRAM, Program>
<IDENTIFIER, Teste>
<LBRACE, {>
<INT_TYPE, int>
<IDENTIFIER, x>
<SEMICOLON, ;>
<IDENTIFIER, x>
<ASSIGN, =>
<NUMBER, 5>
<SEMICOLON, ;>
<RBRACE, }>
<COMMENT, <EOF>>
```

### 2. Análise Sintática e Construção da AST
O parser constrói a Árvore de Sintaxe Abstrata (AST) e verifica a estrutura gramatical.

**Exemplo de Saída:**
```
Iniciando a análise sintática...
Análise sintática realizada com sucesso!

2ª etapa: AST Tree (Raw):
(program Program Teste { (block (stmt (declaration int x ;)) (stmt (assignment x = (expression (term (factor 5))) ;))) } <EOF>)
```

Caso haja erros sintáticos, eles serão reportados com a linha correspondente.

### 3. Análise Semântica
Através da AST gerada, o analisador semântico verifica regras de coerência e tipos.

**Exemplo de Saída:**
```
Iniciando a análise semântica...
Análise semântica concluída com sucesso!
```
Se houver erros semânticos, eles serão reportados.

## Requisitos
- Python 3.7+
- ANTLR4

Para instalar as dependências:
```sh
pip install antlr4-python3-runtime
```

## Autor
Epaminondas

Este projeto foi desenvolvido como parte dos estudos em compiladores, utilizando ANTLR4 para análise léxica, sintática e semântica.

