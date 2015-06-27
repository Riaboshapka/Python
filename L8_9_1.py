from random import randint
import datetime
start = datetime.datetime.today()

def qsort(arr):
	less = []
	equal = []
	greater = []
	
	if len(arr) > 1:
		av = arr[0]
		for x in arr:
			if x < av:
				less.append(x)
			if x == av:
				equal.append(x)
			if x > av:
				greater.append(x)
		return qsort(less) + equal + qsort(greater)
	else:
		return arr
		
#generate random data
n = 500000
nums = []
for i in range(n):
	nums.append(randint(0, 10000))
#print nums
print 'quicksorting, please wait...'
nums = qsort(nums)
print 'ready'
print (datetime.datetime.today() - start).total_seconds()
