# We use docstrings to create API{Application Programming Interface}
# In python function should start with def keyword

def add(x,y):
    """
        This function takes two numbers and find their sum
        It displays the sum as result.
    """
    print("Sum = ",(x+y))

def message():
    '''
    This function displays a welcome message.
    '''
    print("Welcome to python")

#now calling function
add(10,25)
message()

#use command "python -m pydoc -w <programName>" to render API file