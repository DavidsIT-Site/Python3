# format text with alignment

text = "Hello world"

print(text.rjust(20, '='))
print(text.ljust(20, '='))
print(text.center(20, '='))



print("{:>20}".format("Hello worlds"))
print("{:=>20}".format("Hello worlds"))

print("{:<20}".format("Hello worlds"))
print("{:=<20}".format("Hello worlds"))

print("{:^20}".format("Hello worlds"))
print("{:=^20}".format("Hello worlds"))


print("{:>10s}\n{:*^20}".format("Hello", "world"))
x = 1.2345
print("{:10}".format(x))

print("{:^20.2f}".format(x))