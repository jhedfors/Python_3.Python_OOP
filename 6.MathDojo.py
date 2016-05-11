class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self,*nums,**other):
        for num in nums:
            if type(num) is dict:
                self.add(num.values())
            elif type(num) is list or type(num) is tuple:
                self.add(*num)
            else:
                self.result += num
        for thing in other:
            self.result += other[thing]
        return self
    def subtract(self,*nums, **other):
        for num in nums:
            if type(num) is dict:
                self.subtract(num.values())
            elif type(num) is list or type(num) is tuple:
                self.subtract(*num)
            else:
                self.result -= num
        for thing in other:
            self.result += other[thing]
        return self
# print MathDojo().add((1,2)).result
# dict1 = {'number':10, 'dummy':5}
# print MathDojo().add([1],[3,dict1],4).result
print MathDojo().add([1],3,4).add((3, 5, 7, 8), {'a':2, 'b':4.3, 'c':1.25}).subtract({'a':1, 'b':1}, (2,3), [1.1, 2.3]).result

# MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
# print MathDojo().add(2).add(2, 5, 10).subtract(3, 2, 10).result
# tple = (1,5,3)
# rangeend = len(tple)
#
# for count in range(0,rangeend):
#     print tple[count]
# # print len(tple)
