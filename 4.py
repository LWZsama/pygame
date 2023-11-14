'''
a=[2,7,5,1,4,6,3]
for i in range(0,6):
    if a[0]<a[1]:
        c=a[1]
        a[1]=a[0]
        a[0]=c
    if a[1]<a[2]:
        c=a[2]
        a[2]=a[1]
        a[1]=c
    if a[2]<a[3]:
        c=a[3]
        a[3]=a[2]
        a[2]=c
    if a[3]<a[4]:
        c=a[4]
        a[4]=a[3]
        a[3]=c
    if a[4]<a[5]:
        c=a[5]
        a[5]=a[4]
        a[4]=c
    if a[5]<a[6]:
        c=a[6]
        a[6]=a[5]
        a[5]=c
print(a)
'''

'''
a=[2,7,5,1,4,8,6,3]
length=len(a)
for i in range(0,length):
    for x in range(0,length-1-i):
        if a[x]>a[x+1]:
            c=a[x+1]
            a[x+1]=a[x]
            a[x]=c
print(a)
'''

'''
a=[2,7,5,1,4,8,6,3]
length=len(a)
for i in range(0,length):
    min=i
    for x in range(i,length-1):
        if a[min]>a[x+1]:
            min=x+1
    c=a[i]
    a[i]=a[min]
    a[min]=c
print(a)
'''

'''
a=[7,2,6,3,1,5,4]
length=len(a)
for i in range(0,length-1):
    j = i    
    while a[j]>a[j+1] and j>=0:
        x=a[j]
        a[j]=a[j+1]
        a[j+1]=x
        j-=1
print(a)
'''

'''
a=[7,2,6,3,1,5,4]
length=len(a)
for i in range(0,length):
    j=0
    for x in range(0,length-1-i):
        if a[x]>a[x+1]:
            c=a[x+1]
            a[x+1]=a[x]
            a[x]=c
            j+=1
        if a[length-x-1]<a[length-x-2]:
            c=a[length-x-2]
            a[length-x-2]=a[length-x-1]
            a[length-x-1]=c
            j+=1
    print(a)
    if j==0:
        break
'''
'''
sum = 0
for i in range(2,100):
    for j in range(2,i):
        if (i%j == 0):
            break
    else:
        sum += i
print(sum)
'''
x=100
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
o=len(a)
start=0
end=14
index=(start+end)//2
for i in range(0,o):
    index=(start+end)//2
    if x<a[index]:
        end=index
    elif x>a[index]:
        start=index
    else:
        print(index)
        break

