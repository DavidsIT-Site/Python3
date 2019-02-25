# making your programs run faster
A little-known fact is that code defined in the global scope like this runs slower than code defined in
a function. The speed difference has to do with the implementation of local versus global variables
(operations involving locals are faster). The speed difference depends heavily on the processing being performed, but in our experience,
speedups of 15-30% are not uncommon

Sometimes programmers get carried away with making unnecessary data structures when they just
don’t have to. For example, someone might write code like this:
values = [x for x in sequence]
squares = [x*x for x in values]
Perhaps the thinking here is to first collect a bunch of values into a list and then to start applying
operations such as list comprehensions to it. However, the first list is completely unnecessary. Simply
write the code like this:
squares = [x*x for x in sequence]