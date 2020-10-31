# Toy_Interpreter_Python
Toy Language Interpreter built in Python using the [PLY](https://www.dabeaz.com/ply/)
</br>
</br>
Run on the command line as:</br>
>python toy_interpreter.py filename</br>

The file must be in the same directory as toy_interpreter.py</br>
By convention, I titled my files *.toy

*Program only outputs 'error' per given specifications. I would have it give a more detailed error message.*
</br>
</br>
## Toy Language Grammar

Program:</br>
* Assignment*

Assignment:
* Identifier = Exp;

Exp: 
* Exp + Term | Exp - Term | Term

Term:
* Term * Fact  | Fact

Fact:
* ( Exp ) | - Fact | + Fact | Literal | Identifier

Identifier:
* Letter [Letter | Digit]*

Letter:
* a|...|z|A|...|Z|_

Literal:
* 0 | NonZeroDigit Digit*
		
NonZeroDigit:
* 1|...|9

Digit:
* 0|1|...|9
</br>
</br>

## Example inputs and outputs

Input 1

x = 001;

Output 1

error

--

Input 2

x_2 = 0;

Output 2

x_2 = 0

--

Input 3

x = 0

y = x;

z = ---(x+y);

Output 3

error

--

Input 4

x = 1;

y = 2;

z = ---(x+y)*(x+-y);

Output 4

x = 1

y = 2

z = 3
