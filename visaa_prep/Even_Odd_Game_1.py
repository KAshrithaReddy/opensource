n=int(input())
s=0
while(n!=0):
    r=n%10
    s+=r
    n//=10
print('Vignesh'if s%2==0 else 'Charan')
