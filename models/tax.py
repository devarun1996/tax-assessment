import math


def round_up_tax(value):
    # Round up to nearest 0.05
    return math.ceil(value * 20) / 20.0


class Tax:
    def __init__(self, rate):
        self.rate = rate

    def calculate(self, item):
        raise NotImplementedError("Subclasses should implement this!")


class SalesTax(Tax):
    def calculate(self, item):
        if item.is_exempt:
            return 0.0
        return round_up_tax(item.shelf_price * self.rate)


class ImportTax(Tax):
    def calculate(self, item):
        if item.is_imported:
            return round_up_tax(item.shelf_price * self.rate)
        return 0.0
