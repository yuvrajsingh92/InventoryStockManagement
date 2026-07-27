# Inventory Script

import csv

inventory = []

# Reading inventory file

try:
    with open("inventory.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                inventory.append({
                    "item_name": row["item_name"],
                    "current_quantity": int(row["current_quantity"]),
                    "reorder_threshold": int(row["reorder_threshold"])
                })

            except Exception as e:
                print(f"Skipping invalid row: {e}")

except FileNotFoundError:
    print("Error: inventory.csv not found.")
    exit()

# print(inventory)

# Finding low stock items

restock_items = []

for item in inventory:

    quantity = item["current_quantity"]
    threshold = item["reorder_threshold"]

    if quantity <= threshold:

        if quantity <= threshold * 0.25:
            priority = "Critical"
        else:
            priority = "Low"

        target_stock = threshold * 2
        suggested_order = target_stock - quantity

        restock_items.append({
            "item": item["item_name"],
            "current_stock": quantity,
            "threshold": threshold,
            "priority": priority,
            "suggested_order": suggested_order
        })

# print(restock_items)

print("\n" + "=" * 60)
print("             INVENTORY REORDER REPORT")
print("=" * 60)

if not restock_items:
    print("All inventory levels are healthy.")

else:

    for item in restock_items:

        print(f"Item            : {item['item']}")
        print(f"Current Stock   : {item['current_stock']}")
        print(f"Threshold       : {item['threshold']}")
        print(f"Priority        : {item['priority']}")
        print(f"Suggested Order : {item['suggested_order']}")
        print("-" * 60)

# Creating report

with open("restock_report.csv", "w", newline="") as file:

    fieldnames = [
        "item",
        "current_stock",
        "threshold",
        "priority",
        "suggested_order"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(restock_items)

print("\nReport saved as 'restock_report.csv'")

# Email alert

print("\n" + "=" * 60)
print("EMAIL ALERT")
print("=" * 60)

print("Subject: Inventory Restock Alert\n")

if not restock_items:
    print("All products are sufficiently stocked.")

else:

    print("The following products require restocking:\n")

    for item in restock_items:

        print(
            f"- {item['item']} | "
            f"Stock: {item['current_stock']} | "
            f"Priority: {item['priority']} | "
            f"Suggested Order: {item['suggested_order']}"
        )

print("\nEnd of Report.")