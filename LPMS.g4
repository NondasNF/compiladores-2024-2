grammar LPMS;

// Regras Léxicas
PROGRAM : 'Program';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
PRINT : 'print';
INPUT : 'input';
CONST : 'const';
INT_TYPE : 'int';
FLOAT_TYPE : 'float';
BOOL_TYPE : 'bool';
CHAR_TYPE : 'str';
RETURN : 'return';
TRUE : 'true';
FALSE : 'false';
BREAK : 'break';

ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
EQ : '==';
NEQ : '!=';
GE : '>=';
LE : '<=';
GT : '>';
LT : '<';
NOT : '!';
ASSIGN : '=';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
COMMA : ',';
SEMICOLON : ';';

IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]*;
NUMBER : [0-9]+ ('.' [0-9]+)?;
CHAR_LITERAL : '\'' .*? '\'';
STRING_LITERAL : '"' .*? '"';

WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;

// Regras Sintáticas
program
    : PROGRAM IDENTIFIER LBRACE block RBRACE EOF
    ;

block
    : stmt*
    ;

stmt
    : declaration
    | constDeclaration
    | assignment
    | inputStmt
    | printStmt
    | ifStmt
    | whileStmt
    | functionDecl
    | functionCall SEMICOLON
    | returnStmt
    | BREAK SEMICOLON
    ;

declaration
    : (INT_TYPE | FLOAT_TYPE | BOOL_TYPE | CHAR_TYPE) IDENTIFIER (ASSIGN expression)? (COMMA IDENTIFIER (ASSIGN expression)?)* SEMICOLON
    ;

constDeclaration
    : CONST IDENTIFIER ASSIGN expression SEMICOLON
    ;

assignment
    : IDENTIFIER ASSIGN expression SEMICOLON
    ;

inputStmt
    : INPUT LPAREN IDENTIFIER (COMMA IDENTIFIER)* RPAREN SEMICOLON
    ;

printStmt
    : PRINT LPAREN expression (COMMA expression)* RPAREN SEMICOLON
    ;

ifStmt
    : IF LPAREN expression RPAREN LBRACE block RBRACE (ELSE LBRACE block RBRACE)?
    ;

whileStmt
    : WHILE LPAREN expression RPAREN LBRACE block RBRACE
    ;

functionDecl
    : (INT_TYPE | FLOAT_TYPE | BOOL_TYPE | CHAR_TYPE) IDENTIFIER LPAREN parameters? RPAREN LBRACE block returnStmt? RBRACE
    ;

parameters
    : parameter (COMMA parameter)*
    ;

parameter
    : (INT_TYPE | FLOAT_TYPE | BOOL_TYPE | CHAR_TYPE) IDENTIFIER
    ;

functionCall
    : IDENTIFIER LPAREN arguments? RPAREN
    ;

arguments
    : expression (COMMA expression)*
    ;

returnStmt
    : RETURN expression SEMICOLON
    ;

expression
    : term ((ADD | SUB | GT | LT | GE | LE | EQ | NEQ) term)*
    ;

term
    : factor ((MUL | DIV) factor)*
    ;

factor
    : IDENTIFIER
    | functionCall
    | NUMBER
    | CHAR_LITERAL
    | STRING_LITERAL
    | TRUE
    | FALSE
    | LPAREN expression RPAREN
    | NOT factor
    | SUB factor
    ;

