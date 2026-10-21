/* Question 9: Check a palindrome
 * Answer:
 */
s=input().lower(); s=''.join(c for c in s if c.isalnum()); print('Palindrome' if s==s[::-1] else 'Not palindrome')
