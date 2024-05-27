#CSV - Comma Separated Values
data = [{"id":1,"name":"Rohit","sal":650000},
        {"id":2,"name":"Ram","sal":98000},
        {"id":3,"name":"Ankit","sal":15000}]
import csv
with open("xyz.csv","w",newline="") as file:
    writer=csv.writer(file)
    for row in data:
        writer.writerow([row["id"],row["name"],row["sal"]])