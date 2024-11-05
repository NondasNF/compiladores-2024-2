
## Pré-requisitos

- Python 3.x
- ANTLR 4.x

## Configuração e Execução

1. **Gerar Lexer e Parser**: No terminal do PyCharm, execute o comando:

    ```bash
    antlr4 -Dlanguage=Python3 Calculadora.g4
    ```

2. **Configurar o Arquivo de Entrada**: Adicione uma expressão no arquivo `input.txt`. Exemplo:

    ```
    dinheiro = 1
    realizacao = 2
    felicidade = dinheiro + realizacao
    ```

3. **Executar o Parser**: Execute o script principal `main.py` no terminal ou PyCharm:

    ```bash
    python main.py
    ```

4. A saída exibirá a árvore sintática da expressão.

### Licença

Este projeto está licenciado sob a licença MIT.
