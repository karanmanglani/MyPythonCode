# Add upto n
import time

start_time = time.time()

n = int(input("Enter a number : "))
def addUpto(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum 

print(addUpto(n))

print("Time for execution is {0} seconds".format(time.time() - start_time))


