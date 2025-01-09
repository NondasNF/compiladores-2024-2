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
        4,1,38,178,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,5,2,52,8,2,10,2,12,2,55,9,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,5,5,75,8,5,10,5,12,5,78,9,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,5,7,102,8,7,10,7,12,7,105,9,7,1,7,1,7,1,7,1,7,5,7,111,8,7,
        10,7,12,7,114,9,7,1,7,3,7,117,8,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,125,
        8,8,10,8,12,8,128,9,8,1,8,1,8,3,8,132,8,8,1,8,5,8,135,8,8,10,8,12,
        8,138,9,8,1,8,1,8,1,9,1,9,1,9,5,9,145,8,9,10,9,12,9,148,9,9,1,10,
        1,10,1,10,5,10,153,8,10,10,10,12,10,156,9,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,172,8,11,
        1,12,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
        0,4,1,0,8,11,2,0,15,16,19,24,1,0,17,18,1,0,19,24,190,0,26,1,0,0,
        0,2,45,1,0,0,0,4,47,1,0,0,0,6,58,1,0,0,0,8,64,1,0,0,0,10,69,1,0,
        0,0,12,82,1,0,0,0,14,95,1,0,0,0,16,118,1,0,0,0,18,141,1,0,0,0,20,
        149,1,0,0,0,22,171,1,0,0,0,24,173,1,0,0,0,26,27,5,1,0,0,27,28,5,
        33,0,0,28,32,5,29,0,0,29,31,3,2,1,0,30,29,1,0,0,0,31,34,1,0,0,0,
        32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,5,
        30,0,0,36,37,5,0,0,1,37,1,1,0,0,0,38,46,3,4,2,0,39,46,3,8,4,0,40,
        46,3,6,3,0,41,46,3,10,5,0,42,46,3,12,6,0,43,46,3,14,7,0,44,46,3,
        16,8,0,45,38,1,0,0,0,45,39,1,0,0,0,45,40,1,0,0,0,45,41,1,0,0,0,45,
        42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,48,7,0,0,
        0,48,53,5,33,0,0,49,50,5,31,0,0,50,52,5,33,0,0,51,49,1,0,0,0,52,
        55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,
        0,56,57,5,32,0,0,57,5,1,0,0,0,58,59,5,7,0,0,59,60,5,33,0,0,60,61,
        5,26,0,0,61,62,3,18,9,0,62,63,5,32,0,0,63,7,1,0,0,0,64,65,5,33,0,
        0,65,66,5,26,0,0,66,67,3,18,9,0,67,68,5,32,0,0,68,9,1,0,0,0,69,70,
        5,6,0,0,70,71,5,27,0,0,71,76,5,33,0,0,72,73,5,31,0,0,73,75,5,33,
        0,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,
        1,0,0,0,78,76,1,0,0,0,79,80,5,28,0,0,80,81,5,32,0,0,81,11,1,0,0,
        0,82,83,5,5,0,0,83,84,5,27,0,0,84,89,3,18,9,0,85,86,5,31,0,0,86,
        88,3,18,9,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,
        0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,28,0,0,93,94,5,32,0,0,94,
        13,1,0,0,0,95,96,5,2,0,0,96,97,5,27,0,0,97,98,3,18,9,0,98,99,5,28,
        0,0,99,103,5,29,0,0,100,102,3,2,1,0,101,100,1,0,0,0,102,105,1,0,
        0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,
        0,0,106,116,5,30,0,0,107,108,5,3,0,0,108,112,5,29,0,0,109,111,3,
        2,1,0,110,109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,
        0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,117,5,30,0,0,116,107,1,
        0,0,0,116,117,1,0,0,0,117,15,1,0,0,0,118,119,5,4,0,0,119,120,5,27,
        0,0,120,121,3,18,9,0,121,122,5,28,0,0,122,126,5,29,0,0,123,125,3,
        2,1,0,124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,
        0,0,0,127,131,1,0,0,0,128,126,1,0,0,0,129,130,5,14,0,0,130,132,5,
        32,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,136,1,0,0,0,133,135,3,
        2,1,0,134,133,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,
        0,0,0,137,139,1,0,0,0,138,136,1,0,0,0,139,140,5,30,0,0,140,17,1,
        0,0,0,141,146,3,20,10,0,142,143,7,1,0,0,143,145,3,20,10,0,144,142,
        1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,19,1,
        0,0,0,148,146,1,0,0,0,149,154,3,22,11,0,150,151,7,2,0,0,151,153,
        3,22,11,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,
        1,0,0,0,155,21,1,0,0,0,156,154,1,0,0,0,157,172,5,33,0,0,158,172,
        5,34,0,0,159,172,5,35,0,0,160,172,5,36,0,0,161,172,5,12,0,0,162,
        172,5,13,0,0,163,164,5,27,0,0,164,165,3,18,9,0,165,166,5,28,0,0,
        166,172,1,0,0,0,167,168,5,25,0,0,168,172,3,22,11,0,169,170,5,16,
        0,0,170,172,3,22,11,0,171,157,1,0,0,0,171,158,1,0,0,0,171,159,1,
        0,0,0,171,160,1,0,0,0,171,161,1,0,0,0,171,162,1,0,0,0,171,163,1,
        0,0,0,171,167,1,0,0,0,171,169,1,0,0,0,172,23,1,0,0,0,173,174,3,18,
        9,0,174,175,7,3,0,0,175,176,3,18,9,0,176,25,1,0,0,0,14,32,45,53,
        76,89,103,112,116,126,131,136,146,154,171
    ]

class LPMSParser ( Parser ):

    grammarFileName = "LPMS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'if'", "'else'", "'while'", 
                     "'print'", "'input'", "'const'", "'int'", "'float'", 
                     "'bool'", "'str'", "'true'", "'false'", "'break'", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'>='", 
                     "'<='", "'>'", "'<'", "'!'", "'='", "'('", "')'", "'{'", 
                     "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "IF", "ELSE", "WHILE", "PRINT", 
                      "INPUT", "CONST", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "CHAR_TYPE", "TRUE", "FALSE", "BREAK", "ADD", "SUB", 
                      "MUL", "DIV", "EQ", "NEQ", "GE", "LE", "GT", "LT", 
                      "NOT", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "COMMA", "SEMICOLON", "IDENTIFIER", "NUMBER", "CHAR_LITERAL", 
                      "STRING_LITERAL", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_declaration = 2
    RULE_constDeclaration = 3
    RULE_assignment = 4
    RULE_inputStmt = 5
    RULE_printStmt = 6
    RULE_ifStmt = 7
    RULE_whileStmt = 8
    RULE_expression = 9
    RULE_term = 10
    RULE_factor = 11
    RULE_comparison = 12

    ruleNames =  [ "program", "stmt", "declaration", "constDeclaration", 
                   "assignment", "inputStmt", "printStmt", "ifStmt", "whileStmt", 
                   "expression", "term", "factor", "comparison" ]

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
    TRUE=12
    FALSE=13
    BREAK=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    EQ=19
    NEQ=20
    GE=21
    LE=22
    GT=23
    LT=24
    NOT=25
    ASSIGN=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    COMMA=31
    SEMICOLON=32
    IDENTIFIER=33
    NUMBER=34
    CHAR_LITERAL=35
    STRING_LITERAL=36
    WS=37
    COMMENT=38

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

        def RBRACE(self):
            return self.getToken(LPMSParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(LPMSParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.StmtContext)
            else:
                return self.getTypedRuleContext(LPMSParser.StmtContext,i)


        def getRuleIndex(self):
            return LPMSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = LPMSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(LPMSParser.PROGRAM)
            self.state = 27
            self.match(LPMSParser.IDENTIFIER)
            self.state = 28
            self.match(LPMSParser.LBRACE)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589938676) != 0):
                self.state = 29
                self.stmt()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(LPMSParser.RBRACE)
            self.state = 36
            self.match(LPMSParser.EOF)
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


        def assignment(self):
            return self.getTypedRuleContext(LPMSParser.AssignmentContext,0)


        def constDeclaration(self):
            return self.getTypedRuleContext(LPMSParser.ConstDeclarationContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(LPMSParser.InputStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(LPMSParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(LPMSParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(LPMSParser.WhileStmtContext,0)


        def getRuleIndex(self):
            return LPMSParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = LPMSParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.declaration()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.assignment()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.constDeclaration()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.inputStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.printStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.ifStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 7)
                self.state = 44
                self.whileStmt()
                pass
            else:
                raise NoViableAltException(self)

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




    def declaration(self):

        localctx = LPMSParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 48
            self.match(LPMSParser.IDENTIFIER)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 49
                self.match(LPMSParser.COMMA)
                self.state = 50
                self.match(LPMSParser.IDENTIFIER)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
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




    def constDeclaration(self):

        localctx = LPMSParser.ConstDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(LPMSParser.CONST)
            self.state = 59
            self.match(LPMSParser.IDENTIFIER)
            self.state = 60
            self.match(LPMSParser.ASSIGN)
            self.state = 61
            self.expression()
            self.state = 62
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




    def assignment(self):

        localctx = LPMSParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(LPMSParser.IDENTIFIER)
            self.state = 65
            self.match(LPMSParser.ASSIGN)
            self.state = 66
            self.expression()
            self.state = 67
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




    def inputStmt(self):

        localctx = LPMSParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inputStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(LPMSParser.INPUT)
            self.state = 70
            self.match(LPMSParser.LPAREN)
            self.state = 71
            self.match(LPMSParser.IDENTIFIER)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 72
                self.match(LPMSParser.COMMA)
                self.state = 73
                self.match(LPMSParser.IDENTIFIER)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(LPMSParser.RPAREN)
            self.state = 80
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




    def printStmt(self):

        localctx = LPMSParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(LPMSParser.PRINT)
            self.state = 83
            self.match(LPMSParser.LPAREN)
            self.state = 84
            self.expression()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 85
                self.match(LPMSParser.COMMA)
                self.state = 86
                self.expression()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(LPMSParser.RPAREN)
            self.state = 93
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

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(LPMSParser.RBRACE)
            else:
                return self.getToken(LPMSParser.RBRACE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.StmtContext)
            else:
                return self.getTypedRuleContext(LPMSParser.StmtContext,i)


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




    def ifStmt(self):

        localctx = LPMSParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LPMSParser.IF)
            self.state = 96
            self.match(LPMSParser.LPAREN)
            self.state = 97
            self.expression()
            self.state = 98
            self.match(LPMSParser.RPAREN)
            self.state = 99
            self.match(LPMSParser.LBRACE)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589938676) != 0):
                self.state = 100
                self.stmt()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(LPMSParser.RBRACE)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 107
                self.match(LPMSParser.ELSE)
                self.state = 108
                self.match(LPMSParser.LBRACE)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589938676) != 0):
                    self.state = 109
                    self.stmt()
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
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

        def RBRACE(self):
            return self.getToken(LPMSParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.StmtContext)
            else:
                return self.getTypedRuleContext(LPMSParser.StmtContext,i)


        def BREAK(self):
            return self.getToken(LPMSParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(LPMSParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)




    def whileStmt(self):

        localctx = LPMSParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(LPMSParser.WHILE)
            self.state = 119
            self.match(LPMSParser.LPAREN)
            self.state = 120
            self.expression()
            self.state = 121
            self.match(LPMSParser.RPAREN)
            self.state = 122
            self.match(LPMSParser.LBRACE)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 123
                    self.stmt() 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 129
                self.match(LPMSParser.BREAK)
                self.state = 130
                self.match(LPMSParser.SEMICOLON)


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589938676) != 0):
                self.state = 133
                self.stmt()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(LPMSParser.RBRACE)
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




    def expression(self):

        localctx = LPMSParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.term()
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 142
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33128448) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 143
                    self.term() 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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




    def term(self):

        localctx = LPMSParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.factor()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 150
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.factor()
                self.state = 156
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




    def factor(self):

        localctx = LPMSParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(LPMSParser.IDENTIFIER)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(LPMSParser.NUMBER)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(LPMSParser.CHAR_LITERAL)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.match(LPMSParser.STRING_LITERAL)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.match(LPMSParser.TRUE)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.match(LPMSParser.FALSE)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.match(LPMSParser.LPAREN)
                self.state = 164
                self.expression()
                self.state = 165
                self.match(LPMSParser.RPAREN)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 8)
                self.state = 167
                self.match(LPMSParser.NOT)
                self.state = 168
                self.factor()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 9)
                self.state = 169
                self.match(LPMSParser.SUB)
                self.state = 170
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPMSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LPMSParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(LPMSParser.EQ, 0)

        def NEQ(self):
            return self.getToken(LPMSParser.NEQ, 0)

        def GE(self):
            return self.getToken(LPMSParser.GE, 0)

        def LE(self):
            return self.getToken(LPMSParser.LE, 0)

        def GT(self):
            return self.getToken(LPMSParser.GT, 0)

        def LT(self):
            return self.getToken(LPMSParser.LT, 0)

        def getRuleIndex(self):
            return LPMSParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = LPMSParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.expression()
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 175
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





