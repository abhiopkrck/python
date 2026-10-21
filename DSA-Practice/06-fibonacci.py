// Question 6: Print Fibonacci sequence
// Answer:
n=int(input()); print('Prime' if n>=2 and all(n%i for i in range(2,int(n**0.5)+1)) else 'Not prime')
