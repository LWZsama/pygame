bst=[[1,11,2],[3,7,4],[5,25,6],[-1,3,-1],[-1,8,-1],[7,15,8],[-1,28,9],[-1,12,-1],[-1,20,-1],[-1,35,-1]]

#in-order
'''
def in_order(i):
    if bst[i][0] != -1:
        in_order(bst[i][0])    
    print(bst[i][1])

    if bst[i][2] != -1:
        in_order(bst[i][2])
    #print(bst[i][1])

in_order(0)
'''

#pre-order
'''
def pre_order(i):
    if bst[i][0]!=-1:
        print(bst[i][1])
        pre_order(bst[i][0])
    
    if bst[i][0]==-1:
        print(bst[i][1])
    
    if bst[i][2]!=-1:
        pre_order(bst[i][2])

pre_order(0)
'''

#post-order

def post_order(i):
    if bst[i][0]!=-1:
        post_order(bst[i][0])
    
    if bst[i][2]!=-1:
        post_order(bst[i][2])

    print(bst[i][1])

post_order(0)