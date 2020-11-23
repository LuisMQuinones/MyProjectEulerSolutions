
# @author Luis Quinones
# Logic: Pythagorean triplet is defined as:
# a<b<c => a^2 + b^2 = c^2
# Problem wants a triplet that satisfies:
# a + b + c = 10000
# a < 1000/3 because a cannot be greater than b
# c > 1000/3 because c has to be greater than b
#
#

sumLimit = 1000
aLimit = sumLimit/3
for a in range(aLimit):
  for c in range(aLimit,sumLimit):
      b = (c**2-a**2)**.5
      if(a+b+c == 1000 and a<b and b<c):
          p = a*b*c

          sA = str(a)
          sB = str(b)
          sC = str(c)
          sP = str(p)

          print("a: {0} b: {1} c:{2} | product: {3}".format(sA,sB,sC,sP))
