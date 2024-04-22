import pandas as pd

data = [{"id":101,"name":"Rahul","p":90,"c":10,"m":56},
        {"id":102,"name":"Ram","p":100,"c":100,"m":96},
        {"id":103,"name":"Lokesh","p":90,"c":100,"m":60},
        {"id":104,"name":"Ankit","p":20,"c":10,"m":5},
        {"id":105,"name":"Rahul","p":50,"c":50,"m":50},]

# print id along with name
#find average & grade for each student
for i in range(len(data)):
    avg = (data[i]["p"]+data[i]["c"]+data[i]["m"])//3
    grade = None
    if avg>80:
        grade = "A"
    elif avg>60:
        grade = "B"
    elif avg > 50:
        grade = "C"
    elif avg > 33:
        grade = "D"
    else:
        grade = "F"
    data[i]["avg"] = avg
    data[i]["grade"] = grade
    # print(data[i]["id"],data[i]["name"],avg,grade)
df = pd.DataFrame(data)
print(df)