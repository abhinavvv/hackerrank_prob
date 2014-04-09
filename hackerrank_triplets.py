import math
import itertools
n = int(raw_input())
a = set([int(x) for x in raw_input().split()])
print a
print set(itertools.combinations(a, 3))
print len(set(itertools.combinations(a, 3)))
#print (math.factorial(len(a)))/(math.factorial(len(a)-3)*math.factorial(3))