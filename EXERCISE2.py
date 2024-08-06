inventory = [["Apple",50,0.75],
             ["Banana", 100, 0.50],
             ["Orange", 75,0.80]]

def update_inventory(inventory, item_name,quanity_sold):
    for item in inventory:
        if item_name == item[0]:
            item[1] = item[1] - quanity_sold

# update_inventory(inventory,"Banana", 20)

def calculate_total_value(inventory):
    total = 0
    total_sum = 0
    for i in inventory:
        for item in i:
           total = item[1] * item[2]
        total_sum = total_sum+total
    return total_sum

print(calculate_total_value(inventory))

# print(inventory)