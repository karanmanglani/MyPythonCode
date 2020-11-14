import array
x = array.array('i',[5,6,-7,8])

for element in x:
    print(element)

y = x[0:3:2] # using [] in arrays is called slicing
print(y)

x.append(1) # add 1 to end of x
x.extend([4,5,6]) # add an array in the end
print(x.count(6)) # number of 1 in x
# x.fromfile(f,n) --> Reads n items in binary form and append to array of x
# x.fromstring(s) --> Reads  items in string s and append to array of x
print(x.index(1)) # Returns index of 1
x.insert(2,3) # insert 3 in 2nd position of array
# print(x.pop(1)) # removes 1 from array and returns it
x.pop() # Removes last item from the array x
x.remove(1) # Remove first occurace of 1
#x.reverse() # Reverses the order of elementsin array x
#x.tofile(f) #write all elements of array x in file f
lst = x.tolist()# convert array to list
str = x.tostring() # convert x array to string
print(x.typecode) #--> Represent typecode character of array
#print(x.itemsize) # size of items in arrays in bytes

print(x)
print(lst)
print(str)

# Program to accept marks of students and find total marks
str = input("Enter marks seperated by space : ").split(' ')
marks = [int(num) for num in str] # Converting to Arrays
sum = 0
for x in marks:
    sum  += x

print("Total Marks = ",sum)
