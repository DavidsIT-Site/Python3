# parsing and analyzing python source

x = 42
var1 = eval('2 + 2*3 + x')
print(var1)

import ast
ex = ast.parse('2 + 2*3 + x', mode='eval')
print(ex)
print(ast.dump((ex)))