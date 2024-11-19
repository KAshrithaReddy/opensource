n=int(input())
arr=list(map(int,input().split()))
p=0
max_p=-1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]>arr[k] and arr[j]+arr[k]>arr[i] and arr[k]+arr[i]>arr[j]:
                p=arr[i]+arr[j]+arr[k]
                max_p=max(max_p,p)
print(max_p)
