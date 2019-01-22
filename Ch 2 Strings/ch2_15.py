# interpolating variables in strings
print("{} has a {} that is {} years old ".format("david", "world", 3700))


name = 'David'
object = "ball"
age = 35
text = "{name} has a {object} that is {age} years old "

print(text.format_map(vars()))
