import os

print("Current Directory = ", os.getcwd())

#os.makedirs('new/new1')
#os.chdir('./')
#os.mkdir('removeMe')
#os.rmdir('removeMe')

#! Running another python program in this program

os.chdir('Ch17 File Management/zipping')
os.system('unzip.py')