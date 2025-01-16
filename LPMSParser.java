// Generated from C:/Users/nonda/Downloads/TrabalhoCompiladorCompleto/Compiladores-2024-2/LPMS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LPMSParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAM=1, IF=2, ELSE=3, WHILE=4, PRINT=5, INPUT=6, CONST=7, INT_TYPE=8, 
		FLOAT_TYPE=9, BOOL_TYPE=10, CHAR_TYPE=11, RETURN=12, TRUE=13, FALSE=14, 
		BREAK=15, ADD=16, SUB=17, MUL=18, DIV=19, EQ=20, NEQ=21, GE=22, LE=23, 
		GT=24, LT=25, NOT=26, ASSIGN=27, LPAREN=28, RPAREN=29, LBRACE=30, RBRACE=31, 
		COMMA=32, SEMICOLON=33, IDENTIFIER=34, NUMBER=35, CHAR_LITERAL=36, STRING_LITERAL=37, 
		WS=38, COMMENT=39;
	public static final int
		RULE_program = 0, RULE_block = 1, RULE_stmt = 2, RULE_declaration = 3, 
		RULE_constDeclaration = 4, RULE_assignment = 5, RULE_inputStmt = 6, RULE_printStmt = 7, 
		RULE_ifStmt = 8, RULE_whileStmt = 9, RULE_functionDecl = 10, RULE_parameters = 11, 
		RULE_parameter = 12, RULE_functionCall = 13, RULE_arguments = 14, RULE_returnStmt = 15, 
		RULE_expression = 16, RULE_term = 17, RULE_factor = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "block", "stmt", "declaration", "constDeclaration", "assignment", 
			"inputStmt", "printStmt", "ifStmt", "whileStmt", "functionDecl", "parameters", 
			"parameter", "functionCall", "arguments", "returnStmt", "expression", 
			"term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Program'", "'if'", "'else'", "'while'", "'print'", "'input'", 
			"'const'", "'int'", "'float'", "'bool'", "'str'", "'return'", "'true'", 
			"'false'", "'break'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'>='", 
			"'<='", "'>'", "'<'", "'!'", "'='", "'('", "')'", "'{'", "'}'", "','", 
			"';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "IF", "ELSE", "WHILE", "PRINT", "INPUT", "CONST", "INT_TYPE", 
			"FLOAT_TYPE", "BOOL_TYPE", "CHAR_TYPE", "RETURN", "TRUE", "FALSE", "BREAK", 
			"ADD", "SUB", "MUL", "DIV", "EQ", "NEQ", "GE", "LE", "GT", "LT", "NOT", 
			"ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COMMA", "SEMICOLON", 
			"IDENTIFIER", "NUMBER", "CHAR_LITERAL", "STRING_LITERAL", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LPMS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LPMSParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(LPMSParser.PROGRAM, 0); }
		public TerminalNode IDENTIFIER() { return getToken(LPMSParser.IDENTIFIER, 0); }
		public TerminalNode LBRACE() { return getToken(LPMSParser.LBRACE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(LPMSParser.RBRACE, 0); }
		public TerminalNode EOF() { return getToken(LPMSParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(PROGRAM);
			setState(39);
			match(IDENTIFIER);
			setState(40);
			match(LBRACE);
			setState(41);
			block();
			setState(42);
			match(RBRACE);
			setState(43);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(45);
					stmt();
					}
					} 
				}
				setState(50);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public ConstDeclarationContext constDeclaration() {
			return getRuleContext(ConstDeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public InputStmtContext inputStmt() {
			return getRuleContext(InputStmtContext.class,0);
		}
		public PrintStmtContext printStmt() {
			return getRuleContext(PrintStmtContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public FunctionDeclContext functionDecl() {
			return getRuleContext(FunctionDeclContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public TerminalNode BREAK() { return getToken(LPMSParser.BREAK, 0); }
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stmt);
		try {
			setState(65);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				constDeclaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(53);
				assignment();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(54);
				inputStmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(55);
				printStmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(56);
				ifStmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(57);
				whileStmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(58);
				functionDecl();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(59);
				functionCall();
				setState(60);
				match(SEMICOLON);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(62);
				returnStmt();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(63);
				match(BREAK);
				setState(64);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(LPMSParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(LPMSParser.IDENTIFIER, i);
		}
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
		public TerminalNode INT_TYPE() { return getToken(LPMSParser.INT_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(LPMSParser.FLOAT_TYPE, 0); }
		public TerminalNode BOOL_TYPE() { return getToken(LPMSParser.BOOL_TYPE, 0); }
		public TerminalNode CHAR_TYPE() { return getToken(LPMSParser.CHAR_TYPE, 0); }
		public List<TerminalNode> ASSIGN() { return getTokens(LPMSParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(LPMSParser.ASSIGN, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LPMSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LPMSParser.COMMA, i);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitDeclaration(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitDeclaration(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(68);
			match(IDENTIFIER);
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(69);
				match(ASSIGN);
				setState(70);
				expression();
				}
			}

			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(73);
				match(COMMA);
				setState(74);
				match(IDENTIFIER);
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(75);
					match(ASSIGN);
					setState(76);
					expression();
					}
				}

				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(84);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstDeclarationContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(LPMSParser.CONST, 0); }
		public TerminalNode IDENTIFIER() { return getToken(LPMSParser.IDENTIFIER, 0); }
		public TerminalNode ASSIGN() { return getToken(LPMSParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
		public ConstDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterConstDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitConstDeclaration(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitConstDeclaration(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ConstDeclarationContext constDeclaration() throws RecognitionException {
		ConstDeclarationContext _localctx = new ConstDeclarationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_constDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(CONST);
			setState(87);
			match(IDENTIFIER);
			setState(88);
			match(ASSIGN);
			setState(89);
			expression();
			setState(90);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LPMSParser.IDENTIFIER, 0); }
		public TerminalNode ASSIGN() { return getToken(LPMSParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(IDENTIFIER);
			setState(93);
			match(ASSIGN);
			setState(94);
			expression();
			setState(95);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputStmtContext extends ParserRuleContext {
		public TerminalNode INPUT() { return getToken(LPMSParser.INPUT, 0); }
		public TerminalNode LPAREN() { return getToken(LPMSParser.LPAREN, 0); }
		public List<TerminalNode> IDENTIFIER() { return getTokens(LPMSParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(LPMSParser.IDENTIFIER, i);
		}
		public TerminalNode RPAREN() { return getToken(LPMSParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(LPMSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LPMSParser.COMMA, i);
		}
		public InputStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterInputStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitInputStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitInputStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InputStmtContext inputStmt() throws RecognitionException {
		InputStmtContext _localctx = new InputStmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_inputStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(INPUT);
			setState(98);
			match(LPAREN);
			setState(99);
			match(IDENTIFIER);
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(100);
				match(COMMA);
				setState(101);
				match(IDENTIFIER);
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(107);
			match(RPAREN);
			setState(108);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(LPMSParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(LPMSParser.LPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(LPMSParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(LPMSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LPMSParser.COMMA, i);
		}
		public PrintStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterPrintStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitPrintStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitPrintStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrintStmtContext printStmt() throws RecognitionException {
		PrintStmtContext _localctx = new PrintStmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_printStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(PRINT);
			setState(111);
			match(LPAREN);
			setState(112);
			expression();
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(113);
				match(COMMA);
				setState(114);
				expression();
				}
				}
				setState(119);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(120);
			match(RPAREN);
			setState(121);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(LPMSParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(LPMSParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LPMSParser.RPAREN, 0); }
		public List<TerminalNode> LBRACE() { return getTokens(LPMSParser.LBRACE); }
		public TerminalNode LBRACE(int i) {
			return getToken(LPMSParser.LBRACE, i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<TerminalNode> RBRACE() { return getTokens(LPMSParser.RBRACE); }
		public TerminalNode RBRACE(int i) {
			return getToken(LPMSParser.RBRACE, i);
		}
		public TerminalNode ELSE() { return getToken(LPMSParser.ELSE, 0); }
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterIfStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitIfStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitIfStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(IF);
			setState(124);
			match(LPAREN);
			setState(125);
			expression();
			setState(126);
			match(RPAREN);
			setState(127);
			match(LBRACE);
			setState(128);
			block();
			setState(129);
			match(RBRACE);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(130);
				match(ELSE);
				setState(131);
				match(LBRACE);
				setState(132);
				block();
				setState(133);
				match(RBRACE);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(LPMSParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(LPMSParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LPMSParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(LPMSParser.LBRACE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(LPMSParser.RBRACE, 0); }
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterWhileStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitWhileStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitWhileStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_whileStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(WHILE);
			setState(138);
			match(LPAREN);
			setState(139);
			expression();
			setState(140);
			match(RPAREN);
			setState(141);
			match(LBRACE);
			setState(142);
			block();
			setState(143);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LPMSParser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(LPMSParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(LPMSParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(LPMSParser.LBRACE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(LPMSParser.RBRACE, 0); }
		public TerminalNode INT_TYPE() { return getToken(LPMSParser.INT_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(LPMSParser.FLOAT_TYPE, 0); }
		public TerminalNode BOOL_TYPE() { return getToken(LPMSParser.BOOL_TYPE, 0); }
		public TerminalNode CHAR_TYPE() { return getToken(LPMSParser.CHAR_TYPE, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public FunctionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterFunctionDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitFunctionDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitFunctionDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionDeclContext functionDecl() throws RecognitionException {
		FunctionDeclContext _localctx = new FunctionDeclContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_functionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(146);
			match(IDENTIFIER);
			setState(147);
			match(LPAREN);
			setState(149);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) {
				{
				setState(148);
				parameters();
				}
			}

			setState(151);
			match(RPAREN);
			setState(152);
			match(LBRACE);
			setState(153);
			block();
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==RETURN) {
				{
				setState(154);
				returnStmt();
				}
			}

			setState(157);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LPMSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LPMSParser.COMMA, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterParameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitParameters(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitParameters(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			parameter();
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(160);
				match(COMMA);
				setState(161);
				parameter();
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LPMSParser.IDENTIFIER, 0); }
		public TerminalNode INT_TYPE() { return getToken(LPMSParser.INT_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(LPMSParser.FLOAT_TYPE, 0); }
		public TerminalNode BOOL_TYPE() { return getToken(LPMSParser.BOOL_TYPE, 0); }
		public TerminalNode CHAR_TYPE() { return getToken(LPMSParser.CHAR_TYPE, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitParameter(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitParameter(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(168);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LPMSParser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(LPMSParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(LPMSParser.RPAREN, 0); }
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterFunctionCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitFunctionCall(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitFunctionCall(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(IDENTIFIER);
			setState(171);
			match(LPAREN);
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 258033737728L) != 0)) {
				{
				setState(172);
				arguments();
				}
			}

			setState(175);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LPMSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LPMSParser.COMMA, i);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterArguments(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitArguments(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitArguments(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			expression();
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(178);
				match(COMMA);
				setState(179);
				expression();
				}
				}
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(LPMSParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
		public ReturnStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterReturnStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitReturnStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitReturnStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReturnStmtContext returnStmt() throws RecognitionException {
		ReturnStmtContext _localctx = new ReturnStmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_returnStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			match(RETURN);
			setState(186);
			expression();
			setState(187);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> ADD() { return getTokens(LPMSParser.ADD); }
		public TerminalNode ADD(int i) {
			return getToken(LPMSParser.ADD, i);
		}
		public List<TerminalNode> SUB() { return getTokens(LPMSParser.SUB); }
		public TerminalNode SUB(int i) {
			return getToken(LPMSParser.SUB, i);
		}
		public List<TerminalNode> GT() { return getTokens(LPMSParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(LPMSParser.GT, i);
		}
		public List<TerminalNode> LT() { return getTokens(LPMSParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(LPMSParser.LT, i);
		}
		public List<TerminalNode> GE() { return getTokens(LPMSParser.GE); }
		public TerminalNode GE(int i) {
			return getToken(LPMSParser.GE, i);
		}
		public List<TerminalNode> LE() { return getTokens(LPMSParser.LE); }
		public TerminalNode LE(int i) {
			return getToken(LPMSParser.LE, i);
		}
		public List<TerminalNode> EQ() { return getTokens(LPMSParser.EQ); }
		public TerminalNode EQ(int i) {
			return getToken(LPMSParser.EQ, i);
		}
		public List<TerminalNode> NEQ() { return getTokens(LPMSParser.NEQ); }
		public TerminalNode NEQ(int i) {
			return getToken(LPMSParser.NEQ, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			term();
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 66256896L) != 0)) {
				{
				{
				setState(190);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 66256896L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(191);
				term();
				}
				}
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MUL() { return getTokens(LPMSParser.MUL); }
		public TerminalNode MUL(int i) {
			return getToken(LPMSParser.MUL, i);
		}
		public List<TerminalNode> DIV() { return getTokens(LPMSParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(LPMSParser.DIV, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitTerm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitTerm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			factor();
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL || _la==DIV) {
				{
				{
				setState(198);
				_la = _input.LA(1);
				if ( !(_la==MUL || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(199);
				factor();
				}
				}
				setState(204);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LPMSParser.IDENTIFIER, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(LPMSParser.NUMBER, 0); }
		public TerminalNode CHAR_LITERAL() { return getToken(LPMSParser.CHAR_LITERAL, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(LPMSParser.STRING_LITERAL, 0); }
		public TerminalNode TRUE() { return getToken(LPMSParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(LPMSParser.FALSE, 0); }
		public TerminalNode LPAREN() { return getToken(LPMSParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LPMSParser.RPAREN, 0); }
		public TerminalNode NOT() { return getToken(LPMSParser.NOT, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminalNode SUB() { return getToken(LPMSParser.SUB, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitFactor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitFactor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_factor);
		try {
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				functionCall();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(207);
				match(NUMBER);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(208);
				match(CHAR_LITERAL);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(209);
				match(STRING_LITERAL);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(210);
				match(TRUE);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(211);
				match(FALSE);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(212);
				match(LPAREN);
				setState(213);
				expression();
				setState(214);
				match(RPAREN);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(216);
				match(NOT);
				setState(217);
				factor();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(218);
				match(SUB);
				setState(219);
				factor();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\'\u00df\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0005\u0001/\b\u0001\n\u0001\f\u00012\t\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002B\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003H\b\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003N\b\u0003\u0005\u0003P\b\u0003\n\u0003"+
		"\f\u0003S\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0005\u0006g\b\u0006\n\u0006\f\u0006j\t\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0005\u0007t\b\u0007\n\u0007\f\u0007w\t\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0088"+
		"\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0003\n\u0096\b\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u009c\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0005\u000b\u00a3\b\u000b\n\u000b\f\u000b\u00a6\t\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\r\u0003\r\u00ae\b\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00b5\b\u000e\n\u000e\f\u000e"+
		"\u00b8\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0005\u0010\u00c1\b\u0010\n\u0010\f\u0010\u00c4"+
		"\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u00c9\b\u0011"+
		"\n\u0011\f\u0011\u00cc\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003"+
		"\u0012\u00dd\b\u0012\u0001\u0012\u0000\u0000\u0013\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$\u0000"+
		"\u0003\u0001\u0000\b\u000b\u0002\u0000\u0010\u0011\u0014\u0019\u0001\u0000"+
		"\u0012\u0013\u00ec\u0000&\u0001\u0000\u0000\u0000\u00020\u0001\u0000\u0000"+
		"\u0000\u0004A\u0001\u0000\u0000\u0000\u0006C\u0001\u0000\u0000\u0000\b"+
		"V\u0001\u0000\u0000\u0000\n\\\u0001\u0000\u0000\u0000\fa\u0001\u0000\u0000"+
		"\u0000\u000en\u0001\u0000\u0000\u0000\u0010{\u0001\u0000\u0000\u0000\u0012"+
		"\u0089\u0001\u0000\u0000\u0000\u0014\u0091\u0001\u0000\u0000\u0000\u0016"+
		"\u009f\u0001\u0000\u0000\u0000\u0018\u00a7\u0001\u0000\u0000\u0000\u001a"+
		"\u00aa\u0001\u0000\u0000\u0000\u001c\u00b1\u0001\u0000\u0000\u0000\u001e"+
		"\u00b9\u0001\u0000\u0000\u0000 \u00bd\u0001\u0000\u0000\u0000\"\u00c5"+
		"\u0001\u0000\u0000\u0000$\u00dc\u0001\u0000\u0000\u0000&\'\u0005\u0001"+
		"\u0000\u0000\'(\u0005\"\u0000\u0000()\u0005\u001e\u0000\u0000)*\u0003"+
		"\u0002\u0001\u0000*+\u0005\u001f\u0000\u0000+,\u0005\u0000\u0000\u0001"+
		",\u0001\u0001\u0000\u0000\u0000-/\u0003\u0004\u0002\u0000.-\u0001\u0000"+
		"\u0000\u0000/2\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u000001\u0001"+
		"\u0000\u0000\u00001\u0003\u0001\u0000\u0000\u000020\u0001\u0000\u0000"+
		"\u00003B\u0003\u0006\u0003\u00004B\u0003\b\u0004\u00005B\u0003\n\u0005"+
		"\u00006B\u0003\f\u0006\u00007B\u0003\u000e\u0007\u00008B\u0003\u0010\b"+
		"\u00009B\u0003\u0012\t\u0000:B\u0003\u0014\n\u0000;<\u0003\u001a\r\u0000"+
		"<=\u0005!\u0000\u0000=B\u0001\u0000\u0000\u0000>B\u0003\u001e\u000f\u0000"+
		"?@\u0005\u000f\u0000\u0000@B\u0005!\u0000\u0000A3\u0001\u0000\u0000\u0000"+
		"A4\u0001\u0000\u0000\u0000A5\u0001\u0000\u0000\u0000A6\u0001\u0000\u0000"+
		"\u0000A7\u0001\u0000\u0000\u0000A8\u0001\u0000\u0000\u0000A9\u0001\u0000"+
		"\u0000\u0000A:\u0001\u0000\u0000\u0000A;\u0001\u0000\u0000\u0000A>\u0001"+
		"\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000B\u0005\u0001\u0000\u0000"+
		"\u0000CD\u0007\u0000\u0000\u0000DG\u0005\"\u0000\u0000EF\u0005\u001b\u0000"+
		"\u0000FH\u0003 \u0010\u0000GE\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000"+
		"\u0000HQ\u0001\u0000\u0000\u0000IJ\u0005 \u0000\u0000JM\u0005\"\u0000"+
		"\u0000KL\u0005\u001b\u0000\u0000LN\u0003 \u0010\u0000MK\u0001\u0000\u0000"+
		"\u0000MN\u0001\u0000\u0000\u0000NP\u0001\u0000\u0000\u0000OI\u0001\u0000"+
		"\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000RT\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000"+
		"TU\u0005!\u0000\u0000U\u0007\u0001\u0000\u0000\u0000VW\u0005\u0007\u0000"+
		"\u0000WX\u0005\"\u0000\u0000XY\u0005\u001b\u0000\u0000YZ\u0003 \u0010"+
		"\u0000Z[\u0005!\u0000\u0000[\t\u0001\u0000\u0000\u0000\\]\u0005\"\u0000"+
		"\u0000]^\u0005\u001b\u0000\u0000^_\u0003 \u0010\u0000_`\u0005!\u0000\u0000"+
		"`\u000b\u0001\u0000\u0000\u0000ab\u0005\u0006\u0000\u0000bc\u0005\u001c"+
		"\u0000\u0000ch\u0005\"\u0000\u0000de\u0005 \u0000\u0000eg\u0005\"\u0000"+
		"\u0000fd\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000"+
		"\u0000\u0000hi\u0001\u0000\u0000\u0000ik\u0001\u0000\u0000\u0000jh\u0001"+
		"\u0000\u0000\u0000kl\u0005\u001d\u0000\u0000lm\u0005!\u0000\u0000m\r\u0001"+
		"\u0000\u0000\u0000no\u0005\u0005\u0000\u0000op\u0005\u001c\u0000\u0000"+
		"pu\u0003 \u0010\u0000qr\u0005 \u0000\u0000rt\u0003 \u0010\u0000sq\u0001"+
		"\u0000\u0000\u0000tw\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000"+
		"uv\u0001\u0000\u0000\u0000vx\u0001\u0000\u0000\u0000wu\u0001\u0000\u0000"+
		"\u0000xy\u0005\u001d\u0000\u0000yz\u0005!\u0000\u0000z\u000f\u0001\u0000"+
		"\u0000\u0000{|\u0005\u0002\u0000\u0000|}\u0005\u001c\u0000\u0000}~\u0003"+
		" \u0010\u0000~\u007f\u0005\u001d\u0000\u0000\u007f\u0080\u0005\u001e\u0000"+
		"\u0000\u0080\u0081\u0003\u0002\u0001\u0000\u0081\u0087\u0005\u001f\u0000"+
		"\u0000\u0082\u0083\u0005\u0003\u0000\u0000\u0083\u0084\u0005\u001e\u0000"+
		"\u0000\u0084\u0085\u0003\u0002\u0001\u0000\u0085\u0086\u0005\u001f\u0000"+
		"\u0000\u0086\u0088\u0001\u0000\u0000\u0000\u0087\u0082\u0001\u0000\u0000"+
		"\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0011\u0001\u0000\u0000"+
		"\u0000\u0089\u008a\u0005\u0004\u0000\u0000\u008a\u008b\u0005\u001c\u0000"+
		"\u0000\u008b\u008c\u0003 \u0010\u0000\u008c\u008d\u0005\u001d\u0000\u0000"+
		"\u008d\u008e\u0005\u001e\u0000\u0000\u008e\u008f\u0003\u0002\u0001\u0000"+
		"\u008f\u0090\u0005\u001f\u0000\u0000\u0090\u0013\u0001\u0000\u0000\u0000"+
		"\u0091\u0092\u0007\u0000\u0000\u0000\u0092\u0093\u0005\"\u0000\u0000\u0093"+
		"\u0095\u0005\u001c\u0000\u0000\u0094\u0096\u0003\u0016\u000b\u0000\u0095"+
		"\u0094\u0001\u0000\u0000\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096"+
		"\u0097\u0001\u0000\u0000\u0000\u0097\u0098\u0005\u001d\u0000\u0000\u0098"+
		"\u0099\u0005\u001e\u0000\u0000\u0099\u009b\u0003\u0002\u0001\u0000\u009a"+
		"\u009c\u0003\u001e\u000f\u0000\u009b\u009a\u0001\u0000\u0000\u0000\u009b"+
		"\u009c\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0005\u001f\u0000\u0000\u009e\u0015\u0001\u0000\u0000\u0000\u009f"+
		"\u00a4\u0003\u0018\f\u0000\u00a0\u00a1\u0005 \u0000\u0000\u00a1\u00a3"+
		"\u0003\u0018\f\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a3\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a5\u0017\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a8\u0007\u0000\u0000\u0000\u00a8\u00a9\u0005"+
		"\"\u0000\u0000\u00a9\u0019\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005\""+
		"\u0000\u0000\u00ab\u00ad\u0005\u001c\u0000\u0000\u00ac\u00ae\u0003\u001c"+
		"\u000e\u0000\u00ad\u00ac\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000"+
		"\u0000\u0000\u00ae\u00af\u0001\u0000\u0000\u0000\u00af\u00b0\u0005\u001d"+
		"\u0000\u0000\u00b0\u001b\u0001\u0000\u0000\u0000\u00b1\u00b6\u0003 \u0010"+
		"\u0000\u00b2\u00b3\u0005 \u0000\u0000\u00b3\u00b5\u0003 \u0010\u0000\u00b4"+
		"\u00b2\u0001\u0000\u0000\u0000\u00b5\u00b8\u0001\u0000\u0000\u0000\u00b6"+
		"\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7"+
		"\u001d\u0001\u0000\u0000\u0000\u00b8\u00b6\u0001\u0000\u0000\u0000\u00b9"+
		"\u00ba\u0005\f\u0000\u0000\u00ba\u00bb\u0003 \u0010\u0000\u00bb\u00bc"+
		"\u0005!\u0000\u0000\u00bc\u001f\u0001\u0000\u0000\u0000\u00bd\u00c2\u0003"+
		"\"\u0011\u0000\u00be\u00bf\u0007\u0001\u0000\u0000\u00bf\u00c1\u0003\""+
		"\u0011\u0000\u00c0\u00be\u0001\u0000\u0000\u0000\u00c1\u00c4\u0001\u0000"+
		"\u0000\u0000\u00c2\u00c0\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000"+
		"\u0000\u0000\u00c3!\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000"+
		"\u0000\u00c5\u00ca\u0003$\u0012\u0000\u00c6\u00c7\u0007\u0002\u0000\u0000"+
		"\u00c7\u00c9\u0003$\u0012\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9"+
		"\u00cc\u0001\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00ca"+
		"\u00cb\u0001\u0000\u0000\u0000\u00cb#\u0001\u0000\u0000\u0000\u00cc\u00ca"+
		"\u0001\u0000\u0000\u0000\u00cd\u00dd\u0005\"\u0000\u0000\u00ce\u00dd\u0003"+
		"\u001a\r\u0000\u00cf\u00dd\u0005#\u0000\u0000\u00d0\u00dd\u0005$\u0000"+
		"\u0000\u00d1\u00dd\u0005%\u0000\u0000\u00d2\u00dd\u0005\r\u0000\u0000"+
		"\u00d3\u00dd\u0005\u000e\u0000\u0000\u00d4\u00d5\u0005\u001c\u0000\u0000"+
		"\u00d5\u00d6\u0003 \u0010\u0000\u00d6\u00d7\u0005\u001d\u0000\u0000\u00d7"+
		"\u00dd\u0001\u0000\u0000\u0000\u00d8\u00d9\u0005\u001a\u0000\u0000\u00d9"+
		"\u00dd\u0003$\u0012\u0000\u00da\u00db\u0005\u0011\u0000\u0000\u00db\u00dd"+
		"\u0003$\u0012\u0000\u00dc\u00cd\u0001\u0000\u0000\u0000\u00dc\u00ce\u0001"+
		"\u0000\u0000\u0000\u00dc\u00cf\u0001\u0000\u0000\u0000\u00dc\u00d0\u0001"+
		"\u0000\u0000\u0000\u00dc\u00d1\u0001\u0000\u0000\u0000\u00dc\u00d2\u0001"+
		"\u0000\u0000\u0000\u00dc\u00d3\u0001\u0000\u0000\u0000\u00dc\u00d4\u0001"+
		"\u0000\u0000\u0000\u00dc\u00d8\u0001\u0000\u0000\u0000\u00dc\u00da\u0001"+
		"\u0000\u0000\u0000\u00dd%\u0001\u0000\u0000\u0000\u00100AGMQhu\u0087\u0095"+
		"\u009b\u00a4\u00ad\u00b6\u00c2\u00ca\u00dc";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}