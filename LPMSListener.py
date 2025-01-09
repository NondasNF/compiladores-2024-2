# Generated from C:/Users/nonda/Downloads/TrabalhoCompiladorCompleto/Compiladores-2024-2/LPMS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LPMSParser import LPMSParser
else:
    from LPMSParser import LPMSParser

# This class defines a complete listener for a parse tree produced by LPMSParser.
class LPMSListener(ParseTreeListener):

    # Enter a parse tree produced by LPMSParser#program.
    def enterProgram(self, ctx:LPMSParser.ProgramContext):
        pass

    # Exit a parse tree produced by LPMSParser#program.
    def exitProgram(self, ctx:LPMSParser.ProgramContext):
        pass


    # Enter a parse tree produced by LPMSParser#stmt.
    def enterStmt(self, ctx:LPMSParser.StmtContext):
        pass

    # Exit a parse tree produced by LPMSParser#stmt.
    def exitStmt(self, ctx:LPMSParser.StmtContext):
        pass


    # Enter a parse tree produced by LPMSParser#declaration.
    def enterDeclaration(self, ctx:LPMSParser.DeclarationContext):
        pass

    # Exit a parse tree produced by LPMSParser#declaration.
    def exitDeclaration(self, ctx:LPMSParser.DeclarationContext):
        pass


    # Enter a parse tree produced by LPMSParser#constDeclaration.
    def enterConstDeclaration(self, ctx:LPMSParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by LPMSParser#constDeclaration.
    def exitConstDeclaration(self, ctx:LPMSParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by LPMSParser#assignment.
    def enterAssignment(self, ctx:LPMSParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LPMSParser#assignment.
    def exitAssignment(self, ctx:LPMSParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LPMSParser#inputStmt.
    def enterInputStmt(self, ctx:LPMSParser.InputStmtContext):
        pass

    # Exit a parse tree produced by LPMSParser#inputStmt.
    def exitInputStmt(self, ctx:LPMSParser.InputStmtContext):
        pass


    # Enter a parse tree produced by LPMSParser#printStmt.
    def enterPrintStmt(self, ctx:LPMSParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by LPMSParser#printStmt.
    def exitPrintStmt(self, ctx:LPMSParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by LPMSParser#ifStmt.
    def enterIfStmt(self, ctx:LPMSParser.IfStmtContext):
        pass

    # Exit a parse tree produced by LPMSParser#ifStmt.
    def exitIfStmt(self, ctx:LPMSParser.IfStmtContext):
        pass


    # Enter a parse tree produced by LPMSParser#whileStmt.
    def enterWhileStmt(self, ctx:LPMSParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by LPMSParser#whileStmt.
    def exitWhileStmt(self, ctx:LPMSParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by LPMSParser#expression.
    def enterExpression(self, ctx:LPMSParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LPMSParser#expression.
    def exitExpression(self, ctx:LPMSParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LPMSParser#term.
    def enterTerm(self, ctx:LPMSParser.TermContext):
        pass

    # Exit a parse tree produced by LPMSParser#term.
    def exitTerm(self, ctx:LPMSParser.TermContext):
        pass


    # Enter a parse tree produced by LPMSParser#factor.
    def enterFactor(self, ctx:LPMSParser.FactorContext):
        pass

    # Exit a parse tree produced by LPMSParser#factor.
    def exitFactor(self, ctx:LPMSParser.FactorContext):
        pass


    # Enter a parse tree produced by LPMSParser#comparison.
    def enterComparison(self, ctx:LPMSParser.ComparisonContext):
        pass

    # Exit a parse tree produced by LPMSParser#comparison.
    def exitComparison(self, ctx:LPMSParser.ComparisonContext):
        pass



del LPMSParser