from collections import defaultdict, Counter

def analyze_purchases(purchases: list) -> dict:
    customer_dict = defaultdict(lambda: defaultdict(int))
    item_count = defaultdict(Counter)

    # ลูปผ่านรายการ purchases
    for cust_id, category, item in purchases:
        customer_dict[cust_id][category] += 1
        item_count[category][item] += 1

    # หาค่า most_frequent
    most_frequent = {}
    for category, counter in item_count.items():
        most_frequent[category] = counter.most_common(1)[0][0]

    # สร้าง dict ผลลัพธ์
    result = {cust_id: dict(categories) for cust_id, categories in customer_dict.items()}
    result['most_frequent'] = most_frequent

    return result


purchases = [
    ("cust1", "electronics", "laptop"),
    ("cust2", "groceries", "apple"),
    ("cust1", "electronics", "laptop"),
    ("cust1", "electronics", "mouse"),
    ("cust2", "groceries", "apple"),
    ("cust2", "groceries", "banana"),
    ("cust3", "groceries", "banana"),
    ("cust3", "groceries", "apple"),
    ("cust3", "electronics", "camera"),
]

print(analyze_purchases(purchases))
