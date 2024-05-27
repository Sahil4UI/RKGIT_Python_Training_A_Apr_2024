#CSV - Comma Separated Values
data = [["id","name","salary"],
        [1,"Rohit",650000],
        [2,"Ram",98000],
        [3,"Ankit",15000]]
import csv
with open("xyz.csv","w",newline="") as file:
    writer=csv.writer(file)
    # for row in data:
    #     writer.writerow(row)
    writer.writerows(data)