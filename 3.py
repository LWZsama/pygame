'''
f.seek(offset,whence)(位移量，从哪开始 0从头 1从当前 2从尾) 从尾开始位移量是负的
1，2 "wb","rb",二进制打开'''

'''
h=open("hero.txt","r")
h.seek(0,0)
h.seek(0,0)
for i in range(1,10000): 
    if h.read(1) == "t":
        x=h.tell()-2
        h.seek(x,0)
        print(h.read(1))
        break
'''
#truncate(size)不填光标位置前保留，后面删；填size，从头保留size个


