import shutil, os
files = ['files/f1.txt']
for f in files:
    shutil.move(f, 'dest/')