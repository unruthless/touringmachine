import os
import unittest
import tempfile

import api

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, api.app.config['DATABASE'] = tempfile.mkstemp()
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()
        app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(api.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
