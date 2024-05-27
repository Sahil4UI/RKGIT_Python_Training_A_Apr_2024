#CSV - Comma Separated Values
data = [{"id":1,"name":"Rohit","sal":650000},
        {"id":2,"name":"Ram","sal":98000},
        {"id":3,"name":"Ankit","sal":15000}]
import csv
with open("xyz.csv","w",newline="") as file:
    fieldnames = ["id","name","sal"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)