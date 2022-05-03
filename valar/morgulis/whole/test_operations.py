
import unittest
import operations

class TestOperations(unittest.TestCase):
    def testSumOnlyFraction(self):
        self.assertListEqual([0,5,6],operations.sum([0,1,2],[0,1,3]))
    def testSumFractionWithWhole(self):
        """
        3/4 + 4/5 = 15/20 + 16/20 = 31/20 = 1 11/20
        """
        self.assertListEqual([1,11,20],operations.sum([0,3,4], [0,4,5]))
    def testSumForWholeNumber(self):
        """
        3/8 + 5 = 5 3/8
        """
        self.assertListEqual([5,3,8],operations.sum([0,3,8], [5,0,0]))
    def testDiffOnlyFract(self):
        """
        1/6 - 1/7 = 7/42 - 6/42 = 1/42
        """
        self.assertListEqual([0,1,42],operations.diff([0,1,6], [0,1,7]))
    def testDiffWithWholePart(self):
        """
        1 1/2 - 2/3 = 9/6 - 4/6 = 5/6
        """
        self.assertListEqual([0,5,6],operations.diff([1,1,2], [0,2,3]))
    def testDiffNegativeResult(self):
        """
        2/9 - 5/8 = 16/72 - 45/72 = -29/72
        """
        self.assertListEqual([0,-29,72],operations.diff([0,2,9], [0,5,8]))
    def testDiffForWholeNumber(self):
        """
        2 - 1/3 = 1 2/3
        """
        self.assertListEqual([1,2,3],operations.diff([2,0,0], [0,1,3]))
    def testMultipleOnlyFracts(self):
        """
          1/2 * 2/3 = 2/6 = 1/3
        """
        self.assertListEqual([0,1,3],operations.multiple([0,1,2], [0,2,3]))
    def testMultipleWithWHolePart(self):
        """
        1 3/5 * 2 5/7 = 8/5 * 19/7 = 152/35 = 4 12/35
        """
        self.assertListEqual([4,12,35],operations.multiple([1,3,5], [2,5,7]))
    def testMultipleForWholePart(self):
        """
        2 * 3/7 = 14/7 * 3/7 = 42/49 = 6/7
        """
        self.assertListEqual([0,6,7],operations.multiple([2,0,0], [0,3,7]))
    def testDivisionOnlyFractionPart(self):
        """
        4/5 / 2/3 = 4/5 * 3/2 = 12/10 = 1 1/5
        """
        self.assertListEqual([1,1,5],operations.division([0,4,5], [0,2,3]))
    def testDivisionWithWholePart(self):
        """
        2 3/4 / 1 1/2 = 11/4 * 2/3 = 22/12 = 11/6 = 1 5/6
        """
        self.assertListEqual([1,5,6],operations.division([2,3,4], [1,1,2]))
    def testDivisionForWholePart(self):
        """
        1/3 / 2 = 1/3 / 2/1 = 1/3 * 1/2 = 1/6
        
        """
        self.assertListEqual([0,1,6],operations.division([0,1,3], [2,0,0]))
          
    
if __name__ == '__main__':
    unittest.main()
        
