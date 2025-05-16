
class Item:
    def __init__(self, name, shelf_price, quantity, is_imported=False, is_exempt=False):
        self.name = name
        self.shelf_price = shelf_price
        self.quantity = quantity
        self.is_imported = is_imported
        self.is_exempt = is_exempt

        self.total_price_after_tax = 0.0

