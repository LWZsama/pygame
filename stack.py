class stack():
    def __init__(self):
        self.data = []
    
    def push(self,item):
        self.data.append(item)

    def pop(self):
        x = self.data.pop()
        return x
    
    def size(self):
        return len(self.data)
s1 = stack()

myString = str(input("Please enter a word or phrase to be tested:"))
for i in range(0,len(myString)):
    s1.push(myString[i])

a=""
t = s1.size()
for i in range(0,t):
    a += s1.pop()

if a == myString:
    print("true")
else:
    print("false")


