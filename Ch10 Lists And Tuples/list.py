## List ---> Similar to arrays but can store values of different datatype

list = range(1,10,3) # Creating list using Range()

for i in list:
    print(i,end = ' ')

#######! Aiasing and Cloning
#* Aliasing
x = [10,20,30] * 2
y = x 
print("Beforee Modification :-")
print(y)
print(x)

y[0] = 99
print("After Modification  of y :- ")
print(y)
print(x)

print("This is Aliasing!!")

#* Cloning
x = [10,20,30] * 2
y = x[:] # Cloning
print("Beforee Modification :-")
print(y)
print(x)

y[0] = 99
print("After Modification  of y :- ")
print(y)
print(x)

print("This is Cloning!!")

####! Finding Maximum and Minimum
list = [10,20,11,43,3,24]
n = len(list)
big = list[0]
small = list[0]

for i in range(1,n):
    if list[i] > big: big = list[i]
    if list[i] < small: small = list[i]

print("maximum = ",big," smallest = ",small)

######################! Bubble Sort !######################
list = [int(i) for i in input("Enter values to be sorted seperated by space: ").split(" ")]

def bubbleSort(list):
    n = len(list)
    flag = False
    for i in range(n-1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j] += list[j + 1]
                list[j + 1] = list[j] - list[j+1]
                list[j] -=  list[j + 1]
                flag = True
        if flag == False:
            break
        else:
            flag = False

bubbleSort(list)
print(list)

#! Finding common elements
x = set([1,2,3,45])
y = set([3,4,5,67])

z = x.intersection(y)
print(z)

z = x.union(y)
print(z)

