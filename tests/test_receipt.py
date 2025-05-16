import unittest
from models.item import Item
from models.receipt import Receipt

class TestReceipt(unittest.TestCase):

    def test_receipt_totals(self):
        items = [
            Item(name="book", shelf_price=12.49, quantity=1, is_imported=False, is_exempt=True),
            Item(name="music CD", shelf_price=14.99, quantity=1, is_imported=False, is_exempt=False),
            Item(name="chocolate bar", shelf_price=0.85, quantity=1, is_imported=False, is_exempt=True),
        ]
        receipt = Receipt(items)
        receipt.apply_taxes_and_calculate_totals()

        # Check total tax amount (sum of all item taxes)
        self.assertAlmostEqual(receipt.total_tax_amount, 1.50, places=2)

        # Check total amount (sum of all item total prices including tax)
        self.assertAlmostEqual(receipt.total_amount, 29.83, places=2)

        # Check individual item total price after tax
        # Book is exempted, so no tax -> price remains same
        self.assertAlmostEqual(items[0].total_price_after_tax, 12.49)

        # Music CD has sales tax (10%) but no import tax -> 14.99 + 1.50 = 16.49
        self.assertAlmostEqual(items[1].total_price_after_tax, 16.49)

        # Chocolate bar is exempted -> price remains same
        self.assertAlmostEqual(items[2].total_price_after_tax, 0.85)

if __name__ == "__main__":
    unittest.main()
