from LPMSVisitor import LPMSVisitor
from LPMSParser import LPMSParser
from antlr4.tree.Tree import TerminalNode

class TACGenerator(LPMSVisitor):
    def __init__(self):
        self.temp_count = 0  # Contador de variáveis temporárias
        self.label_count = 0  # Contador de rótulos para controle de fluxo
        self.tac_instructions = []  # Lista de instruções TAC
        self.errors = []  # Lista para armazenar erros

    def new_temp(self):
        """ Cria uma nova variável temporária """
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        """ Cria um novo rótulo para controle de fluxo """
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, result, op1, operator=None, op2=None):
        """ Gera uma instrução de código de três endereços """
        if operator:
            self.tac_instructions.append(f"{result} = {op1} {operator} {op2}")
        else:
            self.tac_instructions.append(f"{result} = {op1}")
        return result

    def visitAssignment(self, ctx: LPMSParser.AssignmentContext):
        var_name = ctx.IDENTIFIER().getText()
        expr_temp = self.visit(ctx.expression())
        self.emit(var_name, expr_temp)

    def visitExpression(self, ctx: LPMSParser.ExpressionContext):
        """ Gera código para expressão aritmética respeitando a precedência """
        op1 = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            operator = ctx.getChild(2 * i - 1).getText()  # Captura operadores + ou -
            op2 = self.visit(ctx.term(i))
            temp_var = self.new_temp()
            self.emit(temp_var, op1, operator, op2)
            op1 = temp_var
        return op1

    def visitTerm(self, ctx: LPMSParser.TermContext):
        """ Gera código para termos respeitando a precedência de * e / """
        op1 = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operator = ctx.getChild(2 * i - 1).getText()  # Captura operadores * ou /
            op2 = self.visit(ctx.factor(i))
            temp_var = self.new_temp()
            self.emit(temp_var, op1, operator, op2)
            op1 = temp_var
        return op1

    def visitIfStmt(self, ctx):
        condition_temp = self.visit(ctx.expression())

        label_then = self.new_label()
        label_else = self.new_label()
        label_end = self.new_label()

        # Gerar a instrução de salto condicional
        self.tac_instructions.append(f"if {condition_temp} goto {label_then}")
        self.tac_instructions.append(f"goto {label_else}")

        # Bloco do 'then'
        self.tac_instructions.append(f"{label_then}:")
        self.visit(ctx.block(0))  # Visitando o bloco do 'if'
        self.tac_instructions.append(f"goto {label_end}")

        # Bloco do 'else', se houver
        if ctx.ELSE():
            self.tac_instructions.append(f"{label_else}:")
            self.visit(ctx.block(1))  # Visitando o bloco do 'else'

        self.tac_instructions.append(f"{label_end}:")

    def visitDeclaration(self, ctx: LPMSParser.DeclarationContext):
        var_list = ctx.IDENTIFIER()
        for var in var_list:
            var_name = var.getText()
            self.emit(var_name, "0")  # Inicializa como 0 se não for atribuído valor

    def visitFactor(self, ctx: LPMSParser.FactorContext):
        """ Trata fatores, incluindo identificadores, números e expressões entre parênteses """
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.LPAREN():
            return self.visit(ctx.expression())  # Resolvendo expressões entre parênteses
        return None

    def visitPrintStmt(self, ctx):
        args = ctx.expression()

        if not args or len(args) == 0:
            self.tac_instructions.append("Erro: Nenhum argumento válido para print")
            return

        arg_list = []
        for arg in args:
            # Verificar se o argumento é uma string literal verificando o texto diretamente
            if arg.getText().startswith('"') and arg.getText().endswith('"'):
                arg_list.append(arg.getText())  # Adiciona a string completa com aspas
            else:
                # Trata os outros argumentos normalmente (variáveis ou expressões)
                result = self.visit(arg)
                if result:
                    arg_list.append(result)
                else:
                    self.tac_instructions.append("Erro: Argumento inválido para print")

        if len(arg_list) > 0:
            print_str = ", ".join(arg_list)
            self.tac_instructions.append(f"print {print_str}")
        else:
            self.tac_instructions.append("Erro: Nenhum argumento válido para print")

    def visitWhileStmt(self, ctx):
        start_label = self.new_label()  # Rótulo para início do loop
        end_label = self.new_label()  # Rótulo para sair do loop

        # Marca o início do loop
        self.tac_instructions.append(f"{start_label}:")

        # Avaliação da condição
        condition_temp = self.visit(ctx.expression())
        self.tac_instructions.append(f"if {condition_temp} goto {end_label}")

        # Corpo do loop
        for stmt in ctx.block().stmt():
            # Verifica se o nó contém o token BREAK
            if stmt.getChildCount() > 0 and stmt.getChild(0).getText() == "break":
                self.tac_instructions.append(f"goto {end_label}")  # Adiciona break para sair do loop
            else:
                self.visit(stmt)

        # Retorno ao início do loop
        self.tac_instructions.append(f"goto {start_label}")

        # Rótulo de saída do loop
        self.tac_instructions.append(f"{end_label}:")

    def visitInputStmt(self, ctx):
        # Itera sobre todas as variáveis na entrada
        for var in ctx.IDENTIFIER():
            var_name = var.getText()
            self.tac_instructions.append(f"input {var_name}")
    def generate_TAC(self, tree):
        """ Gera código de três endereços visitando a árvore sintática """
        self.visit(tree)
        return self.tac_instructions
