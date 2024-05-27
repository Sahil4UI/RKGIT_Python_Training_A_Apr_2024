import csv
with open("xyz.csv","r") as file:
    # reader = csv.DictReader(file)
    reader = csv.reader(file)
    
    for i in reader:
        print(i)