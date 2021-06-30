def first_n_values_gen(n):
    i = 1
    while i <=n:
        yield i 
        i = i+1

g = first_n_values_gen(10)

for x in g:
    print(x)