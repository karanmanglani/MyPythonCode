# Fibonacci Series

n = int(input("How many number of fibonacci you want : "))
f1 = 0
f2 = 1
f = f1 + f2
c = 2
if n == 1:
    print(f1, '\n')
elif n == 2:
    print(f1 , '\n' , f2, sep='')
else:
    print(f1 , '\n' , f2, sep='')
    while c < n:
        f1 , f2 = f2 , f
        f = f1 + f2
        print(f)
        c += 1
import math
# Sine Value

x,n = [int(i) for i in input("Enter Angle in degrees and number of iterations(seperated by commas) : ").split(',')]
r = (x * math.pi) / 180
t = r
sum = r
print("Iteraton = %d\t Sine of Angle = %f" % (1 , sum))
i = 2

for j in range (2 , n + 1):
    t = (-1) * t * (r** 2)/(i * (i + 1))
    sum = sum + t
    print('Iteration = %d\t Sine of Angle = %f'%(j, sum))
    i += 2

# Cosine Series

t = 1
sum = 1
i = 1
print('Iteration = %d\t Cosine of angle = %f' % (1 , sum))
for j in range (2 , n + 1):
    t = (-1) * t * r**2 / (i*(i + 1))
    sum = sum + t
    print('Iteration = %d\t Cosine of angle = %f' % (j , sum))
    i += 2

# exponential function
x , n = [int(i) for i in input("Enter value of x and number of iterations: ").split(',')]

t = 1
sum = 1
print('Iteration = %d\t e ^ x = %f'%(1, sum))

for j in range (2 , n + 1):
    t = t * x / j
    sum += t
    print('Iteration = %d\t e ^ x = %f'%(j, sum))