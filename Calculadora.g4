grammar Calculadora;

programa  : expressao+ EOF ;
expressao : atribuicao | operacao ;
atribuicao: ID '=' expressao ;
operacao  : termo (('+' | '-') termo)* ;

termo     : INT | ID ;
ID        : [a-zA-Z]+ ;
INT       : [0-9]+ ;
WS        : [ \t\r\n]+ -> skip ;