import unittest
from models.tax import SalesTax, ImportTax
from models.item import Item

class TestTaxCalculations(unittest.TestCase):

    def setUp(self):
        self.sales_tax = SalesTax(rate=0.10)
        self.import_tax = ImportTax(rate=0.05)

    def test_sales_tax_calculation(self):
        item = Item(name="music CD", shelf_price=14.99, quantity=1, is_imported=False, is_exempt=False)
        tax = self.sales_tax.calculate_tax(item)
        self.assertAlmostEqual(tax, 1.50, places=2)  # 10% of 14.99 rounded up to 1.50

    def test_import_tax_calculation(self):
        item = Item(name="imported box of chocolates", shelf_price=10.00, quantity=1, is_imported=True, is_exempt=True)
        tax = self.import_tax.calculate_tax(item)
        self.assertAlmostEqual(tax, 0.50, places=2)  # 5% of 10.00 = 0.50

    def test_no_tax_for_exempt_non_imported_item(self):
        item = Item(name="book", shelf_price=12.49, quantity=1, is_imported=False, is_exempt=True)
        tax = self.sales_tax.calculate_tax(item)
        self.assertEqual(tax, 0)

    def test_tax_for_imported_non_exempt_item(self):
        item = Item(name="imported perfume", shelf_price=47.50, quantity=1, is_imported=True, is_exempt=False)
        sales = self.sales_tax.calculate_tax(item)
        imp = self.import_tax.calculate_tax(item)
        total_tax = sales + imp
        self.assertAlmostEqual(total_tax, 7.15, places=2)  # 10% + 5% of 47.50

    def test_tax_calculation_with_quantity(self):
        item = Item(name="music CD", shelf_price=14.99, quantity=2, is_imported=False, is_exempt=False)
        tax = self.sales_tax.calculate_tax(item) * item.quantity
        self.assertAlmostEqual(tax, 3.00, places=2)  # doubled for quantity=2

if __name__ == "__main__":
    unittest.main()
