def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'


g = my_gen()
print(type(g))

print(next(g))
print(next(g))
print(next(g))

# if we ask again next(g) we will get StopIteration exception.


g = my_gen()

for x in g:
    print(x) 