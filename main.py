# main.py
from models.receipt import Receipt
from models.receipt import Receipt
from input_parser import parse_input_lines


def main():
    # Example raw input (this would be replaced or extended based on actual use)
    # raw_input = [
    #     "1 book at 12.49",
    #     "1 music CD at 14.99",
    #     "1 chocolate bar at 0.85"
    # ]

    print("Enter your shopping items one by one (e.g., '1 imported bottle of perfume at 47.50').")
    print("Type 'done' when finished:\n")

    raw_input = []
    while True:
        line = input()
        if line.strip().lower() == 'done':
            break
        if line.strip():
            raw_input.append(line)

    # Parse the input into Item objects
    items = parse_input_lines(raw_input)

    # Create a Receipt
    receipt = Receipt(items)

    # Calculate taxes and totals
    receipt.apply_taxes_and_calculate_totals()

    # Print the receipt output
    for item in receipt.items:
        print(f"{item.quantity} {item.name}: {item.total_price_after_tax:.2f}")

    print(f"Sales Taxes: {receipt.total_tax_amount:.2f}")
    print(f"Total: {receipt.total_amount:.2f}")


if __name__ == "__main__":
    main()
