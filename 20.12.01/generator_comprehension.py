def g():
    for i in range(10):
        yield i 

g = g()
print(type(g))

g = (i for i in range(10) if i % 2 == 0)
print(type(g))

for x in g:
    print(x)