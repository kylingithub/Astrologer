import unittest
import Astrologer

class MyTestCase(unittest.TestCase):

    def test_birthday_dict(self):
        self.assertDictEqual(Astrologer.get_birthday_dict(1995,12,13),{
            1:3,
            2:1,
            3:1,
            5:1,
            9:2
        })
        self.assertDictEqual(Astrologer.get_birthday_dict(2005,1,13),{
            1:2,
            2:1,
            3:1,
            5:1
        })
    def test_life_number(self):
        self.assertEqual(1,1)
        self.assertEqual(9,Astrologer.get_life_number(1993,8,15))
        self.assertEqual(1,Astrologer.get_life_number(1993,8,16))
        self.assertEqual(6,Astrologer.get_life_number(1993,8,30))
    
    def test_constellation(self):
        self.assertEqual("獅子座",Astrologer.get_constellation(8,16))
        self.assertEqual("處女座",Astrologer.get_constellation(8,30))


if __name__ == '__main__':
    unittest.main()
