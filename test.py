import unittest
from Visitorcountread import lambda_handler
import json
      
class TestVisitor(unittest.TestCase):
    def test_lambda_handler(self):
        res_api = lambda_handler('a', 'b')
        self.assertEqual(res_api['statusCode'],200,msg=None)
        
    #need add to pipeline python3 -m unittest test.py