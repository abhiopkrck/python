/* Question 12: Implement binary search
 * Answer:
 */
a=sorted(map(int,input().split())); x=int(input()); l=0; r=len(a)-1; ans=-1
while l<=r:
 m=(l+r)//2
 if a[m]==x: ans=m; break
 if a[m]<x: l=m+1
 else: r=m-1
print(ans)
