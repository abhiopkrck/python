// Question 18: Stack push and pop
// Answer:
a=list(map(int,input().split())); t=int(input()); print(next(((i,j) for i in range(len(a)) for j in range(i+1,len(a)) if a[i]+a[j]==t),'No pair'))
