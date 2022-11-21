k=[[0]*256 for i in range(256)]
l=[[1,0,0,1,1],
    [1,0,0,0,1],
    [1,0,0,1,1],
    [1,1,1,1,1]]
indices=[]
for i in range(len(l)):
    fi=-1
    si=-1
    for j in range(len(l[i])):
        if l[i][j]==0 and si==-1:
            si=j
        elif l[i][j]==0 and (fi==-1 or fi==j-1):
            fi=j
    indices.append([[i,si],[i,fi]])

l1=[]
l2=[]

answers=[]
print(indices[0])
for i in indices:
    if i[0][1]!=-1:
        l1.append([i[0][0],i[0][1]])
    if i[1][1]!=-1:
        l2.append([i[1][0],i[1][1]])
print(indices)


        