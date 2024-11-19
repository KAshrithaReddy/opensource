p,q,r=map(int,input().split())
if p>r:
    print(0)
else:
    if p+q>r:
        print(1)
    else:
        print(2)
