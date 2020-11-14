def sumRange(num):
    try:
        if(num == 1): return 1
        return num + sumRange(num - 1)
    except RecursionError:
        print("Undefined")
        return -499499
print(sumRange(999))
