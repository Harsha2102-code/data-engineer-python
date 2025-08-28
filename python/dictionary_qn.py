"""Question2: List & Dictionary Manipulation"""
# List & Dictionary Manipulation

# You have a list of orders:

# orders = [
#     {'order_id': 1, 'customer_id': 101, 'amount': 500},
#     {'order_id': 2, 'customer_id': 102, 'amount': 300},
#     {'order_id': 3, 'customer_id': 101, 'amount': 200},
#     {'order_id': 4, 'customer_id': 103, 'amount': 700},
#     {'order_id': 5, 'customer_id': 102, 'amount': 100},
# ]


# Task: Write Python code to calculate total amount per customer and return a dictionary like:

# {101: 700, 102: 400, 103: 700}

def total_amount_per_customer(orders):

    # cust_id={orders[0]['customer_id']:orders[0]['amount']}
    # for i in range(1,len(orders)):
    #     if orders[i]['customer_id']  not in cust_id:
    #         cust_id[orders[i]['customer_id']]= orders[i]['amount']
    #     else:
    #         cust_id[orders[i]['customer_id']]= cust_id[orders[i]['customer_id']]+orders[i]['amount']
    # return cust_id
    cust_id = {}
    for order in orders:
        cust_id[order['customer_id']] = cust_id.get(order['customer_id'], 0) + order['amount']
    return cust_id  

orders= [
    {'order_id': 1, 'customer_id': 101, 'amount': 500},
    {'order_id': 2, 'customer_id': 102, 'amount': 300},
    {'order_id': 3, 'customer_id': 101, 'amount': 200},
    {'order_id': 4, 'customer_id': 103, 'amount': 700},
    {'order_id': 5, 'customer_id': 102, 'amount': 100},
]
print(total_amount_per_customer(orders))


    