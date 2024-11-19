a=input()
s=''
c=1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        c+=1
    else:
        s+=a[i-1]+str(c)
        c=1
s+=a[-1]+str(c)
print(s)
