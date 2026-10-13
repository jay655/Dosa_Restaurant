import argparse
import json


def read_orders(filename):
    """Load and return orders from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def format_phone(phone):
    """Format a ten-digit phone number as xxx-xxx-xxxx."""
    digits = "".join(
        character for character in str(phone)
        if character in "0123456789"
    )

    if len(digits) != 10:
        raise ValueError(f"Expected a ten-digit phone number: {phone}")

    return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"


def build_customers(orders):
    """Map customer phone numbers to customer names."""
    customers = {}

    for order in orders:
        phone = format_phone(order["phone"])
        customers[phone] = str(order["name"])

    return customers


def write_json(filename, data):
    """Save data to a readable JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        file.write("\n")

def main():
    """Get the input filename and load the orders."""
    parser = argparse.ArgumentParser(
        description="Process restaurant orders from a JSON file."
    )
    parser.add_argument("filename", help="Path to the orders JSON file")
    args = parser.parse_args()

    orders = read_orders(args.filename)
    print(f"Loaded {len(orders)} orders.")

    customers = build_customers(orders)
    write_json("customers.json", customers)
    print(f"Created customers.json with {len(customers)} customers.")


if __name__ == "__main__":
    main()