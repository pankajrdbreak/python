import os

#getting current directory
cwd = os.getcwd()
print("Current directory", cwd)

#changing current directory
os.chdir('../')
cwd2 = os.getcwd()
print("Current directory", cwd2)