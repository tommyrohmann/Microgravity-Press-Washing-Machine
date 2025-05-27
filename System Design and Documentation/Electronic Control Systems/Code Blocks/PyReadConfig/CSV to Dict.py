import csv
 
# csv fileused id Geeks.csv
filename="Test.csv"

# opening the file using "with"
# statement
with open(filename,'r') as data:
   for line in csv.reader(data):
            print(line)