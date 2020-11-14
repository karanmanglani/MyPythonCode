# Sequence ---> Represents a group of elements or items 
# Following are the types of sequences in python :-
# str{string}
# bytes
# bytearray
# list
# tuple
# range

###### String datatype (str) - Group of characters enclosed in " " or ' ' or """ """ or '''' '''
str = "welcome"
str1 = """ 
        this is multiline
        string
       """
print(str + str1)
print(str[2:4])
print(str*2)

####### bytes datatype ---> group of bytes number[0 - 255] 
elements = [10,22,25,56,78]
x=bytes(elements)
print(x[0])
