n=int(input())
arr=list(map(int,input().split()))
k=int(input())
l=0
r=n-1
p=-1
while(l<=r):
    mid=(l+r)//2
    if arr[mid]==k:
        p=mid
        break
    elif k>arr[mid]:
        l=mid+1
    else:
        r=mid-1
print(p)
