/* Question 10: Sum the digits of a number
 * Answer:
 */
n=abs(int(input())); total=0
while n: total+=n%10; n//=10
print(total)
