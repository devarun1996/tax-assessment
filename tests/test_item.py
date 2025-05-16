import unittest
from models.item import Item

class TestItem(unittest.TestCase):
    def test_item_creation(self):
        item = Item(name="book", shelf_price=12.49, quantity=1, is_imported=False, is_exempt=True)
        self.assertEqual(item.name, "book")
        self.assertEqual(item.shelf_price, 12.49)
        self.assertEqual(item.quantity, 1)
        self.assertFalse(item.is_imported)
        self.assertTrue(item.is_exempt)
        self.assertEqual(item.total_price_after_tax, 0.0)  # This is defined in the model

    def test_item_total_price_after_tax_assignment(self):
        item = Item(name="music CD", shelf_price=14.99, quantity=1, is_imported=False, is_exempt=False)
        # Assign total_price_after_tax to simulate tax calculation
        item.total_price_after_tax = 16.49
        self.assertAlmostEqual(item.total_price_after_tax, 16.49, places=2)

if __name__ == "__main__":
    unittest.main()
