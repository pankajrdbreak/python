from importlib.metadata import files
import shutil, os
files = ['files/f1.txt']
for f in files:
    shutil.copy(f, 'dest/')
