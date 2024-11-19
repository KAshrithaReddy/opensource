n=int(input())
k=int(input())
b=bin(n)[2:]
if len(b)>=k and b[-k]=='1':
    print('true')
else:
    print('false')
