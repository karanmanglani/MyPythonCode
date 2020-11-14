# Add upto n
import time

start_time = time.time()

n = int(input("Enter a number : "))
def addUpto(n):
    return n * (n + 1) / 2
print(addUpto(n))
print("Time for execution is {0} miliseconds".format(time.time() - start_time))