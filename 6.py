'''
import random
symbol=["+","-","*","%"]
def create_secret(difficulty):
    for i in range(0,20):
        a=random.randint(1,99)
        b=random.choice(symbol)
        c=random.randint(1,99)
        d=random.choice(symbol)
        e=random.randint(1,99)
        y=eval(str(a)+b+str(c)+d+str(e))
        x=str(a)+b+str(c)+d+str(e)+"="+str(y)
        if len(x)==difficulty:
            return x   
    return "not possible"

print(create_secret(11))
'''

def set_colors(secret,guess):
    x=len(secret)
    ans=[]
    for i in range(0,x):
        a=secret.count(guess[i])
        b=guess.count(guess[i])
        c=guess[:i:].count(guess[i])
        q=0
        
        w=[index for index, element in enumerate(guess) if element==guess[i]]
        #w=guess.find(guess[i])   
        print(w)
        length=len(w)
        head=w[0]
        tail=w[length-1]+1
        for yi in range(head,tail):
            if secret[yi]==guess[yi]:
                q+=1
        print(secret[i],":",q)
        if secret[i]==guess[i]:
            ans.append((i,secret[i],"green"))
        elif secret[i]!=guess[i] and a-q >= 1:
            ans.append((i,guess[i],"yellow"))
        else:
            ans.append((i,guess[i],"grey"))
    
    return ans

print(set_colors("25+4*12=73","21+20*4=55"))

'''
def set_colors(secret,guess):
    x=len(secret)
    ans=[]
'''