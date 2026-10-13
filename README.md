# Restaurant Order Project

## Purpose

This Python script reads restaurant orders from a JSON file and creates:

- customers.json: customer phone numbers as keys and names as values.
- items.json: item names as keys, with each item's price and total
  quantity ordered.

## Requirements

Python 3 is required. No third-party packages are needed.

## How to run

Open a terminal in the project folder and run:

```bash
python restaurant.py example_orders.json
```

The input filename is the first positional argument. To process a
different dataset, replace example_orders.json with its filename or path.

For help:

```bash
python restaurant.py --help
```

Both output files are created in the terminal's current working
directory. Running the script again overwrites the previous outputs.

## Input format

The input is a JSON list of orders. Each order contains:

- name: customer name
- phone: customer phone number
- items: a list of items containing name and numeric price

Other fields, such as timestamp and notes, are not needed.

## Program design

- read_orders loads the JSON data.
- format_phone formats ten-digit phone numbers as xxx-xxx-xxxx.
- build_customers maps phone numbers to customer names.
- build_items collects item prices and counts each item occurrence.
- write_json writes the output dictionaries to JSON files.
- main reads the command-line argument and coordinates the program.

Repeated items within one order are counted individually.
Repeated phone numbers produce one customer entry.

The program assumes consistent prices for each item and keeps the first
price encountered. If a phone number has different customer names, it
keeps the last name encountered in the input.

## Sample results

The supplied sample contains:

- 10,000 orders
- 30 unique customers
- 19 unique items

For example, Butter Masala Dosa has 3,632 orders and Masala Dosa has
4,802 orders. These counts are calculated from the input, not hard-coded.