import unittest
import main-program

class TestProgram(unittest.TestCase):
inputs = ['3','20.05.2022','15:00','21.05.2022','12:00','22.05.2022','07:00']
  
  def test_main(self):
    self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()