import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(values)
print(random.sample(values, 3))
print(values)
random.shuffle(values)
print(values)

print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())



print(random.getrandbits(500))


#  Functions in random() should not be used in programs related to cryptography. If you need such functionality, consider using functions in the ssl module instead. For example, ssl.RAND_bytes() can be used to generate a cryptographically secure sequence of random bytes.