from calculator import Math
import unittest

class TestAssert(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j=Math(5,10)
        print("assertEqual")
        self.assertEqual(j.add(),15)

    def test_add1(self):
        j = Math(5,10)
        print("assertNotEqual")
        self.assertNotEqual(j.add(),12)

    def assertTrue_test(self):
        j=Math(5,10)
        print("assertTrue")
        self.assertTrue(j.add()>10)

    def assertIn_test(self):
        print("assertIn")
        self.assertIn("51zxw","hello,51zxw")
        # self.assertIn("888","hello,51zxw")

    def assetIs_test(self):
        print("assertIs")
        self.assertIs("51zxw","51zxw")
        # self.assertIs("51","51zxw")

    def tearDown(self):
        print("test end")

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestAssert("test_add"))
    suite.addTest(TestAssert("test_add1"))
    suite.addTest(TestAssert("assertTrue_test"))
    suite.addTest(TestAssert("assertIn_test"))
    suite.addTest(TestAssert("assetIs_test"))

    runer=unittest.TextTestRunner()
    runer.run(suite)

    # unittest.main()

