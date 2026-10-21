/* Question 19: Find a pair that sums to target
 * Answer:
 */
a=list(map(int,input().split())); target=int(input()); seen={}; ans=None
for i,x in enumerate(a):
 if target-x in seen: ans=(seen[target-x],i); break
 seen[x]=i
print(ans if ans else 'No pair')
