from time import perf_counter,time,sleep

def doubles(number):
    for n in number:
        sleep(1)
        print('Double:',2*n)

def squares(number):
    for n in number:
        sleep(1)
        print('Square:',n**2)

numbers = [1,2,3,4,5,6]

begintime = perf_counter()

doubles(numbers)
squares(numbers)

endtime = perf_counter()

print('The total time taken:',endtime-begintime)