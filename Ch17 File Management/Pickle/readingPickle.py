import employee as e 
import pickle

f = open('emp.dat','rb')

print("Employee Details : ")
while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print("End of file reached!!")
        break
f.close()
#* pickle.tell() returns the current byte position
#* pickle.seek(offset , fromwhere) moves the pointer to required position 