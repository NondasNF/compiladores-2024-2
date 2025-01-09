from LPMSVisitor import LPMSVisitor
from LPMSParser import LPMSParser
from collections import defaultdict


class SemanticAnalyzer(LPMSVisitor):
    def __init__(self):
        self.symbol_table = defaultdict(dict)  # Tabela de símbolos para cada escopo
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
        for scope in reversed(self.scopes):
            if var_name in self.symbol_table[scope]:
                return self.symbol_table[scope][var_name]
        return None

    def visitDeclaration(self, ctx: LPMSParser.DeclarationContext):
        var_type = ctx.children[0].getText()
        for var in ctx.children[1:]:
            if var.getText() not in [',', ';', '=', None]:
                var_name = var.getText()
                if var_name in self.symbol_table[self.current_scope()]:
                    self.errors.append(
                        f"Erro: A variável '{var_name}' já foi declarada no escopo '{self.current_scope()}'."
                    )
                else:
                    self.symbol_table[self.current_scope()][var_name] = var_type

    def visitFunctionDecl(self, ctx: LPMSParser.FunctionDeclContext):
        func_name = ctx.IDENTIFIER().getText()
        return_type = ctx.children[0].getText()

        if func_name in self.symbol_table["global"]:
            self.errors.append(f"Erro: A função '{func_name}' já foi declarada no escopo global.")
            return

        self.symbol_table["global"][func_name] = {"type": "function", "return_type": return_type}

        self.enter_scope(func_name)

        parameters = ctx.parameters().parameter()
        for param in parameters:
            param_type = param.children[0].getText()
            param_name = param.children[1].getText()
            if param_name in self.symbol_table[self.current_scope()]:
                self.errors.append(
                    f"Erro: O parâmetro '{param_name}' já foi declarado na função '{func_name}'."
                )
            else:
                self.symbol_table[self.current_scope()][param_name] = param_type

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
                self.errors.append(
                    f"Erro: A variável '{var_name}' não foi declarada no escopo atual ou global."
                )

    def visitFunctionCall(self, ctx: LPMSParser.FunctionCallContext):
        func_name = ctx.IDENTIFIER().getText()
        func_info = self.symbol_table["global"].get(func_name)
        if not func_info or func_info.get("type") != "function":
            self.errors.append(f"Erro: A função '{func_name}' não foi declarada.")
            return "undefined"

        args = ctx.arguments().expression()
        if len(args) != len(func_info.get("parameters", [])):
            self.errors.append(
                f"Erro: A função '{func_name}' espera {len(func_info['parameters'])} argumentos, "
                f"mas {len(args)} foram fornecidos."
            )

        return func_info["return_type"]

    def visitReturnStmt(self, ctx: LPMSParser.ReturnStmtContext):
        self.visit(ctx.expression())

    def get_errors(self):
        return self.errors