/* Question 6: Print Fibonacci numbers
 * Answer:
 */
n=int(input()); a,b=0,1
for _ in range(n): print(a,end=' '); a,b=b,a+b
print()
