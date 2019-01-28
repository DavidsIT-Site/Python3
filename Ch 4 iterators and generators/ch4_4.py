#  building custom objects with iteration


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


    def depth_first(self):
        yield self
        for node in self:
            yield from node.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child3 = Node(3)
    child4 = Node(4)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)
    child3.add_child(child4)

    for ch in child1:
        print(ch)
    for ch in root:
        print(ch)
    print("depth first search")
    for ch in root.depth_first():
        print(ch)
