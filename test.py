import random
import unittest
import urllib

class Test(unittest.TestCase):
  def test_adduser(self):
    res = urllib.urlopen("http://127.0.0.1:5000/add_user").getcode()
    self.assertEqual(res, 200)
  def test_show_user(self) :
    res = urllib.urlopen("http://127.0.0.1:5000/show_user/1").getcode()
    self.assertEqual(res, 200)
  def test_list_user(self):
    res = urllib.urlopen("http://127.0.0.1:5000/list_user").getcode()
    self.assertEqual(res, 300)
  

if __name__ == '__main__':
  unittest.main()
