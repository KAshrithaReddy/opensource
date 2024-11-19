n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    l=sum(arr[0:i])
    r=sum(arr[i+1:])
    diff=abs(l-r)
    print(diff,end=' ')
