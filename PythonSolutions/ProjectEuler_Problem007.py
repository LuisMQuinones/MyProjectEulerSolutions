# @author Luis Quinones
# Brute Force Method
# I can implememt Sieve of Eratosthenes Algorithm
# to make it quicker

import time
def isPrime(num):
    if(num == 0 or num==1):
        return True
    counter =2
    while(counter<num):
        if(num%counter ==0):
            return False
        counter+=1
    return True

def findPrime(index):
    counter =0
    prime = -1
    x=1
    while(counter<index):
        x+=1
        if(isPrime(x)):
            prime =x
            counter+=1
            #print(counter,x)
    return prime

beforeTime = time.gmtime()

print(beforeTime)
print(findPrime(10001))
afterTime = time.gmtime()
print(afterTime)
print(time.mktime(afterTime)-time.mktime(beforeTime))
