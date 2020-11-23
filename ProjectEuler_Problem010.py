# Implemented Sieve of Eratosthenes Algorithm
# Used this algorithm to make it more efficient

def Sieve(n):
    nums = [True for x in range(n+1)]
    limit = int(n**.5)
    for i in range(2,n):
        if(nums[i] == True):
            for j in range(i*i, n+1, i):
                nums[j] = False
    return nums

nums = Sieve(2000000)
primes = [i for i in range(len(nums)) if (nums[i])== True]
primes.remove(0)
primes.remove(1)

sum = 0
for prime in primes:
    sum += prime
print(sum)
