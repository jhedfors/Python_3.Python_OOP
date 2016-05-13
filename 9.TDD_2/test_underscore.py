import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.test_list = [1,2,3,4]
    def testMap(self):
        self.result = self._.map(self.test_list, lambda x: x*2)
        return self.assertEqual([2,4,6,8], self.result)
    def testReduce(self):
        self.result = self._.reduce(self.test_list, lambda x,y: x+y)
        return self.assertEqual(10, self.result)
    def testFind(self):
        self.result = self._.find(self.test_list, lambda x,y: x==y, self.test_list[2])
        return self.assertEqual([3], self.result)
    def testFilter(self):
        self.result = self._.filter(lambda x: x%2==0, self.test_list)
        return self.assertEqual([2,4], self.result)
    def testReject(self):
        self.result = self._.reject(lambda x: x%2==0, self.test_list)
        return self.assertEqual([1,3], self.result)

if __name__ == "__main__":
    unittest.main()
