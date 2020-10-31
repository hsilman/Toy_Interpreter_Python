# ---------------------------
# Syntactical Parser for the toy language
# ---------------------------

import ply.yacc as yacc

# Get the token map from the lexer
from toy_lexical_tokens import tokens

names = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTI'),
)


def get_results():
    return names


def p_assignment_expression(p):
    'assignment : ID EQUAL expression SEMICOLON'
    names[p[1]] = p[3]


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_multi(p):
    'term : term MULTI factor'
    p[0] = p[1] * p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_exp(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_factor_uminus(p):
    'factor : MINUS factor'
    p[0] = -p[2]


def p_factor_plus(p):
    'factor : PLUS factor'
    p[0] = p[2]


def p_factor_literal(p):
    'factor : LITERAL'
    p[0] = p[1]


def p_factor_id(p):
    'factor : ID'
    try:
        p[0] = names[p[1]]
    except LookupError:
        p[0] = 0


# Error rule
def p_error(p):
    print("error")
    exit(1)


# Build parser
parser = yacc.yacc()
