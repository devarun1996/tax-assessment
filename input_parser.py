from models.item import Item

EXEMPT_KEYWORDS = [
    "book",
    "chocolate",     
    "chocolates",    
    "pill",          
    "pills",   
    "headache"      
]


# raw_input = [
#         "1 book at 12.49",
#         "1 music CD at 14.99",
#         "1 chocolate bar at 0.85"
#     ]

def parse_input_lines(input_lines):
    items = []

    for line in input_lines:
        tokens = line.strip().split()
        quantity = int(tokens[0])
        is_imported = "imported" in line

        # Find the price (last token)
        price = float(tokens[-1])

        # Extract item name (everything between quantity and "at <price>")
        at_index = tokens.index("at")
        item_name = " ".join(tokens[1:at_index])

        # Check if exempted
        name_words = item_name.lower().split()
        is_exempt = any(word in EXEMPT_KEYWORDS for word in name_words)

        # Adding an entry to Item
        items.append(Item(item_name, price, quantity, is_imported, is_exempt))
        
    return items
