# InventoryStockManagement

# Inventory Reorder Alert System

## Overview

The **Inventory Reorder Alert System** is a Python-based application that helps identify products that need to be restocked by comparing their current inventory levels with predefined reorder thresholds.

The program reads inventory data from a CSV file, detects low-stock items, assigns priority levels, suggests reorder quantities, generates a report, exports the report to another CSV file, and simulates an email notification.

---

## Features

- Read inventory data from a CSV file.
- Detect products that require restocking.
- Assign priority levels:
  - **Critical**
  - **Low**
- Suggest reorder quantities.
- Display a formatted inventory report.
- Export the report to `restock_report.csv`.
- Simulate an email alert for the inventory manager.
- Handle invalid data and missing files using exception handling.

---

## Technologies Used

- Python 3
- CSV Module (`csv`)
- Dictionaries
- Lists
- Loops
- Conditional Statements
- Exception Handling

---

## Project Structure

```
Inventory-Reorder-System/
│
├── inventory.csv
├── inventory_alert.py
├── restock_report.csv
└── README.md
```

---

## Input File

Create an `inventory.csv` file with the following format:

```csv
item_name,current_quantity,reorder_threshold
Laptop,15,10
Mouse,5,10
Keyboard,8,8
Monitor,2,5
USB Cable,30,20
Printer,0,5
Headphones,12,15
Charger,4,10
```

---

## How It Works

1. Reads the inventory data from `inventory.csv`.
2. Converts each row into a dictionary.
3. Compares the current stock with the reorder threshold.
4. Marks items that require restocking.
5. Assigns a priority level:
   - **Critical** if stock is less than or equal to 25% of the threshold.
   - **Low** otherwise.
6. Calculates a suggested reorder quantity.
7. Displays a formatted report.
8. Saves the report as `restock_report.csv`.
9. Simulates an email notification listing the products that require restocking.

---

## Output

Console Output:

```
============================================================
             INVENTORY REORDER REPORT
============================================================

Item            : Mouse
Current Stock   : 5
Threshold       : 10
Priority        : Low
Suggested Order : 15
------------------------------------------------------------

Report saved as 'restock_report.csv'
```

Generated File:

```
restock_report.csv
```

---

## Error Handling

The application handles:

- Missing CSV file (`FileNotFoundError`)
- Invalid numeric values (`ValueError`)
- Missing CSV columns (`KeyError`)

Invalid rows are skipped without stopping the program.

---

## Future Improvements

- Send real email notifications using SMTP.
- Add a graphical user interface (GUI).
- Store inventory data in a database.
- Build a web version using Flask or Django.
- Add logging for inventory updates.

---

## Yuvraj Singh 
Email : ayuvraj929@gmail.com

**Yuvraj Singh**

Python Developer | Learning Backend Development

GitHub: https://github.com/your-github-username
LinkedIn: https://linkedin.com/in/your-linkedin-profile
