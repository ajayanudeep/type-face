s1 = input()
s2 = input()
count=0
for i in range(len(s1)):
    if(s2[len(s2)-1]==s1[i]):
        count+=1
print(count)