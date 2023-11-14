def merge(a,b):
    left=0
    right=0
    l=len(a)
    r=len(b)
    temp=[]
    while left<l and right<r:
        if a[left]>b[right]:
            temp.append(b[right])
            right+=1
        else:
            temp.append(a[left])
            left+=1
    temp.extend(a[left:])
    temp.extend(b[right:])
    return(temp)

def divide(_list):
    if (len(_list)<=1):
        return _list
    mid=len(_list)//2
    left=divide(_list[:mid])
    right=divide(_list[mid:])
    return merge(left,right)

print(divide([1,4,5,2,7]))