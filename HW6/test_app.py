import unittest
from unittest.mock import patch

from app import *


class Test(unittest.TestCase):

    @patch('builtins.input', return_value='10006')
    def test_get_doc_owner_name(self, mock_inputs):
        print(documents)
        self.assertEqual(get_doc_owner_name(), 'Аристарх Павлов')

    @patch('builtins.input', return_value='10006')
    def test_get_doc_shelf(self, mock_inputs):
        self.assertEqual(get_doc_shelf(), '2')

    @patch('builtins.input',
           side_effect=['4545 222551', 'passport', 'Тест Тестин', '4'])
    def test_add_new_doc(self, mock_inputs):
        self.assertEqual(add_new_doc(), '4')
        self.assertIn(
            {
                "type": "passport",
                "number": "4545 222551",
                "name": "Тест Тестин"
            }, documents)

    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, mock_inputs):
        doc_num, del_mark = delete_doc()
        self.assertEqual(doc_num, '11-2')
        self.assertEqual(del_mark, True)
        self.assertNotIn(
            {
                "type": "invoice",
                "number": "11-2",
                "name": "Геннадий Покемонов"
            }, documents)
        self.assertNotIn('1', directories['1'])

    @patch('builtins.input', return_value='1')
    def test_add_new_shelf_exist(self, mock_inputs):
        num, mark = add_new_shelf()
        self.assertEqual(num, '1')
        self.assertEqual(mark, False)

    @patch('builtins.input', return_value='5')
    def test_add_new_shelf_not_exist(self, mock_inputs):
        num, mark = add_new_shelf()
        self.assertEqual(num, '5')
        self.assertEqual(mark, True)

    @patch('builtins.input', side_effect=['5455 028765', '3'])
    def test_move_doc_to_shelf(self, mock_inputs):
        move_doc_to_shelf()
        self.assertIn('5455 028765', directories['3'])
        self.assertNotIn('5455 028765', directories['1'])


if __name__ == '__main__':
    unittest.main()
