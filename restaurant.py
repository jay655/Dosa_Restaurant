import argparse
import json


def read_orders(filename):
    """Load and return orders from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    """Get the input filename and load the orders."""
    parser = argparse.ArgumentParser(
        description="Process restaurant orders from a JSON file."
    )
    parser.add_argument("filename", help="Path to the orders JSON file")
    args = parser.parse_args()

    orders = read_orders(args.filename)
    print(f"Loaded {len(orders)} orders.")


if __name__ == "__main__":
    main()