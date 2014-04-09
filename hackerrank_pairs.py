# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = [int(x) for x in raw_input().split()]
a =[]
count = 0
a  = [int(x) for x in ra_input.split()]
a.sort()
for i in range(0,n):
    if (a[i]+k) > a[n-1]:
        break
    elif (a[i]+k) in a:
        count = count+1
    else:
        continue
print count
    
    