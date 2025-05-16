import unittest
from input_parser import parse_input_lines
from models.item import Item

class TestInputParser(unittest.TestCase):

    def test_basic_parsing(self):
        raw_input = [
            "1 book at 12.49",
            "1 music CD at 14.99",
            "1 chocolate bar at 0.85"
        ]
        items = parse_input_lines(raw_input)

        self.assertEqual(len(items), 3)

        self.assertEqual(items[0].name, "book")
        self.assertEqual(items[0].shelf_price, 12.49)
        self.assertEqual(items[0].quantity, 1)
        self.assertTrue(items[0].is_exempt)
        self.assertFalse(items[0].is_imported)

        self.assertEqual(items[1].name, "music CD")
        self.assertEqual(items[1].shelf_price, 14.99)
        self.assertFalse(items[1].is_exempt)

        self.assertEqual(items[2].name, "chocolate bar")
        self.assertTrue(items[2].is_exempt)


    def test_import_and_exempt_flags(self):
        raw_input = [
            "1 imported box of chocolates at 10.00",
            "1 imported bottle of perfume at 47.50"
        ]
        items = parse_input_lines(raw_input)

        self.assertTrue(items[0].is_imported)
        self.assertTrue(items[0].is_exempt)

        self.assertTrue(items[1].is_imported)
        self.assertFalse(items[1].is_exempt)


    def test_parse_input_lines_with_missing_quantity(self):
        input_lines = ["book at 12.49"]  # no quantity at start
        items = parse_input_lines(input_lines)
        self.assertEqual(len(items), 0)


    def test_parse_input_lines_with_missing_price(self):
        input_lines = ["1 book at"]  # missing price after 'at'
        items = parse_input_lines(input_lines)
        self.assertEqual(len(items), 0)


    def test_parse_input_lines_with_missing_name(self):
        input_lines = ["1 at 12.49"]  # no item name between quantity and 'at'
        items = parse_input_lines(input_lines)
        self.assertEqual(len(items), 0)


    def test_parse_input_lines_with_invalid_quantity(self):
        input_lines = ["abc book at 12.49"]  # non-integer quantity
        items = parse_input_lines(input_lines)
        self.assertEqual(len(items), 0)


    def test_parse_input_lines_with_invalid_price(self):
        input_lines = ["1 book at xyz"]  # non-float price
        items = parse_input_lines(input_lines)
        self.assertEqual(len(items), 0)


    def test_parse_input_lines_valid_and_invalid_mixed(self):
        input_lines = [
            "1 book at 12.49",
            "invalid line",
            "2 imported chocolates at 5.00",
            "1 at 20.00",
            "3 music CD at xyz"
        ]
        items = parse_input_lines(input_lines)
        
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].name, "book")
        self.assertEqual(items[1].name, "imported chocolates")


if __name__ == "__main__":
    unittest.main()
