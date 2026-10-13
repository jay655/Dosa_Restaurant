# Dosa Restaurant Orders

I made this Python project to organize the restaurant's order data into
a customer list and an item summary.

## How it works

The script reads a JSON file and loops through its orders to create:

- customers.json: customer names linked to phone numbers in xxx-xxx-xxxx format.
- items.json: each item's price and total number ordered.

If an item appears twice in one order, it is counted twice.

## How to run

You need Python 3. No extra packages are required.

Run this command in the terminal:

```bash
python restaurant.py example_orders.json
```

You can replace example_orders.json with another orders file in the same
format. Both output files are saved in the current folder and replaced
each time the script runs.

Author: Jay Mehta — jm2735