from LPMSVisitor import LPMSVisitor
from LPMSParser import LPMSParser

class TACGenerator(LPMSVisitor):
    def __init__(self):
        self.temp_count = 0  # Contador de variáveis temporárias
        self.tac_instructions = []  # Lista de instruções TAC

    def new_temp(self):
        """ Cria uma nova variável temporária """
        self.temp_count += 1
        return f"t{self.temp_count}"

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

    def visitDeclaration(self, ctx: LPMSParser.DeclarationContext):
        var_type = ctx.getChild(0).getText()  # Obtém o tipo da variável (int, float, etc.)
        var_list = ctx.IDENTIFIER()
        assign_index = ctx.getChildCount() - 3  # Verifica se há atribuição

        for var in var_list:
            var_name = var.getText()

            # Caso a variável seja declarada com uma atribuição
            if "=" in ctx.getText():
                for i in range(1, ctx.getChildCount()):
                    if ctx.getChild(i).getText() == "=":
                        assigned_expr = ctx.getChild(i + 1)
                        if assigned_expr:
                            assigned_temp = self.visit(assigned_expr)
                            self.emit(var_name, assigned_temp)
            else:
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

    def generate_TAC(self, tree):
        """ Gera código de três endereços visitando a árvore sintática """
        self.visit(tree)
        return self.tac_instructions
