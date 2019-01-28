#  depth first alternative
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []


    def __repr__(self):
        return 'Node{}'.format(self._value)


    def add_child(self, other_node):
        self._children.append(other_node)


    def __iter__(self):
        return iter(self._children)


    def depth_first(self):
        return DepthFirstIterator(self)

class DepthFirstIterator(object):
    '''
    depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None


    def __iter__(self):
        return self

    def __next__(self):
        # return myself if just started; create iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)




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


    print("depth first search")
    for ch in root.depth_first():
        print(ch)
