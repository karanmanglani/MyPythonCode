reclen = 30

with open("cities.bin","rb") as f:
    n = int(input("Enter record number : "))
    #! move the file pointer to n-1th record
    f.seek(reclen * (n - 1))
    str = f.read(reclen)
    print(str.decode())