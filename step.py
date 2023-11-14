'''
import math 
 
def isPrime(n): 
    if n == 1: 
        return True
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            return False
    return True

def step(n):
    if n>=3:
        sum=0
        for i in range(1,n+1):
            if isPrime(i)==True:
                x=n-i
                if x!=0:
                    sum=sum+step(x)
                else:
                    sum=sum+1
        return sum
    if n==1:
        return 1
    if n==2:
        return 2
    
print(step(5))
'''

def prime(x):
    lst=[1]
    for num in range(1,x+1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                lst.append(num)
    return lst


X = int(input())

result = [1,1]

for i in range(2,X+1):
    result.append(0)
    for x in prime(i):
        result[i]+=result[i-x]



print(result[X])