/* Question 20: Count value frequencies
 * Answer:
 */
from collections import Counter
a=list(map(int,input().split())); print(dict(Counter(a)))
