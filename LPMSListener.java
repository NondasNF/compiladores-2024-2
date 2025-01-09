// Generated from C:/Users/nonda/Downloads/TrabalhoCompiladorCompleto/Compiladores-2024-2/LPMS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LPMSParser}.
 */
public interface LPMSListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LPMSParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(LPMSParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(LPMSParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(LPMSParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(LPMSParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(LPMSParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(LPMSParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#constDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterConstDeclaration(LPMSParser.ConstDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#constDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitConstDeclaration(LPMSParser.ConstDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(LPMSParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(LPMSParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#inputStmt}.
	 * @param ctx the parse tree
	 */
	void enterInputStmt(LPMSParser.InputStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#inputStmt}.
	 * @param ctx the parse tree
	 */
	void exitInputStmt(LPMSParser.InputStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(LPMSParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(LPMSParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(LPMSParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(LPMSParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(LPMSParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(LPMSParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(LPMSParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(LPMSParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(LPMSParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(LPMSParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(LPMSParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(LPMSParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPMSParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(LPMSParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPMSParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(LPMSParser.ComparisonContext ctx);
}