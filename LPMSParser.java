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
		FLOAT_TYPE=9, BOOL_TYPE=10, CHAR_TYPE=11, TRUE=12, FALSE=13, BREAK=14, 
		ADD=15, SUB=16, MUL=17, DIV=18, EQ=19, NEQ=20, GE=21, LE=22, GT=23, LT=24, 
		NOT=25, ASSIGN=26, LPAREN=27, RPAREN=28, LBRACE=29, RBRACE=30, COMMA=31, 
		SEMICOLON=32, IDENTIFIER=33, NUMBER=34, CHAR_LITERAL=35, STRING_LITERAL=36, 
		WS=37, COMMENT=38;
	public static final int
		RULE_program = 0, RULE_stmt = 1, RULE_declaration = 2, RULE_constDeclaration = 3, 
		RULE_assignment = 4, RULE_inputStmt = 5, RULE_printStmt = 6, RULE_ifStmt = 7, 
		RULE_whileStmt = 8, RULE_expression = 9, RULE_term = 10, RULE_factor = 11, 
		RULE_comparison = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stmt", "declaration", "constDeclaration", "assignment", "inputStmt", 
			"printStmt", "ifStmt", "whileStmt", "expression", "term", "factor", "comparison"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Program'", "'if'", "'else'", "'while'", "'print'", "'input'", 
			"'const'", "'int'", "'float'", "'bool'", "'str'", "'true'", "'false'", 
			"'break'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'>='", "'<='", 
			"'>'", "'<'", "'!'", "'='", "'('", "')'", "'{'", "'}'", "','", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "IF", "ELSE", "WHILE", "PRINT", "INPUT", "CONST", "INT_TYPE", 
			"FLOAT_TYPE", "BOOL_TYPE", "CHAR_TYPE", "TRUE", "FALSE", "BREAK", "ADD", 
			"SUB", "MUL", "DIV", "EQ", "NEQ", "GE", "LE", "GT", "LT", "NOT", "ASSIGN", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "COMMA", "SEMICOLON", "IDENTIFIER", 
			"NUMBER", "CHAR_LITERAL", "STRING_LITERAL", "WS", "COMMENT"
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
		public TerminalNode RBRACE() { return getToken(LPMSParser.RBRACE, 0); }
		public TerminalNode EOF() { return getToken(LPMSParser.EOF, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(PROGRAM);
			setState(27);
			match(IDENTIFIER);
			setState(28);
			match(LBRACE);
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589938676L) != 0)) {
				{
				{
				setState(29);
				stmt();
				}
				}
				setState(34);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(35);
			match(RBRACE);
			setState(36);
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
	public static class StmtContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ConstDeclarationContext constDeclaration() {
			return getRuleContext(ConstDeclarationContext.class,0);
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
		enterRule(_localctx, 2, RULE_stmt);
		try {
			setState(45);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
			case FLOAT_TYPE:
			case BOOL_TYPE:
			case CHAR_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				declaration();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				assignment();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 3);
				{
				setState(40);
				constDeclaration();
				}
				break;
			case INPUT:
				enterOuterAlt(_localctx, 4);
				{
				setState(41);
				inputStmt();
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 5);
				{
				setState(42);
				printStmt();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 6);
				{
				setState(43);
				ifStmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 7);
				{
				setState(44);
				whileStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		enterRule(_localctx, 4, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(48);
			match(IDENTIFIER);
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(49);
				match(COMMA);
				setState(50);
				match(IDENTIFIER);
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(56);
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
		enterRule(_localctx, 6, RULE_constDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(CONST);
			setState(59);
			match(IDENTIFIER);
			setState(60);
			match(ASSIGN);
			setState(61);
			expression();
			setState(62);
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
		enterRule(_localctx, 8, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(IDENTIFIER);
			setState(65);
			match(ASSIGN);
			setState(66);
			expression();
			setState(67);
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
		enterRule(_localctx, 10, RULE_inputStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(INPUT);
			setState(70);
			match(LPAREN);
			setState(71);
			match(IDENTIFIER);
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(72);
				match(COMMA);
				setState(73);
				match(IDENTIFIER);
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(79);
			match(RPAREN);
			setState(80);
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
		enterRule(_localctx, 12, RULE_printStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(PRINT);
			setState(83);
			match(LPAREN);
			setState(84);
			expression();
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(85);
				match(COMMA);
				setState(86);
				expression();
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(92);
			match(RPAREN);
			setState(93);
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
		public List<TerminalNode> RBRACE() { return getTokens(LPMSParser.RBRACE); }
		public TerminalNode RBRACE(int i) {
			return getToken(LPMSParser.RBRACE, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
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
		enterRule(_localctx, 14, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(IF);
			setState(96);
			match(LPAREN);
			setState(97);
			expression();
			setState(98);
			match(RPAREN);
			setState(99);
			match(LBRACE);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589938676L) != 0)) {
				{
				{
				setState(100);
				stmt();
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(106);
			match(RBRACE);
			setState(116);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(107);
				match(ELSE);
				setState(108);
				match(LBRACE);
				setState(112);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589938676L) != 0)) {
					{
					{
					setState(109);
					stmt();
					}
					}
					setState(114);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(115);
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
		public TerminalNode RBRACE() { return getToken(LPMSParser.RBRACE, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public TerminalNode BREAK() { return getToken(LPMSParser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(LPMSParser.SEMICOLON, 0); }
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
		enterRule(_localctx, 16, RULE_whileStmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(WHILE);
			setState(119);
			match(LPAREN);
			setState(120);
			expression();
			setState(121);
			match(RPAREN);
			setState(122);
			match(LBRACE);
			setState(126);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(123);
					stmt();
					}
					} 
				}
				setState(128);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BREAK) {
				{
				setState(129);
				match(BREAK);
				setState(130);
				match(SEMICOLON);
				}
			}

			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589938676L) != 0)) {
				{
				{
				setState(133);
				stmt();
				}
				}
				setState(138);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(139);
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
		enterRule(_localctx, 18, RULE_expression);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			term();
			setState(146);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(142);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 33128448L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(143);
					term();
					}
					} 
				}
				setState(148);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
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
		enterRule(_localctx, 20, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			factor();
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL || _la==DIV) {
				{
				{
				setState(150);
				_la = _input.LA(1);
				if ( !(_la==MUL || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(151);
				factor();
				}
				}
				setState(156);
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
		enterRule(_localctx, 22, RULE_factor);
		try {
			setState(171);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(157);
				match(IDENTIFIER);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(158);
				match(NUMBER);
				}
				break;
			case CHAR_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(159);
				match(CHAR_LITERAL);
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(160);
				match(STRING_LITERAL);
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 5);
				{
				setState(161);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 6);
				{
				setState(162);
				match(FALSE);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 7);
				{
				setState(163);
				match(LPAREN);
				setState(164);
				expression();
				setState(165);
				match(RPAREN);
				}
				break;
			case NOT:
				enterOuterAlt(_localctx, 8);
				{
				setState(167);
				match(NOT);
				setState(168);
				factor();
				}
				break;
			case SUB:
				enterOuterAlt(_localctx, 9);
				{
				setState(169);
				match(SUB);
				setState(170);
				factor();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class ComparisonContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(LPMSParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(LPMSParser.NEQ, 0); }
		public TerminalNode GE() { return getToken(LPMSParser.GE, 0); }
		public TerminalNode LE() { return getToken(LPMSParser.LE, 0); }
		public TerminalNode GT() { return getToken(LPMSParser.GT, 0); }
		public TerminalNode LT() { return getToken(LPMSParser.LT, 0); }
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).enterComparison(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LPMSListener ) ((LPMSListener)listener).exitComparison(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LPMSVisitor ) return ((LPMSVisitor<? extends T>)visitor).visitComparison(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			expression();
			setState(174);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 33030144L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(175);
			expression();
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
		"\u0004\u0001&\u00b2\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000"+
		"\u001f\b\u0000\n\u0000\f\u0000\"\t\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0003\u0001.\b\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0005\u00024\b\u0002\n\u0002\f\u00027\t\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0005"+
		"\u0005K\b\u0005\n\u0005\f\u0005N\t\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005"+
		"\u0006X\b\u0006\n\u0006\f\u0006[\t\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0005\u0007f\b\u0007\n\u0007\f\u0007i\t\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0005\u0007o\b\u0007\n\u0007\f\u0007r\t"+
		"\u0007\u0001\u0007\u0003\u0007u\b\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0005\b}\b\b\n\b\f\b\u0080\t\b\u0001\b\u0001\b\u0003"+
		"\b\u0084\b\b\u0001\b\u0005\b\u0087\b\b\n\b\f\b\u008a\t\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0005\t\u0091\b\t\n\t\f\t\u0094\t\t\u0001\n"+
		"\u0001\n\u0001\n\u0005\n\u0099\b\n\n\n\f\n\u009c\t\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u00ac\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0000\u0000\r\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u0000\u0004\u0001\u0000\b\u000b\u0002\u0000\u000f\u0010\u0013"+
		"\u0018\u0001\u0000\u0011\u0012\u0001\u0000\u0013\u0018\u00be\u0000\u001a"+
		"\u0001\u0000\u0000\u0000\u0002-\u0001\u0000\u0000\u0000\u0004/\u0001\u0000"+
		"\u0000\u0000\u0006:\u0001\u0000\u0000\u0000\b@\u0001\u0000\u0000\u0000"+
		"\nE\u0001\u0000\u0000\u0000\fR\u0001\u0000\u0000\u0000\u000e_\u0001\u0000"+
		"\u0000\u0000\u0010v\u0001\u0000\u0000\u0000\u0012\u008d\u0001\u0000\u0000"+
		"\u0000\u0014\u0095\u0001\u0000\u0000\u0000\u0016\u00ab\u0001\u0000\u0000"+
		"\u0000\u0018\u00ad\u0001\u0000\u0000\u0000\u001a\u001b\u0005\u0001\u0000"+
		"\u0000\u001b\u001c\u0005!\u0000\u0000\u001c \u0005\u001d\u0000\u0000\u001d"+
		"\u001f\u0003\u0002\u0001\u0000\u001e\u001d\u0001\u0000\u0000\u0000\u001f"+
		"\"\u0001\u0000\u0000\u0000 \u001e\u0001\u0000\u0000\u0000 !\u0001\u0000"+
		"\u0000\u0000!#\u0001\u0000\u0000\u0000\" \u0001\u0000\u0000\u0000#$\u0005"+
		"\u001e\u0000\u0000$%\u0005\u0000\u0000\u0001%\u0001\u0001\u0000\u0000"+
		"\u0000&.\u0003\u0004\u0002\u0000\'.\u0003\b\u0004\u0000(.\u0003\u0006"+
		"\u0003\u0000).\u0003\n\u0005\u0000*.\u0003\f\u0006\u0000+.\u0003\u000e"+
		"\u0007\u0000,.\u0003\u0010\b\u0000-&\u0001\u0000\u0000\u0000-\'\u0001"+
		"\u0000\u0000\u0000-(\u0001\u0000\u0000\u0000-)\u0001\u0000\u0000\u0000"+
		"-*\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000-,\u0001\u0000\u0000"+
		"\u0000.\u0003\u0001\u0000\u0000\u0000/0\u0007\u0000\u0000\u000005\u0005"+
		"!\u0000\u000012\u0005\u001f\u0000\u000024\u0005!\u0000\u000031\u0001\u0000"+
		"\u0000\u000047\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u000056\u0001"+
		"\u0000\u0000\u000068\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u0000"+
		"89\u0005 \u0000\u00009\u0005\u0001\u0000\u0000\u0000:;\u0005\u0007\u0000"+
		"\u0000;<\u0005!\u0000\u0000<=\u0005\u001a\u0000\u0000=>\u0003\u0012\t"+
		"\u0000>?\u0005 \u0000\u0000?\u0007\u0001\u0000\u0000\u0000@A\u0005!\u0000"+
		"\u0000AB\u0005\u001a\u0000\u0000BC\u0003\u0012\t\u0000CD\u0005 \u0000"+
		"\u0000D\t\u0001\u0000\u0000\u0000EF\u0005\u0006\u0000\u0000FG\u0005\u001b"+
		"\u0000\u0000GL\u0005!\u0000\u0000HI\u0005\u001f\u0000\u0000IK\u0005!\u0000"+
		"\u0000JH\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001\u0000"+
		"\u0000\u0000LM\u0001\u0000\u0000\u0000MO\u0001\u0000\u0000\u0000NL\u0001"+
		"\u0000\u0000\u0000OP\u0005\u001c\u0000\u0000PQ\u0005 \u0000\u0000Q\u000b"+
		"\u0001\u0000\u0000\u0000RS\u0005\u0005\u0000\u0000ST\u0005\u001b\u0000"+
		"\u0000TY\u0003\u0012\t\u0000UV\u0005\u001f\u0000\u0000VX\u0003\u0012\t"+
		"\u0000WU\u0001\u0000\u0000\u0000X[\u0001\u0000\u0000\u0000YW\u0001\u0000"+
		"\u0000\u0000YZ\u0001\u0000\u0000\u0000Z\\\u0001\u0000\u0000\u0000[Y\u0001"+
		"\u0000\u0000\u0000\\]\u0005\u001c\u0000\u0000]^\u0005 \u0000\u0000^\r"+
		"\u0001\u0000\u0000\u0000_`\u0005\u0002\u0000\u0000`a\u0005\u001b\u0000"+
		"\u0000ab\u0003\u0012\t\u0000bc\u0005\u001c\u0000\u0000cg\u0005\u001d\u0000"+
		"\u0000df\u0003\u0002\u0001\u0000ed\u0001\u0000\u0000\u0000fi\u0001\u0000"+
		"\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hj\u0001"+
		"\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000jt\u0005\u001e\u0000\u0000"+
		"kl\u0005\u0003\u0000\u0000lp\u0005\u001d\u0000\u0000mo\u0003\u0002\u0001"+
		"\u0000nm\u0001\u0000\u0000\u0000or\u0001\u0000\u0000\u0000pn\u0001\u0000"+
		"\u0000\u0000pq\u0001\u0000\u0000\u0000qs\u0001\u0000\u0000\u0000rp\u0001"+
		"\u0000\u0000\u0000su\u0005\u001e\u0000\u0000tk\u0001\u0000\u0000\u0000"+
		"tu\u0001\u0000\u0000\u0000u\u000f\u0001\u0000\u0000\u0000vw\u0005\u0004"+
		"\u0000\u0000wx\u0005\u001b\u0000\u0000xy\u0003\u0012\t\u0000yz\u0005\u001c"+
		"\u0000\u0000z~\u0005\u001d\u0000\u0000{}\u0003\u0002\u0001\u0000|{\u0001"+
		"\u0000\u0000\u0000}\u0080\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000"+
		"\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0083\u0001\u0000\u0000\u0000"+
		"\u0080~\u0001\u0000\u0000\u0000\u0081\u0082\u0005\u000e\u0000\u0000\u0082"+
		"\u0084\u0005 \u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0084"+
		"\u0001\u0000\u0000\u0000\u0084\u0088\u0001\u0000\u0000\u0000\u0085\u0087"+
		"\u0003\u0002\u0001\u0000\u0086\u0085\u0001\u0000\u0000\u0000\u0087\u008a"+
		"\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0088\u0089"+
		"\u0001\u0000\u0000\u0000\u0089\u008b\u0001\u0000\u0000\u0000\u008a\u0088"+
		"\u0001\u0000\u0000\u0000\u008b\u008c\u0005\u001e\u0000\u0000\u008c\u0011"+
		"\u0001\u0000\u0000\u0000\u008d\u0092\u0003\u0014\n\u0000\u008e\u008f\u0007"+
		"\u0001\u0000\u0000\u008f\u0091\u0003\u0014\n\u0000\u0090\u008e\u0001\u0000"+
		"\u0000\u0000\u0091\u0094\u0001\u0000\u0000\u0000\u0092\u0090\u0001\u0000"+
		"\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0013\u0001\u0000"+
		"\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0095\u009a\u0003\u0016"+
		"\u000b\u0000\u0096\u0097\u0007\u0002\u0000\u0000\u0097\u0099\u0003\u0016"+
		"\u000b\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0099\u009c\u0001\u0000"+
		"\u0000\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009a\u009b\u0001\u0000"+
		"\u0000\u0000\u009b\u0015\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000"+
		"\u0000\u0000\u009d\u00ac\u0005!\u0000\u0000\u009e\u00ac\u0005\"\u0000"+
		"\u0000\u009f\u00ac\u0005#\u0000\u0000\u00a0\u00ac\u0005$\u0000\u0000\u00a1"+
		"\u00ac\u0005\f\u0000\u0000\u00a2\u00ac\u0005\r\u0000\u0000\u00a3\u00a4"+
		"\u0005\u001b\u0000\u0000\u00a4\u00a5\u0003\u0012\t\u0000\u00a5\u00a6\u0005"+
		"\u001c\u0000\u0000\u00a6\u00ac\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005"+
		"\u0019\u0000\u0000\u00a8\u00ac\u0003\u0016\u000b\u0000\u00a9\u00aa\u0005"+
		"\u0010\u0000\u0000\u00aa\u00ac\u0003\u0016\u000b\u0000\u00ab\u009d\u0001"+
		"\u0000\u0000\u0000\u00ab\u009e\u0001\u0000\u0000\u0000\u00ab\u009f\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a0\u0001\u0000\u0000\u0000\u00ab\u00a1\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a2\u0001\u0000\u0000\u0000\u00ab\u00a3\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a7\u0001\u0000\u0000\u0000\u00ab\u00a9\u0001"+
		"\u0000\u0000\u0000\u00ac\u0017\u0001\u0000\u0000\u0000\u00ad\u00ae\u0003"+
		"\u0012\t\u0000\u00ae\u00af\u0007\u0003\u0000\u0000\u00af\u00b0\u0003\u0012"+
		"\t\u0000\u00b0\u0019\u0001\u0000\u0000\u0000\u000e -5LYgpt~\u0083\u0088"+
		"\u0092\u009a\u00ab";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}