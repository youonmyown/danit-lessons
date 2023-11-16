import unittest
from unittest.mock import patch
from getid import get_user_ids

class TestGetUserIds(unittest.TestCase):

    @patch('builtins.print', side_effect=lambda *args: None)
    @patch('sys.argv', ['getid.py', 'https://jsonplaceholder.typicode.com/posts', 'output.json', '--verbose'])
    def test_get_user_ids_verbose(self, mock_print):
        with patch('requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_response.status_code = 200

            get_user_ids('https://jsonplaceholder.typicode.com/posts', 'output.json', verbose=True)

if __name__ == '__main__':
    unittest.main()
