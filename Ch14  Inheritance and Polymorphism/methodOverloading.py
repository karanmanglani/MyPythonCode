
class Myclass:
    def sum(self, a = None, b = None , c = None):
        if a != None and b != None and c !=None:
            print(a + b + c)
        elif a != None and b != None:
            print(a + b)
        else:
            print('Please enter 2 or three arguments ')

m = Myclass()
m.sum(10,20,30)
m.sum(10,20)
m.sum(10)