// Generated from C:/Users/nonda/Downloads/TrabalhoCompiladorCompleto/Compiladores-2024-2/LPMS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link LPMSParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface LPMSVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link LPMSParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(LPMSParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(LPMSParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStmt(LPMSParser.StmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration(LPMSParser.DeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#constDeclaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstDeclaration(LPMSParser.ConstDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(LPMSParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#inputStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInputStmt(LPMSParser.InputStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#printStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrintStmt(LPMSParser.PrintStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#ifStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStmt(LPMSParser.IfStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#whileStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStmt(LPMSParser.WhileStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#functionDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDecl(LPMSParser.FunctionDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#parameters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameters(LPMSParser.ParametersContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter(LPMSParser.ParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionCall(LPMSParser.FunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#arguments}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArguments(LPMSParser.ArgumentsContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#returnStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStmt(LPMSParser.ReturnStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(LPMSParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(LPMSParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link LPMSParser#factor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactor(LPMSParser.FactorContext ctx);
}