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
    : PROGRAM IDENTIFIER LBRACE stmt* RBRACE EOF
    ;

stmt
    : declaration
    | assignment
    | constDeclaration
    | inputStmt
    | printStmt
    | ifStmt
    | whileStmt
    ;

declaration
    : (INT_TYPE | FLOAT_TYPE | BOOL_TYPE | CHAR_TYPE) IDENTIFIER (COMMA IDENTIFIER)* SEMICOLON
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
    : 'if' '(' expression ')' '{' stmt* '}' ('else' '{' stmt* '}')?
    ;

whileStmt
    : WHILE LPAREN expression RPAREN LBRACE stmt* (BREAK SEMICOLON)? stmt* RBRACE
    ;

expression
    : term (( '+' | '-' | '>' | '<' | '>=' | '<=' | '==' | '!=' ) term)*
    ;

term
    : factor ((MUL | DIV) factor)*
    ;

factor
    : IDENTIFIER
    | NUMBER
    | CHAR_LITERAL
    | STRING_LITERAL
    | TRUE
    | FALSE
    | LPAREN expression RPAREN
    | NOT factor
    | SUB factor
    ;

comparison
    : expression (EQ | NEQ | GE | LE | GT | LT) expression
    ;

