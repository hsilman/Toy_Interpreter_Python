# --------------------------------
# module: toy_lexical_tokens.py
#
# tokens for toy language
# --------------------------------

from ply.lex import TOKEN

# List of token names
tokens = (
    'PLUS',
    'MINUS',
    'MULTI',
    'EQUAL',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'ID',
    'LITERAL'
)

# Simple token regex
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_EQUAL = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r'\;'
t_ID = r'([A-Za-z_]([A-Za-z_]|[0-9])*)'

# More complex literal token
literal = r'(0|([1-9]([0-9]*)))'


@TOKEN(literal)
def t_LITERAL(t):
    t.value = int(t.value)
    return t


# Ignore whitespace and newline tokens
t_ignore = ' \n'


# Error handling
def t_error(t):
    print("error")
    t.lexer.skip(1)
