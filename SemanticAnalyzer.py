from LPMSVisitor import LPMSVisitor
from LPMSParser import LPMSParser
from collections import defaultdict


class SemanticAnalyzer(LPMSVisitor):
    def __init__(self):
        self.symbol_table = defaultdict(dict)  # Tabela de símbolos por escopo
        self.scopes = ["global"]  # Pilha de escopos
        self.errors = []

    def current_scope(self):
        return self.scopes[-1]

    def enter_scope(self, scope_name):
        self.scopes.append(scope_name)
        if scope_name not in self.symbol_table:
            self.symbol_table[scope_name] = {}

    def exit_scope(self):
        self.scopes.pop()

    def lookup_variable(self, var_name):
        """ Procura a variável nos escopos da pilha, do mais interno ao global """
        for scope in reversed(self.scopes):
            if var_name in self.symbol_table[scope]:
                return self.symbol_table[scope][var_name]
        return None



    def visitFunctionDecl(self, ctx: LPMSParser.FunctionDeclContext):
        """ Declara uma função na tabela de símbolos e define um novo escopo para ela. """
        func_name = ctx.IDENTIFIER().getText()
        return_type = ctx.children[0].getText()

        if func_name in self.symbol_table["global"]:
            self.errors.append(f"Erro: A função '{func_name}' já foi declarada no escopo global.")
            return

        # Registra a função no escopo global
        self.symbol_table["global"][func_name] = {"type": "function", "return_type": return_type, "parameters": []}

        self.enter_scope(func_name)

        parameters = ctx.parameters().parameter()
        for param in parameters:
            param_type = param.children[0].getText()
            param_name = param.children[1].getText()

            if param_name in self.symbol_table[self.current_scope()]:
                self.errors.append(f"Erro: O parâmetro '{param_name}' já foi declarado na função '{func_name}'.")
            else:
                self.symbol_table[self.current_scope()][param_name] = {"type": param_type}
                self.symbol_table["global"][func_name]["parameters"].append(param_type)

        self.visit(ctx.block())
        self.exit_scope()

    def visitExpression(self, ctx: LPMSParser.ExpressionContext):
        terms = ctx.term()
        for term in terms:
            self.visit(term)

    def visitTerm(self, ctx: LPMSParser.TermContext):
        factors = ctx.factor()
        for factor in factors:
            self.visit(factor)

    def visitFactor(self, ctx: LPMSParser.FactorContext):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if not self.lookup_variable(var_name):
                self.errors.append(f"Erro: A variável '{var_name}' não foi declarada no escopo atual ou global.")

    def visitFunctionCall(self, ctx: LPMSParser.FunctionCallContext):
        """ Verifica se a função chamada foi declarada corretamente e valida os argumentos. """
        func_name = ctx.IDENTIFIER().getText()
        func_info = self.symbol_table["global"].get(func_name)

        if not func_info or func_info.get("type") != "function":
            self.errors.append(f"Erro: A função '{func_name}' não foi declarada.")
            return "undefined"

        args = ctx.arguments().expression()
        expected_params = func_info.get("parameters", [])

        if len(args) != len(expected_params):
            self.errors.append(
                f"Erro: A função '{func_name}' espera {len(expected_params)} argumentos, "
                f"mas {len(args)} foram fornecidos."
            )

        return func_info["return_type"]

    def visitConstDeclaration(self, ctx: LPMSParser.ConstDeclarationContext):
        """ Registra constantes na tabela de símbolos e verifica seu tipo inicial. """
        const_name = ctx.IDENTIFIER().getText()
        assigned_expression = ctx.expression()

        # Verifica se a constante já foi declarada no escopo atual
        if const_name in self.symbol_table[self.current_scope()]:
            self.errors.append(
                f"Erro semântico: Constante '{const_name}' já foi declarada no escopo '{self.current_scope()}'.")
            return

        # Determina o tipo da expressão atribuída
        const_type = self.determine_expression_type(assigned_expression)

        # Registra a constante na tabela de símbolos com uma flag indicando que é uma constante
        self.symbol_table[self.current_scope()][const_name] = {"type": const_type, "is_const": True}

    def visitDeclaration(self, ctx):
        """ Registra variáveis na tabela de símbolos e verifica o tipo inicial (se houver). """
        var_type = ctx.getChild(0).getText()  # Tipo da variável (ex: "int")

        for i in range(1, ctx.getChildCount(), 2):
            var_name = ctx.getChild(i).getText()

            # Verifica se a variável já foi declarada no escopo atual
            if var_name in self.symbol_table[self.current_scope()]:
                self.errors.append(f"Erro semântico: Variável '{var_name}' já foi declarada neste escopo.")
                continue

            # Verifica se há uma atribuição inicial (ex: int x = ...)
            if i + 1 < ctx.getChildCount() and ctx.getChild(i + 1).getText() == "=":
                # Obtém a expressão atribuída
                assigned_expression = ctx.getChild(i + 2)
                assigned_type = self.determine_expression_type(assigned_expression)

                # Valida se o tipo atribuído é compatível com o tipo declarado
                if var_type != assigned_type:
                    self.errors.append(
                        f"Erro semântico: Não é possível atribuir um valor de tipo '{assigned_type}' "
                        f"à variável '{var_name}' do tipo '{var_type}'."
                    )

            # Registra a variável na tabela de símbolos
            self.symbol_table[self.current_scope()][var_name] = {"type": var_type}

    def determine_expression_type(self, expression_ctx):
        """ Determina o tipo de uma expressão baseado na AST """
        if expression_ctx.term():
            return self.determine_term_type(expression_ctx.term(0))
        return "undefined"

    def determine_term_type(self, term_ctx):
        """ Determina o tipo de um termo """
        if term_ctx.factor():
            return self.determine_factor_type(term_ctx.factor(0))
        return "undefined"

    def visitAssignment(self, ctx):
        """ Verifica se a atribuição é válida """
        var_name = ctx.IDENTIFIER().getText()
        assigned_expression = ctx.expression()

        # Verifica se a variável foi declarada
        var_info = self.lookup_variable(var_name)
        if not var_info:
            self.errors.append(f"Erro semântico: Variável '{var_name}' não foi declarada antes da atribuição.")
            return

        var_type = var_info["type"]
        is_const = var_info.get("is_const", False)

        # Impede alterações em constantes
        if is_const:
            self.errors.append(f"Erro semântico: Não é possível alterar o valor da constante '{var_name}'.")
            return

        # Determina o tipo da expressão atribuída
        assigned_type = self.determine_expression_type(assigned_expression)

        # Valida se os tipos são compatíveis
        if var_type != assigned_type:
            self.errors.append(
                f"Erro semântico: Não é possível atribuir um valor de tipo '{assigned_type}' "
                f"à variável '{var_name}' do tipo '{var_type}'."
            )

    def determine_factor_type(self, factor_ctx):
        """ Determina o tipo de um fator """
        if factor_ctx.STRING_LITERAL():
            return "str"
        elif factor_ctx.NUMBER():
            return "int" if '.' not in factor_ctx.getText() else "float"
        elif factor_ctx.IDENTIFIER():
            var_name = factor_ctx.IDENTIFIER().getText()
            var_info = self.lookup_variable(var_name)
            if var_info:
                return var_info["type"]
            else:
                self.errors.append(f"Erro: A variável '{var_name}' não foi declarada.")
                return "undefined"
        elif factor_ctx.TRUE() or factor_ctx.FALSE():
            return "bool"
        return "undefined"

    def visitReturnStmt(self, ctx: LPMSParser.ReturnStmtContext):
        self.visit(ctx.expression())

    def get_errors(self):
        return self.errors
