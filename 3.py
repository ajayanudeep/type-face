valid_digits=[0,1,2,5,6,8,9]

def valid(k):
    k=str(k)
    for i in k:
        if int(i) not in valid_digits:
            return False
    return True

n = int(input())
if n < len(valid_digits):
    print(valid_digits[n])
else:
    count=len(valid_digits)
    k=valid_digits[-1]
    while(count<=n):
        k+=1
        if valid(k):
            count+=1
    print(k)




