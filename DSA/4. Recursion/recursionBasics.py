
def countDown(num):
    if num <= 0:
        print('All Done')
        return None
    print(num)
    num -= 1
    countDown(num)

countDown(int(input('Enter a number : ')))

def sumRange(num):
    if num == 1:
        return 1
    return num + sumRange(num-1)

print(sumRange(int(input('Enter a Number : '))))