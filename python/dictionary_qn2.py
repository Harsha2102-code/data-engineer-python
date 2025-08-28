#  You have a list of transactions. Write a function to return the top 2 customers with the highest total spend.

# transactions = [
#     {"cust_id": 1, "amount": 200},
#     {"cust_id": 2, "amount": 500},
#     {"cust_id": 1, "amount": 300},
#     {"cust_id": 3, "amount": 400},
#     {"cust_id": 2, "amount": 100},
# ]


# Expected output (order doesn’t matter but amounts correct):

# [(2, 600), (1, 500)] 
def high_spend(transactions,N):
    cust={}
    for transact in transactions:
        cust[transact['cust_id']]=cust.get(transact['cust_id'],0)+transact['amount']
    top2 = sorted(cust.items(), key=lambda x: x[1], reverse=True)[:N]
    return top2

transactions = [
    {"cust_id": 1, "amount": 200},
    {"cust_id": 2, "amount": 500},
    {"cust_id": 1, "amount": 300},
    {"cust_id": 3, "amount": 400},
    {"cust_id": 2, "amount": 100},
]
N=int(input("Enter N: "))
print(high_spend(transactions,N))

