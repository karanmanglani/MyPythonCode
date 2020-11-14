import sys
class Bank(object):
    def __init__(self,name,balance = 0.0):
        self.name = name 
        self.balance = balance
    

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Not enough balance left!!")
        
        return self.balance
    
name = input('Enter name: ')
b = Bank(name = name)

while(True):
    print('d --> Deposit , w --> withdraw , e --> exit ')
    choice = input("Your choice: ")

    if choice == 'e' or choice == 'E':
        sys.exit()
    amt = int(input("Enter amount: "))
    # do transaction
    if choice == 'd' or choice == 'D':
        print("Balance after deposit: ",b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print("Balance after withdrawl: ",b.withdraw(amt)) 