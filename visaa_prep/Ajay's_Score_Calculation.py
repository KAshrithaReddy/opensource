n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    t=x//10
    m=y*t
    print(m)
