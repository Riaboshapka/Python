from random import randint
import datetime
start = datetime.datetime.today()

#generate random data
n = 5000
nums = []
for i in range(n):
	nums.append(randint(0, 10000))
#print nums
print 'sorting, please wait...'

#sort
for i in range(len(nums)):
	for j in range(len(nums)):
		if nums[i] < nums[j]:
			tmp = nums[i]
			nums[i] = nums[j]
			nums[j] = tmp

#print nums
print 'ready'
print (datetime.datetime.today() - start).total_seconds()
