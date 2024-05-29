import matplotlib.pyplot as plt

data = {
        "names" : ['John','Shwan','Max','Smith','Nick','Steve'],
        "dept" : ['IT','HR','IT','HR','IT','Admin'],
        "Salary" :[56000,45000,25000,70000,55000,30000]
}
plt.figure(figsize=(8,8))
plt.pie(data['Salary'], labels=data['names'], autopct='%.2f%%', shadow=True,
        startangle=90, explode=[0,0.4,0,0,0,0])
plt.title("Salary of employees..")
plt.legend(loc = 'upper right',bbox_to_anchor=(1,1))
plt.show()
