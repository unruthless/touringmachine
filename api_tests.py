import os
import unittest
import tempfile

import api

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.api = api.app.test_client()

    def tearDown(self): pass

    def test_endpoint(self):
        resp = self.api.get('/api/v0')
        self.assertEqual(resp.status_code, 200)

    def test_200_when_required_parameters_provided(self):
        resp = self.api.post('/api/v0', data=dict(
            origin=94103,
            destination=90210
        ), follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()
