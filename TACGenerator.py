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
        assigned_expr = ctx.expression()

        assigned_value = self.visit(assigned_expr)
        if assigned_value is None:
            assigned_value = assigned_expr.getText()  # Obtém o valor bruto

        self.emit(var_name, assigned_value)

    def visitExpression(self, ctx: LPMSParser.ExpressionContext):
        """ Gera código para expressão aritmética ou valores literais corretamente """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term(0))

        op1 = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            operator = ctx.getChild(2 * i - 1).getText()
            op2 = self.visit(ctx.term(i))

            if op1 is None or op2 is None:
                return None

            temp_var = self.new_temp()
            self.emit(temp_var, op1, operator, op2)
            op1 = temp_var

        return op1

    def visitFactor(self, ctx: LPMSParser.FactorContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()  # Retorna o valor da string com aspas
        elif ctx.LPAREN():
            return self.visit(ctx.expression())  # Resolvendo expressões entre parênteses
        return None

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
        var_type = ctx.getChild(0).getText()  # Obtém o tipo da variável (ex: int, str, float)
        var_list = ctx.IDENTIFIER()

        for i, var in enumerate(var_list):
            var_name = var.getText()

            if var_type == "int" or var_type == "float":
                default_value = "0"
            elif var_type == "str":
                default_value = '""'
            elif var_type == "bool":
                default_value = "false"
            else:
                default_value = "0"

            ctx_var_index = 0
            for index_c, child in enumerate(ctx.children):
                if child.getText() == var_name:
                    ctx_var_index = index_c
                    break
            if ctx_var_index < ctx.getChildCount() and ctx.getChild(ctx_var_index + 1).getText() == "=":
                assigned_expr = ctx.getChild(ctx_var_index + 2)

                # Utiliza a função para encontrar o valor correto
                terminal_node = self.find_terminal_node(assigned_expr)
                if terminal_node and terminal_node.getSymbol().type == LPMSParser.STRING_LITERAL:
                    assigned_value = terminal_node.getText()
                else:
                    assigned_value = self.visit(assigned_expr)

                self.emit(var_name, assigned_value)
            else:
                self.emit(var_name, default_value)

    def visitFactor(self, ctx: LPMSParser.FactorContext):
        """ Trata fatores, incluindo identificadores, números e strings """
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()  # Retorna o valor da string com aspas
        elif ctx.LPAREN():
            return self.visit(ctx.expression())  # Resolvendo expressões entre parênteses
        return None

    def visitPrintStmt(self, ctx):
        args = ctx.expression()

        if not args or len(args) == 0:
            self.tac_instructions.append("Erro: Nenhum argumento válido para print")
            return

        arg_count = 0

        for arg in args:
            # Encontrar o nó terminal correto (STRING_LITERAL)
            terminal_node = self.find_terminal_node(arg)

            if terminal_node and terminal_node.getSymbol().type == LPMSParser.STRING_LITERAL:
                arg_value = terminal_node.getText()  # Obtém o valor da string
                self.tac_instructions.append(f'param {arg_value}')
            else:
                # Trata os outros argumentos normalmente (variáveis ou expressões)
                result = self.visit(arg)
                if result:
                    self.tac_instructions.append(f'param {result}')
                else:
                    self.tac_instructions.append("Erro: Argumento inválido para print")

            arg_count += 1

        # Adiciona chamada para a função print com o número correto de argumentos
        self.tac_instructions.append(f"call print {arg_count}")

    def find_terminal_node(self, ctx):
        """ Percorre recursivamente a árvore até encontrar um nó terminal """
        if isinstance(ctx, TerminalNode):
            return ctx
        for i in range(ctx.getChildCount()):
            result = self.find_terminal_node(ctx.getChild(i))
            if result:
                return result
        return None

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
            if stmt.getChildCount() > 0 and stmt.getChild(0).getText() == "break":
                self.tac_instructions.append(f"goto {end_label}")
            else:
                self.visit(stmt)

        # Retorno ao início do loop
        self.tac_instructions.append(f"goto {start_label}")

        # Rótulo de saída do loop
        self.tac_instructions.append(f"{end_label}:")

    def visitInputStmt(self, ctx):
        variables = ctx.IDENTIFIER()

        if not variables or len(variables) == 0:
            self.tac_instructions.append("Erro: Nenhuma variável válida para input")
            return

        arg_count = 0
        for var in variables:
            var_name = var.getText()
            self.tac_instructions.append(f"param {var_name}")
            arg_count += 1

        # Gera chamada para a função input com o número de variáveis passadas
        self.tac_instructions.append(f"call input {arg_count}")

    def generate_TAC(self, tree):
        """ Gera código de três endereços visitando a árvore sintática """
        self.visit(tree)
        return self.tac_instructions
