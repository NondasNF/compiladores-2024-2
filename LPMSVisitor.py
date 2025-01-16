# Generated from C:/Users/nonda/Downloads/TrabalhoCompiladorCompleto/Compiladores-2024-2/LPMS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LPMSParser import LPMSParser
else:
    from LPMSParser import LPMSParser

# This class defines a complete generic visitor for a parse tree produced by LPMSParser.

class LPMSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LPMSParser#program.
    def visitProgram(self, ctx:LPMSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#block.
    def visitBlock(self, ctx:LPMSParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#stmt.
    def visitStmt(self, ctx:LPMSParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#declaration.
    def visitDeclaration(self, ctx:LPMSParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#constDeclaration.
    def visitConstDeclaration(self, ctx:LPMSParser.ConstDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#assignment.
    def visitAssignment(self, ctx:LPMSParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#inputStmt.
    def visitInputStmt(self, ctx:LPMSParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#printStmt.
    def visitPrintStmt(self, ctx:LPMSParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#ifStmt.
    def visitIfStmt(self, ctx:LPMSParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#whileStmt.
    def visitWhileStmt(self, ctx:LPMSParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#functionDecl.
    def visitFunctionDecl(self, ctx:LPMSParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#parameters.
    def visitParameters(self, ctx:LPMSParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#parameter.
    def visitParameter(self, ctx:LPMSParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#functionCall.
    def visitFunctionCall(self, ctx:LPMSParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#arguments.
    def visitArguments(self, ctx:LPMSParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#returnStmt.
    def visitReturnStmt(self, ctx:LPMSParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#expression.
    def visitExpression(self, ctx:LPMSParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#term.
    def visitTerm(self, ctx:LPMSParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPMSParser#factor.
    def visitFactor(self, ctx:LPMSParser.FactorContext):
        return self.visitChildren(ctx)



del LPMSParser