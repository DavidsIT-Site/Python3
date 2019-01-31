# attaching informational metadata to functional arguments

# any type of object can be an instance
def add(x: int, y: int) -> int:
    return x + y

print(add(1,2))
print(add.__annotations__)
