#l = ['Good morning', 'Good afternoon', 'Good night']

#for i in l:
#    print(i)

def counter(num = 10):
    for _ in range(num):
        yield 'run'
        
print("###############")

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'
    
#for g in greeting():
#    print(g)
    
g = greeting()
c = counter()

print(next(g))
print(next(c))

print(next(g))
print(next(c))

print(next(g))
print(next(c))

print(next(g))