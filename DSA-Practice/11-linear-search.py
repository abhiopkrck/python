// Question 11: Linear search
// Answer:
a=sorted(map(int,input().split())); x=int(input()); print(__import__('bisect').bisect_left(a,x) if x in a else -1)
