def power(num , x):
    try:        
        if(x <= 1):
            return num
        return num * power(num , x - 1)
    except RecursionError:
        print("Not able to calculate ")
        return None
print(power(5,2))