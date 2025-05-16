from models.item import Item


EXEMPT_KEYWORDS = [
    "book",
    "chocolate",     
    "chocolates",    
    "pill",          
    "pills",   
    "headache"      
]


def parse_input_lines(input_lines):
    items = []

    for line in input_lines:
        try:

            tokens = line.strip().split()
            if len(tokens) < 4:  # minimal length check (e.g. "1 book at 12.49")
                continue

            quantity = int(tokens[0])
            is_imported = "imported" in line

            # Find the price (last token)
            price = float(tokens[-1])

            # Extract item name (everything between quantity and "at <price>")
            if "at" not in tokens:
                continue  # skip line if 'at' not found

            at_index = tokens.index("at")
            if at_index <= 1:  # no name found between quantity and 'at'
                continue

            item_name = " ".join(tokens[1:at_index])

            # Check if exempted
            name_words = item_name.lower().split()
            is_exempt = any(word in EXEMPT_KEYWORDS for word in name_words)

            # Adding an entry to Item
            items.append(Item(item_name, price, quantity, is_imported, is_exempt))


        except (ValueError, IndexError):
            continue
        
    return items
