import unittest
import os
from data.data_collection import fetch_new_releases, save_data

class TestDataCollection(unittest.TestCase):
    def test_fetch_new_releases(self):
        data = fetch_new_releases()
        self.assertIn('albums', data)

    def test_save_data(self):
        data = {'test': 'data'}
        save_data(str(data), 'test_data.json')
        self.assertTrue(os.path.exists(os.path.join('data', 'datasets', 'raw', 'test_data.json')))
        os.remove(os.path.join('data', 'datasets', 'raw', 'test_data.json'))

if __name__ == '__main__':
    unittest.main()
