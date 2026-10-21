/* Question 8: Reverse an integer
 * Answer:
 */
n=int(input()); sign=-1 if n<0 else 1; n=abs(n); r=0
while n: r=r*10+n%10; n//=10
print(sign*r)
