import argparse

# Create argument parser class object
parser = argparse.ArgumentParser(description='This program displays square of a given number')

# add argument of type int and name num
parser.add_argument("num",type=int , help="Please input an integer")

# Retrieving argument
args = parser.parse_args()
result = args.num**2;
print("Square value = ", result)
