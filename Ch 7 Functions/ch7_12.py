# accessing variables inside a closure
def sample():
    n = 0
    # closure function
    def func():
        print('n=', n)


    def get_n():
        return n


    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
print(f())

f.set_n(10)
print(f())

#pg 239/240 closure speed verses classes skipped
