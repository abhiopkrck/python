/* Question 5: Calculate factorial
 * Answer:
 */
n=int(input()); f=1
for i in range(2,n+1): f*=i
print(f if n>=0 else 'Invalid input')
