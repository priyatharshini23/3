p=int(input())
q=list(map(int,input().split(" ")))
r=sorted(q)
print(r[len(q)//2])
