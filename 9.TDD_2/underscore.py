class Underscore(object):
    def map(self, mylist, callback):
        newList = []
        for item in mylist:
            newList.append(callback(item))
        return newList
    def reduce(self, mylist, callback):
        num = 0
        for item in mylist:
            num += callback(num, item) - num
        return num
    def find(self, mylist, callback, thing):
        newList = []
        for item in mylist:
            if callback(item, thing) == True:
                newList.append(item)
        return newList
    def filter(self, callback, mylist):
        newList = []
        for item in mylist:
            if callback(item) == True:
                newList.append(item)
        return newList
    def reject(self, callback, mylist):
        newList = []
        for item in mylist:
            if callback(item) == False:
                newList.append(item)
        return newList
_ = Underscore()
# nums = [2,3]
# for i in map(lambda x: x**x, nums): print(i)
# f = lambda x,y: x**2 + y**2
# print f(5,6)
# nums = [1,2,3,4]
# print list(_.filter(lambda x: x%2==0, nums))
nums = [1,2,3,4]
print list(_.reject(lambda x: x%2==0, nums))
# nums = [1,2,3,4]
# print _.map(nums, lambda x: x*2)
# nums = [1,2,3,4]
# print _.reduce(nums, lambda x,y: x+y)
# nums = [1,2,3,4,10, "star"]
# print _.find(nums, lambda x,y: x==y, nums[2])
