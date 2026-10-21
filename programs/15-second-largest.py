/* Question 15: Find the second-largest distinct value
 * Answer:
 */
a=sorted(set(map(int,input().split()))); print(a[-2] if len(a)>1 else 'No second-largest')
