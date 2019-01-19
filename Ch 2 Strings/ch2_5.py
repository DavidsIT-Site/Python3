# searching and replacing text
text0 = "yeah, but no, but yeah, but no, but yeah"
text1 = "Today is 11/27/2012. Yesterday was: 1/18/2019"
text0_ = text0.replace('yeah', 'yep')

print(text0_)


import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text1_ = datepat.sub(r'\3 - \1 - \2', text1)
print(text1_)

