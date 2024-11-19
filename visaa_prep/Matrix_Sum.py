n=int(input())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(n):
    s1=sum(mat[i])
    for j in range(n):
        s1+=mat[j][i]
    print(s1,end=' ')
