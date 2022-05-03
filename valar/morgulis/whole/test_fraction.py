
import unittest
import fraction

class TestFraction(unittest.TestCase):
    def testCheckOnlyWholePart(self):
        input_string = "146"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[True,'Good'])
    def testCheckOnlyFracts(self):
        input_string = "1/2"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[True,'Good'])
    def testCheckFractsAndWholePart(self):
        input_string = "5 3/5"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[True,'Good'])
    def testCheckBigNumber(self):
        input_string = "12 123/1234"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[True,'Good'])
    def testCheckNegativeNumeberWithWholePart(self):
        input_string = "-78 12/13"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[True,'Good'])
    def testCheckNegativeNumeberWithWholePart(self):
        input_string = "-1414/1415"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[True,'Good'])
    def testCheckWrongFormat(self):
        input_string = "bla-bla-bla"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[False,'Wrong format input string'])
    def testCheckFormatNullDenominator(self):
        input_string = "5/0"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[False,'Denominator cannot be 0!'])
    def testCheckFormatNullNumenator(self):
        input_string = "0/10"
        answer = fraction.check(input_string)
        self.assertListEqual(answer,[False,'Numenator cannot be 0!'])
    def testMakeListOnlyFracts(self):
        input_string = "3/4"
        answer = fraction.makeList(input_string)
        self.assertListEqual(answer,[0,3,4])
    def testMakeListFracts(self):
        input_string = "5 2/3"
        answer = fraction.makeList(input_string)
        self.assertListEqual(answer,[5,2,3])
    def testFormatFractsWithoutWholePart(self):
        fract = [0,7,9]
        answer = fraction.toString(fract)
        self.assertEqual(answer,'7/9')
    def testFormatFractsWithWholePart(self):
        fract = [3,11,12]
        answer = fraction.toString(fract)
        self.assertEqual(answer,'3 11/12')
    def testFormatFractsEmptyFractPart(self):
        fract = [234,0,0]
        answer = fraction.toString(fract)
        self.assertEqual(answer,'234')
    def testFormatFractsNull(self):
        fract = [0,0,0]
        answer = fraction.toString(fract)
        self.assertEqual(answer,'0')
    def testNormalize(self):
        fract = [5,24,60]
        answer = fraction.toNormalize(fract)
        self.assertEqual(answer,[5,2,5])
    def testNormalizeWithWholePart(self):
        fract = [3,1870,770]
        answer = fraction.toNormalize(fract)
        self.assertEqual(answer,[5,3,7])
    def testNormalizeBorderCase(self):
        fract = [0,6,2]
        answer = fraction.toNormalize(fract)
        self.assertEqual(answer,[3,0,0])    
    def testRespectByEvclid(self):
        numbers = [1071, 462]
        self.assertEqual(fraction.respectByEvclid(numbers), 21)
    def testRespectByEvclidOtherCase(self):
        numbers = [123, 122]
        self.assertEqual(fraction.respectByEvclid(numbers), 1)
    def testUnNormalize(self):
        self.assertListEqual([0,4,3], fraction.unNormalize([1,1,3]))
    
    
    
    
if __name__ == '__main__':
    unittest.main()
        
