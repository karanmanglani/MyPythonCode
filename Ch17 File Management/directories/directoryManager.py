import os

print("Current Directory = ", os.getcwd())

#os.makedirs('new/new1')
os.chdir('./new')
#os.mkdir('removeMe')
#os.rmdir('removeMe')

#! Running another python program in this program

os.chdir('../../zipping')
os.system('unzip.py')