import os
import unittest
import tempfile

class AppTestCase(unittest.TestCase):

	def test_main(self):
		rv = self.app.get('/a')
		assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()