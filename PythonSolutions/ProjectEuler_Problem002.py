'''
Written By: LUIS QUINONES Sept 6, 2020
https://projecteuler.net/problem=2
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1
and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the
sum of the even-valued terms.

Comment:
Rough as you go code
No real Optimization
'''
def fib(n):
    if(n<=0):
        return 0
    if(n==1):
        return 1
    if(n ==2):
        return 2
    return fib(n-1) + fib(n-2)

'''
for x in range(1,11):
    print(fib(x))
'''

def EvenFibonacciNumbers(limit):
    counter = 0
    theSum =  0  
    term = fib(counter)
    while(term<limit):
        if(term %2 ==0):
            theSum+=term
        term = fib(counter)
        counter+=1
    return theSum


print(EvenFibonacciNumbers(4000000))
