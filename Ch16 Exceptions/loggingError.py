import logging

logging.basicConfig(filename='log.txt' , level = logging.ERROR)
try:
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    c = a/b

except Exception as e:
    logging.exception(e)

else:
    print("The result of division is : ",c)