#for a in range(100,1000):
#    b=a//100
  #  c=(a-b*100)//10
   # d=(a-b*100-c*10)
    #e=b**3+c**3+d**3
    #if(e==a):
     #   print(a)
#a=int(input())
#for b in range(1,a+1):
#    if(a%b==0):
#        print(b)
#for x in range(1,1001):
#    c=0
#    for b in range(1,1001):
#        if(x%b==0):
#            c+=1
#    if(c==2):
#        print(x)
#for a in range(1,1001):
#    sum=0
#    for b in range(1,1000):
#        if(a%b==0):
#            sum=sum+b
#            if(sum==a):
#                print(a)
#n=int(input())
#def fibo(n):
#  last1=1
#  last2=1
#  for b in range(1,n-1):
#    result=last1+last2
#    last1=last2
#    last2=result
#  return result
#print(fibo(n))
#n=int(input())
#x=n
#b=""
#while(x>=2):
#  a=x%2
#  x=x//2
#  b=b+str(a)
#c=b+str(x)
#print(c[::-1])
#a="abcdefgh"
#print(a[6::-6])
#a=str(input())
#b=a[::-1]
#if(b==a):
#  print("yes")
#else:
#  print("no")
#def untitled(a,b):
#  x=-1
#  while(x!=0):
#    x=a%b
#    a=b
#    b=x
#  return a
#a=int(input())
#b=int(input())
#print(untitled(a,b))
#def fibo(n):
#  if(n==1 or n==2):
#    return 1
#  else:
#    return fibo(n-1)+fibo(n-2)
#n=int(input())
#print(fibo(n))
#def fac(n):
#  if(n==1):
#    return 1
#  else:
#    return n*fac(n-1)
#n=int(input())
#print(fac(n))
#def dec(n):
#  if(n==1):
#    return 1
#  elif(n%2==0):
#    return str(dec(n//2))+"0"
#  else:
#    return str(dec(n//2))+"1"
#n=int(input())
#print(dec(n))


#dict={"a":"true"}
#print(id(dict))
#dict["b"]="false"
#print(id(dict))

#for a in ranglobale(2,2000):
#  sum=0
#  for b in range(2,a):
#    if b%a==0:
#      sum=sum+b
#  if sum==a:
#    print(a)
# <string>[start:stop:step]
# start:从0开始
# stop:终止位置取不到
# step：默认是1
#[:stop:step] 从头开始
#[start::step]切到结尾
#[::step]从头切到尾
#[index]
#[:]
#<string>.upper()全大写
#<string>.lower()全小写
#<string>.title()首字母大写
#<string>.capitalize()字符串的首字母大写
#a="shit shit"
#print(id(a))
#a=a.upper()
#print(id(a))
#<string>.isdigit()判断是否为数字字符串
#<string>.isalpha()判断是否为字母字符串
#a="12a"
#print(a.isdigit())
#print(a.isalpha())
#print(a.isalnum())
#a="shit"
#print(a.count("i"))
#<string>.count(<substring>,start,stop)
#"a"+"b"="ab"
#a=input()
#a=a.upper()
#sum=""
#for x in a:
#  if x.isalpha()==True or x.isdigit()==True:
#    sum=sum+x
#if (sum==sum[::-1]):
#  print("true")
#else:
#  print("false")
#<list>.append(<element>)
#<list>.insert(<element>,<index>)
#<list>.extend(<
#print(id(a))list>)
#a=[1,2,3]
#b=[4,5,6]
#a.append(b)
#print(id(a))
#<list>.remove(<element>)
#<list>.pop(<index>)
#<list>.clear()    
#a=[3,3,3,5,5,5]
#a.remove(3)
#print(a)
#for i in range(0,6):
#  a.remove(3)
#for i in range(0,6):
#  if (a[i]==3)
#    a.pop(i)

'''def removeElement(a,b):
    c=a.count(b)
    for i in range(0,c):
        a.remove(b)

a=[1,2,3,4,4,4,4]
b=int(input())
removeElement(a,b)
print(a)'''

'''def removeElement(a,b):
    while (a.count(b)>=1):
      for i in range(0,len(a)):
        if a[i]==b:
          a.pop(i)
          break
a=[1,2,3,4,4,4,4]
b=int(input())
removeElement(a,b)
print(a)'''

#d={"name":"",}字典无序

'''d={"age":99,"name":"shit"}
print(d["age"])'''

#<dict>[key]=<new value>

#iteration迭代 iter(<dict>)

#for x in iter(d):

'''d={"name":"shit","age":99,"sex":"helicopter"}
for x in iter(d):
    print(d[x])'''

#del <dict>[<key>]

'''d={"name":"shit","age":99,"sex":"helicopter"}
del d["name"]
print(d)'''

#sorted(key/value)

'''d={"lwz":"100","abc":"99","shit":"00"}
print(d)

for x in sorted(d.values()):
    print(x)'''

'''d={}
def addInfo(d):
  for i in range(0,5):
    a=input()
    b=int(input())
    d[a]=b
    print("next")
addInfo(d)
for x in sorted(d.values()):
  print(x)'''

#class <id>():

'''
class Rectangle():
  #attribute: lenth,width
  #method: getPerimeter(), getArea()
'''

'''
class Rectangle():
  def __init__ (self,length,width):
    self.length=length
    self.width=width

  def getPerimeter(self):
    return 2*(self.lenth+self.width)
  
  def getArea(self):
    return self.length*self.width
'''
'''
class Cat():
    def __init__ (self,name,age,sex,isSter=False):
        self.name=name
        self.age=age
        self.sex=sex
        self.isSter=isSter

    def pee():
        print(self.name+" is peeing")

    def sterilize():
        self.isSter=True
'''
'''
r=Rectange(4,3)
<object>=<calling the constructor>
'''
'''
class Cat():
    def __init__ (self,name,age,sex,isSter=False):
        self.name=name
        self.age=age
        self.sex=sex
        self.isSter=isSter

    def pee(self):
        print(self.name+" is peeing")

    def sterilize(self):
        self.isSter=True

c=Cat("shit",1,"male")
c.pee()
'''
'''
class Rectangle():
  def __init__ (self,length,width):
    self.length=length
    self.width=width

  def getPerimeter(self):
    return 2*(self.lenth+self.width)
  
  def getArea(self):
    return self.length*self.width

r=Rectangle(5,3)
print(r.getArea())
'''
'''
class Point():
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    
    def getX(self):
        return(self.x)
    
    def getY(self):
        return(self.y)

    def getGradient(self):
        return(self.y/self.x)
      
    def getDistanceOrigin(self):
        return((self.x**2+self.y**2)**0.5)
    
    def getLine(self,k):
        return("y"+"-"+str(self.y)+"="+str(k)+"(x-"+str(self.x)+")")

    def getDistanceAnother(self,P):
        return(((self.x-P.getX())**2+(self.y-P.getY())**2)**0.5)

class GongXian():
    def __init__ (self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def getAB(self):
        return((self.a.getY()-self.b.getY())/(self.a.getX()-self.b.getX()))
    
    def getAC(self):
        return((self.a.getY()-self.c.getY())/(self.a.getX()-self.c.getX()))
    
    def getBC(self):
        return((self.b.getY()-self.c.getY())/(self.b.getX()-self.c.getX()))
    
    def judge(self):
        if self.getAB()==self.getAC()==self.getBC():
            return("Yes")
        else:
            return("No")
g=GongXian(Point(1,1),Point(2,3),Point(3,3))
print(g.judge())       
'''
'''
class Dog():
    def __init__ (self,name,medal):
        self.name=name
        self.medal=medal

    def getName(self):
        return(self.name)
    
    def getMedal(self):
        return(self.medal)
    
class DogFamily():
    def __init__ (self,a):
        self.a=a

    def add(self,dog):
        self.a.append(dog)

    def findDog(self):
        print("input the name of the dog you are looking for")
        c=input()
        e=len(self.a)
        for y in range(0,e):
            if c==self.a[y].name:
                print(self.a[y].medal)

    def champion(self):
        e=len(self.a)
        g=self.a[0].medal
        for y in range(0,e):
            if self.a[y].medal>g:
                g=self.a[y].medal
        for y in range(0,e):
            if g==self.a[y].medal:
                print(self.a[y].name)

    def battle(self):
        print("input the name you want to battle")
        k=input()
        print("input he medals")
        l=int(input())
        e=len(self.a)
        g=self.a[0].medal
        for y in range(0,e):
            if self.a[y].medal>g:
                g=self.a[y].medal
        if l>g:
            d.add(Dog(k,l))
            print("success")
        else:
            print("fail")
d=DogFamily([])
print("input nums")
t=int(input())
for i in range(0,t):
    print("input name"+" "+str(i+1))
    n=input()
    print("input medal"+" "+str(i+1))
    m=int(input())
    d.add(Dog(n,m))
d.battle()
'''

'''
class Square():
    def __init__(self,a):
        self.a=a

    def shit(self,bullshit):
        x=[]
        num=len(self.a)
        for i in range(0,num):
            damn=self.a[i]
            goddamn=damn[bullshit]
            x.append(goddamn)
        return x
    
    def shitty(self,pig):
        gig=len(pig)
        for u in range(0,gig):
            re=pig.count(pig[u])
            if re!=1:
                return True
        return False

    def isAppear(self,l1,l2):
        gan=len(l1)
        for yu in range(0,gan):
            for xu in range(0,gan):
                if l2.count(l1[yu])==0:
                    return False
        return True
                
    def isMagic(self,ll1):
        ji=len(ll1)
        li1=ll1[0]
        if self.shitty(li1)==True: 
            return False
        for ki in range(0,ji):        
            if self.isAppear(li1,ll1[ki])==False:
                return False
        for ki in range(0,ki):  
            if self.isAppear(li1,self.shit(ki))==False:
                return False
        return True     

s=Square([[1,2],[2,2]])
print(s.isMagic([[1,2],[2,2]]))
'''
'''
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getOlder(self):
        self.age+=1
    
    def changeName(self,newName):
        self.name=newName

#student class is a subclass of person子类
#person is a superclass of student父类
'''
'''
子类的构造函数
*在父类构造完成的基础在进行构造
def __init__ (self,name,age,score)
    super().__init__(name,age)
'''
'''
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score

    def changeScore(self,inputScore):
        a,b,c=map(int,inputScore.split())
        self.score.append(a)
        self.score.append(b)
        self.score.append(c)
        print(self.score)

s=Student("Trump",2024,[])
s.changeScore("1 2 3")
'''

'''
class Regular():
    def __init__(self,sidelength):
        self.sidelength=sidelength

class Square(Regular):
    def __init__(self,sidelength):
        super().__init__(sidelength)

    def getPeri(self):
        return self.sidelength*4

    def getArea(self):
        return self.sidelength**2

class Triangle(Regular):
    def __init__(self,sidelength):
        super().__init__(sidelength)

    def getPeri(self):
        return self.sidelength*3
    
    def getArea(self):
        return self.sidelength*0.5*(3**0.5)*self.sidelength*0.5
    
s=Triangle(4)
print(s.getPeri())
'''
'''
class Hero():
    def __init__(self,hp,att):
        self.hp=hp
        self.att=att

    def beattack(self,enemy):
        self.hp-=enemy.att
    
    def attack(self,enemy):
        enemy.beattack(self)
    
    def heal(self):
        self.hp+=1

class Shooter(Hero):
    def __init__(self,hp,att):
        super().__init__(hp,att)
    
    def attack(self,enemy):
        super().attack(enemy)
        super().attack(enemy)

class Archmage(Hero):   
    def __init__(self,hp,att,mp):
        super().__init__(hp,att)
        self.mp=mp

    def heal(self):
        self.mp-=1
        super().heal()
        super().heal()

class Warrior(Hero):   
    def __init__(self,hp,att,defe):
        super().__init__(hp,att)
        self.defe=defe

    def beattack(self,enemy):
        if self.defe>enemy.att:
            self.defe-=enemy.att
        else:
            x=enemy.att-self.defe
            self.hp-=x
            self.defe=0

a=Archmage(3,3,4)
w=Warrior(3,1,2)
a.attack(w)
print(w.hp)
'''
'''
s=open("shit.txt","w")
s.writelines(["shit","\n","shift"])
s.close()
s=open("shit.txt","r")
print(s.readline())
print(s.readline())
'''
#f=open("文件路径+文件名"，"打开模式") w , a , r

'''
读取：
.read(<size>)默认全读
.readline()按行输出
.readlines()逐行读取，合并列表输出
写入：
.write(<str>)
.writelines(<list>)
'''

p=open("patient.txt","w")
print("name")
name=input()
p.writelines([name,"\n"])
print("temp")
temp=str(input())
p.writelines([temp,"\n"])
print("pulse")
pulse=str(input())
p.write(pulse)
p.close()
p=open("patient.txt","r")
print(p.read())
