import unittest
from unittest.mock import patch

import file_utils


class TestTotal(unittest.TestCase):

    @patch('file_utils.get_file_data')
    def test_calculate_sum_with_pathc_decorator(self, mock_get_file_data):
        mock_get_file_data.return_value = [3, 4, 5]
        result = file_utils.calculate_sum('')
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()