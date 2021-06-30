def fib_gen():
    a,b = 0 ,1

    while True:
        yield a
        a,b = b , a+b


g = fib_gen()

for x in g:
    if x<10:
        print(x)
    else:
        break
    