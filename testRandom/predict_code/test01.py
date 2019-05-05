
x = 3
A = 12
B = 13
M = 100
def foo():
    global x
    x = (A*x + B) % M
    return x


x_1 = 3
x_2 = 43
M = 100

def foo_2():
    global x_1
    global x_2
    x_2_tmp = (x_1 * x_2) % M
    x_1 = x_2
    x_2 =  x_2_tmp
    return x_2
# generate a sequence of random numbers in [0, 99]
def generate_sequence(length=25):
    # return [randint(0, 99) for _ in range(length)]
    return [foo_2() for _ in range(length)]

a = generate_sequence()
print(a)
a = generate_sequence()
print(a)
a = generate_sequence()
print(a)
