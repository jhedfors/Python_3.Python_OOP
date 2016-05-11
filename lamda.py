# https://github.com/madjaqk/explanations/blob/master/lambda.md

#
# nums = [3,2,6,1,5]
# print sorted(nums) # [1,2,3,5,6]

animals = ['monkey', 'eagle', 'giraffe', 'emu', 'seal']

# print sorted(animals) # ['eagle', 'emu', 'giraffe', 'monkey', 'seal']
# print sorted(animals, key=lambda x: x.find("e")) # ['eagle', 'emu', 'seal', 'monkey', 'giraffe']

# f = lambda a,b: a**2 + b**2
# print f(3,4) # 25

# nums = [2,3,4,5]
# for i in map(lambda x: x**x, nums): print(i)

# nums = [2,3,4,5]
# print list(filter(lambda x: x%2==0, nums)) # [2,4]

# nums = [2,3,4,5]
# print list(reject(lambda x: x%2==0, nums)) # [1,3]

# nums = [2,3,4,5]
# from functools import reduce # In Python 3, reduce was moved from the standard library to the functools module
# print reduce(lambda a,b: a+b, nums) # 14 = 2 + 3 + 4 + 5
# print reduce(lambda a,b: a*b, nums) # 120 = 2 * 3 * 4 * 5
# print reduce(lambda a,b: b**(a%b), nums) # 625 (left as an exercise for the reader)


nums = [2,3,4,5]

# map
for i in map(lambda x: x**x, nums): print(i)
[i**i for i in nums] # [4,27,256,3125]

# filter
print [i for i in nums if i%2==0] # [2,4]

# reject
print [i for i in nums if i%2!=0] # [3,5]
print [i for i in nums if not i%2==0] # [3,5] alternate syntax

#reduce
print sum(i for i in nums) # 14; you can also just do sum(nums)
