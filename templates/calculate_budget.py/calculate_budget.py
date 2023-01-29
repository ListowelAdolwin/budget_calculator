# Class for the Item object. Keeps the name, unit price, quantity and total cost of an item
class Item():
    def __init__(self, name, unit_price, quantity):
        self.unit_price = unit_price
        self.name = name
        self.quantity = quantity
        self.total = self.quantity * self.unit_price

# Function that makes the budget calculation and displays results in a tabular format
def calculate_budget():
    num_items = int(input("Please enter the number of items: "))

    budget = []

#Loop through all items and take their details
    for i in range(num_items):
        name = input("Enter item name: ")
        unit_price = int(input("Enter unit price of item: "))
        quantity = int(input("Enter quantity: "))
        print("")

        budget.append(Item(name, unit_price, quantity))

#Loop through all items and add their total to Total
    total_for_nhil = 0
    for item in budget:
        total_for_nhil += item.total

    nhil = round(total_for_nhil * 0.06, 2)

    subtotal = total_for_nhil + nhil

    vat = round(subtotal * 0.15, 2)

    grandtotal = vat + subtotal


# Display the final results in a tabular format
    print ("{:<17} {:<10} {:<15} {:<15}".format('Item','Unit Price','Quantity','Total'))
    print("")
    for item in budget:
        print ("{:<17} {:<10} {:<15} {:<15}".format(item.name, item.unit_price, item.quantity, item.total))
        print()

    print ("{:<17} {:<10} {:<15} {:<15}".format('','','Total',total_for_nhil))
    print()
    print ("{:<17} {:<10} {:<15} {:<15}".format('NHIL/GetFund','','',nhil))
    print()
    print ("{:<17} {:<10} {:<15} {:<15}".format('','','Subtotal',subtotal))
    print()
    print ("{:<17} {:<10} {:<15} {:<15}".format('VAT','','',vat))
    print()
    print ("{:<17} {:<10} {:<15} {:<15}".format('','','GrandTotal',grandtotal))

#call the function to execute the command
calculate_budget()
