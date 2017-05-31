import os
import app
import unittest
import tempfile

class AppTestCase(unittest.TestCase):

	def test_main(self):
		rv = self.app.get('/')
		self.assertEqual(rv.data, "Home")

if __name__ == '__main__':
    unittest.main()