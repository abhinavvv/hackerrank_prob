from collections import Counter
n=int(raw_input())
a = []
#for i in range(0,n):
 #   a.append(int(raw_input()))
a = [int(x) for x in raw_input().split()]
count = Counter()
for number in a:
    count[number] += 1
print [k for k, v in count.iteritems() if v == 1][0]