import unittest
import os
from data.data_preprocessing import process_data

class TestDataPreprocessing(unittest.TestCase):
    def test_process_data(self):
        raw_data = {'albums': {'items': [{'name': 'Test Album'}]}}
        raw_data_path = os.path.join('data', 'datasets', 'raw', 'test_data.json')
        with open(raw_data_path, 'w') as file:
            file.write(str(raw_data))
        
        process_data('test_data.json', 'processed_test_data.json')
        
        processed_data_path = os.path.join('data', 'datasets', 'processed', 'processed_test_data.json')
        self.assertTrue(os.path.exists(processed_data_path))
        
        os.remove(raw_data_path)
        os.remove(processed_data_path)

if __name__ == '__main__':
    unittest.main()
