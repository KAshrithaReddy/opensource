n=int(input())
arr=list(map(int,input().split()))
max_al=0
al=0
for i in arr:
    al+=i
    max_al=max(al,max_al)
print(max_al)
