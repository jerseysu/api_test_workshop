##This is for python get API test method sample

import requests
import unittest

class TestGETMethods(unittest.TestCase):

    def setUp(self):
        TestGETMethods.req = requests.get('http://jsonplaceholder.typicode.com/posts/1')

    def test_check_userid(self):
        print TestGETMethods.req.json()['userId']
        self.assertEqual(TestGETMethods.req.json()['userId'], 1)

    def test_check_id(self):
    	print TestGETMethods.req.json()['id']
    	self.assertEqual(TestGETMethods.req.json()['id'], 2)


if __name__ == '__main__':
    unittest.main()
