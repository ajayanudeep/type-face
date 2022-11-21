dec = int(input())
l=[]
while(dec>0):
    r = int(dec%3)
    l.append(str(r))
    dec=int(dec/3)
ans="".join(l[::-1])
print(int(ans))