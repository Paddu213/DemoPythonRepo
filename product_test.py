from INHERITANCE2 import Product
import unittest

class Test_Product(unittest.TestCase):
    def test_Display_Product_details(self):
        self.obj1=Product("milk",20,15,4.5)
        self.assertEqual(self.obj1.Display_Product_details,'product name : milk')
        self.obj1.Display_Product_details()

if __name__=="__main__":
    unittest.main()