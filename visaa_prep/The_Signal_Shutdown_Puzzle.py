n,m=map(int,input().split())
mat=[]
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
r,c=[],[]
for i in range(n):
    for j in range(m):
        if mat[i][j]==0:
            r.append(i)
            c.append(j)
for i in range(n):
    for j in range(m):
        if i in r or j in c:
            mat[i][j]=0
for i in range(n):
    for j in range(m):
        print(mat[i][j],end=' ')
    print()
