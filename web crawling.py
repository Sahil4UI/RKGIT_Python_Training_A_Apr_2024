import urllib.request as url
import bs4
home = "https://www.flipkart.com"
pname = input("Enter Product Name : ").replace(" ","+")
path = "https://www.flipkart.com/search?q="+pname
res = url.urlopen(path)
data = bs4.BeautifulSoup(res,'lxml')

path=home+data.find("a",class_="_1fQZEK")['href']
res = url.urlopen(path)
data = bs4.BeautifulSoup(res,'lxml')
print("Name : ",data.find("span",class_="B_NuCI").text)
print("Price : ",data.find("div",class_="_30jeq3 _16Jk6d").text)
div = data.find("div",class_="_2418kt")
li=div.findAll("li")
print("***********Highlights************")
for i in range(len(li)):
    print(i+1,". ",li[i].text)
