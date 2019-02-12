# implementing the visitor pattern
# One weakness of the visitor pattern is its heavy reliance on recursion. If you try to apply
# it to a deeply nested structure, it’s possible that you will hit Python’s recursion depth
# limit

class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

t0 = Number(2)
t1 = Sub(Number(1), Number(2))
t2 = Mul(Number(2), t0)


class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
    def generic_visit(self, node):
        raise RuntimeError('{} method'.format('visit_' + type(node).__name__))

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Sdd(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.vist(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand
e = Evaluator()

result = e.visit(t0)
print(result)

result = e.visit(t2)
print(result
      )
result = e.visit(t1)
print(result)

