# managing memory in cyclic data structures
# Cyclic data structures are a somewhat tricky aspect of Python that require careful study
# because the usual rules of garbage collection often don’t apply.
# Python’s garbage collection is based on simple reference count‐
# ing. When the reference count of an object reaches 0, it is immediately deleted. For
# cyclic data structures, however, this never happens. Thus, in the last part of the example,
# the parent and child nodes refer to each other, keeping the reference count nonzero.
# Weak references solve this problem by eliminating reference cycles. Essentially, a weak
# reference is a pointer to an object that does not increase its reference count. You create
# weak references using the weakref library.