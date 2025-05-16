from models.tax import ImportTax, SalesTax


class Receipt:
    def __init__(self, items):
        self.items = items
        self.total_tax_amount = 0.0
        self.total_amount = 0.0

    def apply_taxes_and_calculate_totals(self):
        sales_tax = SalesTax(0.10)
        import_tax = ImportTax(0.05)

        for item in self.items:
            item_tax = sales_tax.calculate_tax(item) + import_tax.calculate_tax(item)
            item.total_price_after_tax = (item.shelf_price + item_tax) * item.quantity

            self.total_tax_amount += item_tax * item.quantity
            self.total_amount += item.total_price_after_tax
