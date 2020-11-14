reclen = 30
with open("cities.bin","wb") as f:
    n = int(input("Enter number of cities : "))
    for i in range(n):
        city = input("Enter city : ")
        ln = len(city)
        city += (reclen - ln)*' '
        city = city.encode()
        f.write(city)
