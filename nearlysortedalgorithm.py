t=int(input())
while(t):
    t-=1
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    i=0
    l=[]
    while i<n:
        temp=arr[i:i+k]
        temp.sort()
        l.append(temp)
        i+=k
    for r in l:
        for j in r:
            print(j,end=" ")
    print()
   
