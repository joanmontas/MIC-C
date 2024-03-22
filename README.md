# MIC-C
Compiler for a niche architecture.

# Grammar
    <statements> ::= statement
                 | statement statements

    <statement> ::= <TYPE> <ID> '=' <<expressionStatement> ';'                
                |   <ID> '=' <<expressionStatement> ';'                       
                |   <TYPE> <ID> ';'                                           
                |   <BLOCK>
                |   IF <LPAREN> <<expressionStatement> <RPAREN> <LCURL> <<expressionStatement> <RCURL> ';'
                |   IF <LPAREN> <<expressionStatement> <RPAREN> <LCURL> <<expressionStatement> <RCURL> ELSE <LCURL> <expressionStatement> <RCURL> ';'
                |   WHILE <LPAREN> <expressionStatement> <RPAREN> <LCURL> <<expressionStatement> <RCURL> ';'
                |   <expressionStatement> ';'

    <expressionStatement> ::= <expression> '+' <expression>
                          |   <expression> '-' <expression>
                          |   <expression> '*' <expression>
                          |   <expression> '/' <expression>
                          |   <expression> '==' <expression>
                          |   <LPAREN> <expression> <RPAREN>
                          |   '*' <expression>                                        
                          |   '-' <expression>                                        
                          |   <ID>
                          |   <TYPE>
                          |   <NUMBER>
                          |   <STRING>

    <TYPE>      ::= 'number'
                |   'string'

    <ID>        ::= [a-zA-Z_][a-zA-Z0-9_]*

    <NUMBER>    ::= \d+

    <STRING>    ::= '\'' ([^\\']+|\\')* '\''
    <BLOCK>     ::= LCURL <statements> RCURL                                
