glossary = {
    'variables': 'a variable is a container (storage area) to hold data.',
    'loop': 'loops are used to repeat a block of code.',
    'list': 'lists are used to store multiple data at once.',
    'comment': 'comments is to make our code more understandable and are ignored by the interpreters, meant for fellow programmers.',
    'operators': "special symbols that perform operations on vari.ables and values.",
     'value': 'A value is one of the basic things a program works with, like a letter or a number. You can print values in Python.',
     'If statement': 'we use the if statement to run a block code only when a certain condition is met.',
    'string': 'a string is a sequence of characters, we use single quotes or double quotes to represent a string in Python',
    'float': 'float is a numerical data type that represents a floating-point number. A floating-point number is a number with a decimal point or exponent notation.',
    'boolean expression': 'When you compare two values, the expression is evaluated and Python returns the Boolean answer, True or False',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")

# I add five more Python terms to the glossary and automatically included in the output.