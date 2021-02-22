import pdb


def add_constant(x):
    return x + 10


a = 1
b = 2
c = 3

# we can use pdb here to change the values of variables, or even redefine the function
# pdb.set_trace()

a, b, c = [add_constant(x) for x in (a, b, c)]

print(f"Program result -- a: {a}, b: {b}, c: {c}")
