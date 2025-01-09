# Generated from C:/Users/nonda/Downloads/TrabalhoCompiladorCompleto/Compiladores-2024-2/LPMS.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,223,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,3,1,3,1,3,1,3,
        3,3,72,8,3,1,3,1,3,1,3,1,3,3,3,78,8,3,5,3,80,8,3,10,3,12,3,83,9,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,136,8,8,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,150,8,10,1,10,1,10,1,10,1,
        10,3,10,156,8,10,1,10,1,10,1,11,1,11,1,11,5,11,163,8,11,10,11,12,
        11,166,9,11,1,12,1,12,1,12,1,13,1,13,1,13,3,13,174,8,13,1,13,1,13,
        1,14,1,14,1,14,5,14,181,8,14,10,14,12,14,184,9,14,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,5,16,193,8,16,10,16,12,16,196,9,16,1,17,1,17,
        1,17,5,17,201,8,17,10,17,12,17,204,9,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,221,8,18,
        1,18,0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        0,3,1,0,8,11,2,0,16,17,20,25,1,0,18,19,236,0,38,1,0,0,0,2,48,1,0,
        0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,86,1,0,0,0,10,92,1,0,0,0,12,97,1,
        0,0,0,14,110,1,0,0,0,16,123,1,0,0,0,18,137,1,0,0,0,20,145,1,0,0,
        0,22,159,1,0,0,0,24,167,1,0,0,0,26,170,1,0,0,0,28,177,1,0,0,0,30,
        185,1,0,0,0,32,189,1,0,0,0,34,197,1,0,0,0,36,220,1,0,0,0,38,39,5,
        1,0,0,39,40,5,34,0,0,40,41,5,30,0,0,41,42,3,2,1,0,42,43,5,31,0,0,
        43,44,5,0,0,1,44,1,1,0,0,0,45,47,3,4,2,0,46,45,1,0,0,0,47,50,1,0,
        0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,3,1,0,0,0,50,48,1,0,0,0,51,66,
        3,6,3,0,52,66,3,8,4,0,53,66,3,10,5,0,54,66,3,12,6,0,55,66,3,14,7,
        0,56,66,3,16,8,0,57,66,3,18,9,0,58,66,3,20,10,0,59,60,3,26,13,0,
        60,61,5,33,0,0,61,66,1,0,0,0,62,66,3,30,15,0,63,64,5,15,0,0,64,66,
        5,33,0,0,65,51,1,0,0,0,65,52,1,0,0,0,65,53,1,0,0,0,65,54,1,0,0,0,
        65,55,1,0,0,0,65,56,1,0,0,0,65,57,1,0,0,0,65,58,1,0,0,0,65,59,1,
        0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,66,5,1,0,0,0,67,68,7,0,0,0,68,
        71,5,34,0,0,69,70,5,27,0,0,70,72,3,32,16,0,71,69,1,0,0,0,71,72,1,
        0,0,0,72,81,1,0,0,0,73,74,5,32,0,0,74,77,5,34,0,0,75,76,5,27,0,0,
        76,78,3,32,16,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,73,
        1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,
        83,81,1,0,0,0,84,85,5,33,0,0,85,7,1,0,0,0,86,87,5,7,0,0,87,88,5,
        34,0,0,88,89,5,27,0,0,89,90,3,32,16,0,90,91,5,33,0,0,91,9,1,0,0,
        0,92,93,5,34,0,0,93,94,5,27,0,0,94,95,3,32,16,0,95,96,5,33,0,0,96,
        11,1,0,0,0,97,98,5,6,0,0,98,99,5,28,0,0,99,104,5,34,0,0,100,101,
        5,32,0,0,101,103,5,34,0,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,
        1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,108,
        5,29,0,0,108,109,5,33,0,0,109,13,1,0,0,0,110,111,5,5,0,0,111,112,
        5,28,0,0,112,117,3,32,16,0,113,114,5,32,0,0,114,116,3,32,16,0,115,
        113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,
        120,1,0,0,0,119,117,1,0,0,0,120,121,5,29,0,0,121,122,5,33,0,0,122,
        15,1,0,0,0,123,124,5,2,0,0,124,125,5,28,0,0,125,126,3,32,16,0,126,
        127,5,29,0,0,127,128,5,30,0,0,128,129,3,2,1,0,129,135,5,31,0,0,130,
        131,5,3,0,0,131,132,5,30,0,0,132,133,3,2,1,0,133,134,5,31,0,0,134,
        136,1,0,0,0,135,130,1,0,0,0,135,136,1,0,0,0,136,17,1,0,0,0,137,138,
        5,4,0,0,138,139,5,28,0,0,139,140,3,32,16,0,140,141,5,29,0,0,141,
        142,5,30,0,0,142,143,3,2,1,0,143,144,5,31,0,0,144,19,1,0,0,0,145,
        146,7,0,0,0,146,147,5,34,0,0,147,149,5,28,0,0,148,150,3,22,11,0,
        149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,5,29,0,0,
        152,153,5,30,0,0,153,155,3,2,1,0,154,156,3,30,15,0,155,154,1,0,0,
        0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,31,0,0,158,21,1,0,0,
        0,159,164,3,24,12,0,160,161,5,32,0,0,161,163,3,24,12,0,162,160,1,
        0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,23,1,0,
        0,0,166,164,1,0,0,0,167,168,7,0,0,0,168,169,5,34,0,0,169,25,1,0,
        0,0,170,171,5,34,0,0,171,173,5,28,0,0,172,174,3,28,14,0,173,172,
        1,0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,176,5,29,0,0,176,27,
        1,0,0,0,177,182,3,32,16,0,178,179,5,32,0,0,179,181,3,32,16,0,180,
        178,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,
        29,1,0,0,0,184,182,1,0,0,0,185,186,5,12,0,0,186,187,3,32,16,0,187,
        188,5,33,0,0,188,31,1,0,0,0,189,194,3,34,17,0,190,191,7,1,0,0,191,
        193,3,34,17,0,192,190,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,
        195,1,0,0,0,195,33,1,0,0,0,196,194,1,0,0,0,197,202,3,36,18,0,198,
        199,7,2,0,0,199,201,3,36,18,0,200,198,1,0,0,0,201,204,1,0,0,0,202,
        200,1,0,0,0,202,203,1,0,0,0,203,35,1,0,0,0,204,202,1,0,0,0,205,221,
        5,34,0,0,206,221,3,26,13,0,207,221,5,35,0,0,208,221,5,36,0,0,209,
        221,5,37,0,0,210,221,5,13,0,0,211,221,5,14,0,0,212,213,5,28,0,0,
        213,214,3,32,16,0,214,215,5,29,0,0,215,221,1,0,0,0,216,217,5,26,
        0,0,217,221,3,36,18,0,218,219,5,17,0,0,219,221,3,36,18,0,220,205,
        1,0,0,0,220,206,1,0,0,0,220,207,1,0,0,0,220,208,1,0,0,0,220,209,
        1,0,0,0,220,210,1,0,0,0,220,211,1,0,0,0,220,212,1,0,0,0,220,216,
        1,0,0,0,220,218,1,0,0,0,221,37,1,0,0,0,16,48,65,71,77,81,104,117,
        135,149,155,164,173,182,194,202,220
    ]

class LPMSParser ( Parser ):

    grammarFileName = "LPMS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'if'", "'else'", "'while'", 
                     "'print'", "'input'", "'const'", "'int'", "'float'", 
                     "'bool'", "'str'", "'return'", "'true'", "'false'", 
                     "'break'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'>='", "'<='", "'>'", "'<'", "'!'", "'='", "'('", 
                     "')'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "IF", "ELSE", "WHILE", "PRINT", 
                      "INPUT", "CONST", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "CHAR_TYPE", "RETURN", "TRUE", "FALSE", "BREAK", "ADD", 
                      "SUB", "MUL", "DIV", "EQ", "NEQ", "GE", "LE", "GT", 
                      "LT", "NOT", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "COMMA", "SEMICOLON", "IDENTIFIER", "NUMBER", 
                      "CHAR_LITERAL", "STRING_LITERAL", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_block = 1
    RULE_stmt = 2
    RULE_declaration = 3
    RULE_constDeclaration = 4
    RULE_assignment = 5
    RULE_inputStmt = 6
    RULE_printStmt = 7
    RULE_ifStmt = 8
    RULE_whileStmt = 9
    RULE_functionDecl = 10
    RULE_parameters = 11
    RULE_parameter = 12
    RULE_functionCall = 13
    RULE_arguments = 14
    RULE_returnStmt = 15
    RULE_expression = 16
    RULE_term = 17
    RULE_factor = 18

    ruleNames =  [ "program", "block", "stmt", "declaration", "constDeclaration", 
                   "assignment", "inputStmt", "printStmt", "ifStmt", "whileStmt", 
                   "functionDecl", "parameters", "parameter", "functionCall", 
                   "arguments", "returnStmt", "expression", "term", "factor" ]

    EOF = Token.EOF
    PROGRAM=1
    IF=2
    ELSE=3
    WHILE=4
    PRINT=5
    INPUT=6
    CONST=7
    INT_TYPE=8
    FLOAT_TYPE=9
    BOOL_TYPE=10
    CHAR_TYPE=11
    RETURN=12
    TRUE=13
    FALSE=14
    BREAK=15
    ADD=16
    SUB=17
    MUL=18
    DIV=19
    EQ=20
    NEQ=21
    GE=22
    LE=23
    GT=24
    LT=25
    NOT=26
    ASSIGN=27
    LPAREN=28
    RPAREN=29
    LBRACE=30
    RBRACE=31
    COMMA=32
    SEMICOLON=33
    IDENTIFIER=34
    NUMBER=35
    CHAR_LITERAL=36
    STRING_LITERAL=37
    WS=38
    COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(LPMSParser.PROGRAM, 0)

        def IDENTIFIER(self):
            return self.getToken(LPMSParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LPMSParser.LBRACE, 0)

        def block(self):
            return self.getTypedRuleContext(LPMSParser.BlockContext,0)


        def RBRACE(self):
            return self.getToken(LPMSParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(LPMSParser.EOF, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LPMSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(LPMSParser.PROGRAM)
            self.state = 39
            self.match(LPMSParser.IDENTIFIER)
            self.state = 40
            self.match(LPMSParser.LBRACE)
            self.state = 41
            self.block()
            self.state = 42
            self.match(LPMSParser.RBRACE)
            self.state = 43
            self.match(LPMSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.StmtContext)
            else:
                return self.getTypedRuleContext(LPMSParser.StmtContext,i)


        def getRuleIndex(self):
            return LPMSParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LPMSParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 45
                    self.stmt() 
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(LPMSParser.DeclarationContext,0)


        def constDeclaration(self):
            return self.getTypedRuleContext(LPMSParser.ConstDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(LPMSParser.AssignmentContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(LPMSParser.InputStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(LPMSParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(LPMSParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(LPMSParser.WhileStmtContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(LPMSParser.FunctionDeclContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(LPMSParser.FunctionCallContext,0)


        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def returnStmt(self):
            return self.getTypedRuleContext(LPMSParser.ReturnStmtContext,0)


        def BREAK(self):
            return self.getToken(LPMSParser.BREAK, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = LPMSParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.constDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.inputStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.printStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.ifStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.whileStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.functionDecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.functionCall()
                self.state = 60
                self.match(LPMSParser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 62
                self.returnStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 63
                self.match(LPMSParser.BREAK)
                self.state = 64
                self.match(LPMSParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.IDENTIFIER)
            else:
                return self.getToken(LPMSParser.IDENTIFIER, i)

        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def INT_TYPE(self):
            return self.getToken(LPMSParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(LPMSParser.FLOAT_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(LPMSParser.BOOL_TYPE, 0)

        def CHAR_TYPE(self):
            return self.getToken(LPMSParser.CHAR_TYPE, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.ASSIGN)
            else:
                return self.getToken(LPMSParser.ASSIGN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LPMSParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.COMMA)
            else:
                return self.getToken(LPMSParser.COMMA, i)

        def getRuleIndex(self):
            return LPMSParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = LPMSParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 68
            self.match(LPMSParser.IDENTIFIER)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 69
                self.match(LPMSParser.ASSIGN)
                self.state = 70
                self.expression()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 73
                self.match(LPMSParser.COMMA)
                self.state = 74
                self.match(LPMSParser.IDENTIFIER)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 75
                    self.match(LPMSParser.ASSIGN)
                    self.state = 76
                    self.expression()


                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(LPMSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(LPMSParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(LPMSParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(LPMSParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(LPMSParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_constDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDeclaration" ):
                listener.enterConstDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDeclaration" ):
                listener.exitConstDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDeclaration" ):
                return visitor.visitConstDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constDeclaration(self):

        localctx = LPMSParser.ConstDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(LPMSParser.CONST)
            self.state = 87
            self.match(LPMSParser.IDENTIFIER)
            self.state = 88
            self.match(LPMSParser.ASSIGN)
            self.state = 89
            self.expression()
            self.state = 90
            self.match(LPMSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LPMSParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(LPMSParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(LPMSParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LPMSParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(LPMSParser.IDENTIFIER)
            self.state = 93
            self.match(LPMSParser.ASSIGN)
            self.state = 94
            self.expression()
            self.state = 95
            self.match(LPMSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(LPMSParser.INPUT, 0)

        def LPAREN(self):
            return self.getToken(LPMSParser.LPAREN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.IDENTIFIER)
            else:
                return self.getToken(LPMSParser.IDENTIFIER, i)

        def RPAREN(self):
            return self.getToken(LPMSParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.COMMA)
            else:
                return self.getToken(LPMSParser.COMMA, i)

        def getRuleIndex(self):
            return LPMSParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)




    def inputStmt(self):

        localctx = LPMSParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_inputStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(LPMSParser.INPUT)
            self.state = 98
            self.match(LPMSParser.LPAREN)
            self.state = 99
            self.match(LPMSParser.IDENTIFIER)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 100
                self.match(LPMSParser.COMMA)
                self.state = 101
                self.match(LPMSParser.IDENTIFIER)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(LPMSParser.RPAREN)
            self.state = 108
            self.match(LPMSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(LPMSParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(LPMSParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LPMSParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(LPMSParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.COMMA)
            else:
                return self.getToken(LPMSParser.COMMA, i)

        def getRuleIndex(self):
            return LPMSParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = LPMSParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(LPMSParser.PRINT)
            self.state = 111
            self.match(LPMSParser.LPAREN)
            self.state = 112
            self.expression()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 113
                self.match(LPMSParser.COMMA)
                self.state = 114
                self.expression()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(LPMSParser.RPAREN)
            self.state = 121
            self.match(LPMSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LPMSParser.IF, 0)

        def LPAREN(self):
            return self.getToken(LPMSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LPMSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LPMSParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.LBRACE)
            else:
                return self.getToken(LPMSParser.LBRACE, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.BlockContext)
            else:
                return self.getTypedRuleContext(LPMSParser.BlockContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.RBRACE)
            else:
                return self.getToken(LPMSParser.RBRACE, i)

        def ELSE(self):
            return self.getToken(LPMSParser.ELSE, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = LPMSParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(LPMSParser.IF)
            self.state = 124
            self.match(LPMSParser.LPAREN)
            self.state = 125
            self.expression()
            self.state = 126
            self.match(LPMSParser.RPAREN)
            self.state = 127
            self.match(LPMSParser.LBRACE)
            self.state = 128
            self.block()
            self.state = 129
            self.match(LPMSParser.RBRACE)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 130
                self.match(LPMSParser.ELSE)
                self.state = 131
                self.match(LPMSParser.LBRACE)
                self.state = 132
                self.block()
                self.state = 133
                self.match(LPMSParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LPMSParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(LPMSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LPMSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LPMSParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(LPMSParser.LBRACE, 0)

        def block(self):
            return self.getTypedRuleContext(LPMSParser.BlockContext,0)


        def RBRACE(self):
            return self.getToken(LPMSParser.RBRACE, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = LPMSParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(LPMSParser.WHILE)
            self.state = 138
            self.match(LPMSParser.LPAREN)
            self.state = 139
            self.expression()
            self.state = 140
            self.match(LPMSParser.RPAREN)
            self.state = 141
            self.match(LPMSParser.LBRACE)
            self.state = 142
            self.block()
            self.state = 143
            self.match(LPMSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LPMSParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(LPMSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LPMSParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(LPMSParser.LBRACE, 0)

        def block(self):
            return self.getTypedRuleContext(LPMSParser.BlockContext,0)


        def RBRACE(self):
            return self.getToken(LPMSParser.RBRACE, 0)

        def INT_TYPE(self):
            return self.getToken(LPMSParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(LPMSParser.FLOAT_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(LPMSParser.BOOL_TYPE, 0)

        def CHAR_TYPE(self):
            return self.getToken(LPMSParser.CHAR_TYPE, 0)

        def parameters(self):
            return self.getTypedRuleContext(LPMSParser.ParametersContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(LPMSParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return LPMSParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = LPMSParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            self.match(LPMSParser.IDENTIFIER)
            self.state = 147
            self.match(LPMSParser.LPAREN)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0):
                self.state = 148
                self.parameters()


            self.state = 151
            self.match(LPMSParser.RPAREN)
            self.state = 152
            self.match(LPMSParser.LBRACE)
            self.state = 153
            self.block()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 154
                self.returnStmt()


            self.state = 157
            self.match(LPMSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.ParameterContext)
            else:
                return self.getTypedRuleContext(LPMSParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.COMMA)
            else:
                return self.getToken(LPMSParser.COMMA, i)

        def getRuleIndex(self):
            return LPMSParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = LPMSParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.parameter()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 160
                self.match(LPMSParser.COMMA)
                self.state = 161
                self.parameter()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LPMSParser.IDENTIFIER, 0)

        def INT_TYPE(self):
            return self.getToken(LPMSParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(LPMSParser.FLOAT_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(LPMSParser.BOOL_TYPE, 0)

        def CHAR_TYPE(self):
            return self.getToken(LPMSParser.CHAR_TYPE, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = LPMSParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 168
            self.match(LPMSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LPMSParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(LPMSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LPMSParser.RPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(LPMSParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return LPMSParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = LPMSParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(LPMSParser.IDENTIFIER)
            self.state = 171
            self.match(LPMSParser.LPAREN)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 258033737728) != 0):
                self.state = 172
                self.arguments()


            self.state = 175
            self.match(LPMSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LPMSParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.COMMA)
            else:
                return self.getToken(LPMSParser.COMMA, i)

        def getRuleIndex(self):
            return LPMSParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = LPMSParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.expression()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 178
                self.match(LPMSParser.COMMA)
                self.state = 179
                self.expression()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LPMSParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(LPMSParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = LPMSParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(LPMSParser.RETURN)
            self.state = 186
            self.expression()
            self.state = 187
            self.match(LPMSParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.TermContext)
            else:
                return self.getTypedRuleContext(LPMSParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.ADD)
            else:
                return self.getToken(LPMSParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.SUB)
            else:
                return self.getToken(LPMSParser.SUB, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.GT)
            else:
                return self.getToken(LPMSParser.GT, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.LT)
            else:
                return self.getToken(LPMSParser.LT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.GE)
            else:
                return self.getToken(LPMSParser.GE, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.LE)
            else:
                return self.getToken(LPMSParser.LE, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.EQ)
            else:
                return self.getToken(LPMSParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.NEQ)
            else:
                return self.getToken(LPMSParser.NEQ, i)

        def getRuleIndex(self):
            return LPMSParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = LPMSParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.term()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66256896) != 0):
                self.state = 190
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66256896) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.term()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.FactorContext)
            else:
                return self.getTypedRuleContext(LPMSParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.MUL)
            else:
                return self.getToken(LPMSParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.DIV)
            else:
                return self.getToken(LPMSParser.DIV, i)

        def getRuleIndex(self):
            return LPMSParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LPMSParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.factor()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 198
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.factor()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LPMSParser.IDENTIFIER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(LPMSParser.FunctionCallContext,0)


        def NUMBER(self):
            return self.getToken(LPMSParser.NUMBER, 0)

        def CHAR_LITERAL(self):
            return self.getToken(LPMSParser.CHAR_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(LPMSParser.STRING_LITERAL, 0)

        def TRUE(self):
            return self.getToken(LPMSParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LPMSParser.FALSE, 0)

        def LPAREN(self):
            return self.getToken(LPMSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LPMSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LPMSParser.RPAREN, 0)

        def NOT(self):
            return self.getToken(LPMSParser.NOT, 0)

        def factor(self):
            return self.getTypedRuleContext(LPMSParser.FactorContext,0)


        def SUB(self):
            return self.getToken(LPMSParser.SUB, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = LPMSParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_factor)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(LPMSParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(LPMSParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.match(LPMSParser.CHAR_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.match(LPMSParser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 210
                self.match(LPMSParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 211
                self.match(LPMSParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 212
                self.match(LPMSParser.LPAREN)
                self.state = 213
                self.expression()
                self.state = 214
                self.match(LPMSParser.RPAREN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 216
                self.match(LPMSParser.NOT)
                self.state = 217
                self.factor()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 218
                self.match(LPMSParser.SUB)
                self.state = 219
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





