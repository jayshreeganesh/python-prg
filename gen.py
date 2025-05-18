def my_gen():
    yield 1
    yield 2
    yield 4

x = my_gen()
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())

def my_gen(n):
    a = 0
    while a < n:
        if a%2 == 0:
            yield a
        a += 1

x = my_gen(15)
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())

for i in (x):
    print(i)

x = my_gen(15)
print(next(x))    

def fibo(n):
    a,b = 0,1
    while a < n:
        yield a
        a,b = b,a+b

x = fibo(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())

x = fibo(10)
for i in x:
    print(i)