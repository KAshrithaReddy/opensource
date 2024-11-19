n=int(input())
mat=[]
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
for i in range(n):
    for j in range(n-1,-1,-1):
        print(mat[i][j],end=' ')
    print()
