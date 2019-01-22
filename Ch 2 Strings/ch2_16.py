# reformatting text

text = """Development; towards what?


Does empowerment come through social media evaluation and validation?   
or that 'luxury' apartment, which can never be paid off   
 
Do you operate like a minuscule cog   
A mindless rodent running in societies' gargantuan wheels   
           
Oh darling, you call thus - existence?   
           
Ignorance, Suppressed knowledge that:   
Civil wars, mass genocide, extraordinary theft are manifest   
           
Trade freedom for temporary security   
or question instigators of austerity   
           
Develop towards anything specific
"""

print(text)

import textwrap
print(textwrap.fill(text))
print(textwrap.fill(text, 40))
print(textwrap.fill(text, 70))
print(textwrap.fill(text, 40, initial_indent='       '))
print(textwrap.fill(text, 70, initial_indent='       '))
print(textwrap.fill(text, 40, subsequent_indent='       '))
print(textwrap.fill(text, 70, subsequent_indent='       '))
