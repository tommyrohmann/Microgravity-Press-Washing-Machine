import os
from os import listdir
from os.path import isfile, join

current_dir = os.path.dirname(__file__)
print(current_dir)

 = "WashInstructions"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
#"""
