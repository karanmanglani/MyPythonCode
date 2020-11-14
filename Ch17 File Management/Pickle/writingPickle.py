import employee as e 
import pickle

reclen = 45
f = open('emp.dat','wb')
n = int(input("Enter number of employee : "))

for i in range(n):
    print("###################Employee number ",i,"####################")
    id = int(input("Enter ID : "))
    name = input("Enter Name : ")
    name += (reclen-(len(name)))*' '
    sal = int(input("Enter Salary : "))
    emp = e.Emp(id,name,sal)
    pickle.dump(emp,f)

f.close()

#! str.encode() string to byte
#! str.decode() get's string from byte