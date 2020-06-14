import unittest
from employee import HBCemployee

class Test_hbcEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUPclass() Method")

    def setUp(self):
        print("setUp() Method")
        self.emp1 = HBCemployee("Praveen", "Atravanam", 3000)
        self.emp2 = HBCemployee("Naveen", "Kumar", 5000)

    def test_Fullname(self):
        print("test_Fullname() Method")
        self.assertEqual(self.emp1.empfullName, "Praveen Atravanam")
        self.assertEqual(self.emp2.empfullName, "Naveen Kumar")

    def test_Email(self):
        print("test_Email() Method")
        self.assertEqual(self.emp1.empEmail, "Praveen.Atravanam@email.com")
        self.assertEqual(self.emp2.empEmail, "Naveen.Kumar@email.com")

    def test_Pay(self):
        print("test_Pay() Method")
        self.emp1.raisePay()
        self.emp2.raisePay()
        self.assertEqual(self.emp1.raisePay(), 3750)
        self.assertEqual(self.emp2.raisePay(), 6250)

    def tearDown(self):
        print("tearDown() Method")
        unittest.TestCase.tearDown(self)

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass() method")


if __name__ == '__main__':
    unittest.main()
