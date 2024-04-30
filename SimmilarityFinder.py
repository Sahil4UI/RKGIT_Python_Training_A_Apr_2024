data1 = '''Python is a programming language that is interpreted, object-oriented, and considered to be high-level too. What is Python? Python is one of the easiest yet most useful programming languages which is widely used in the software industry. People use Python for Competitive Programming, Web Development, and creating software. Due to its easiest syntax, it is recommended for beginners who are new to the software engineering field. Its demand is growing at a very rapid pace due to its vast use cases in Modern Technological fields like Data Science, Machine learning, and Automation Tasks. For many years now, it has been ranked among the top Programming languages.'''
data2 = '''Python is a computer programming language often used to build websites and software, automate tasks, and analyze data. Python is a general-purpose language, not specialized for any specific problems, and used to create various programmes. This versatility and its beginner-friendliness have made it one of the most used programming languages today. In 2020, more than one-third of Indian IT professionals said Python was their preferred programming language [2]. It continues to top lists of the most desired programming languages in the country.'''
#Step1  - Tokenization
token1 = data1.split()
token2 = data2.split()
#Remove StopWords
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
list1,list2  = [],[]
for value in token1:
    if value not in stopwords:
        list1.append(value)
for value in token2:
    if value not in stopwords:
        list2.append(value)

#convert to sets
set1,set2 = set(list1),set(list2)
num = len(set1.intersection(set2))
den = len(set1.union(set2))
print(f"%=> {num/den*100}")
