# ---------------------------
# CISC7120X Final Project
# Interpreter for the toy language given
#
# Run from the command line
# ex: >python toy_interpreter.py test.toy
# ---------------------------


import ply.lex as lex
import toy_lexical_tokens
from toy_syntactical_parser import *
import sys

# Create a variable for the .toy file inputted in command line
fname = sys.argv[1]

# Initialize empty lists to strip comment lines later
raw_input = []
text_input = []

# Input each line in .toy file as an entry in the list
with open(fname) as f:
    raw_input = f.readlines()

# Strip the comment lines from the .toy file, if any
# Strip blank lines in between assignments
for line in raw_input:
    if line[0:1] in ('#', '\n'):
        continue
    else:
        text_input.append(line)

# Initialize the lexer with the tokens provided
lexer = lex.lex(module=toy_lexical_tokens)

# Parse the .toy file
for line in text_input:
    parser.parse(line)

# results is a list with the variables and values obtained after parsing
results = get_results()

# Display the results as per the project specifications
for key in results:
    print("%s = %s" % (key, results[key]))
