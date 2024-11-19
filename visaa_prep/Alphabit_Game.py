s=input()
n=len(s)
v,c=0,0
for i in s:
    if i.lower() in 'aeiou':
        v+=1
    elif 'a'< i.lower()<='z':
        c+=1
print(f"{v},{c}")
