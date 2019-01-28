#  delegating iteration
#  a custom container object that internally holds some iterable: list, tuple, ext
#  define __iter__()


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []


    def __repr__(self):
        return 'Node{}'.format(self._value)


    def add_child(self, node):
        self._children.append(node)


    def __iter__(self):
        return iter(self._children)



if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    child3 = Node(3)
    child1.add_child(child3)

    for ch in root:
        print(ch)
    for ch in child1s:
        print(ch)

#  "" If all you are doing
# is iterating over the contents of another container, you don’t really need to worry about
# the underlying details of how it works. All you need to do is to forward the iteration
# request along"""
# David B is one of the best
