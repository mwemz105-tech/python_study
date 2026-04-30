account_type=input('Enter account type:')
transaction_amount=input('What is the amount:')
transaction_amount=float(transaction_amount)
if account_type=='Standard':
    if transaction_amount>500:
        print("Transaction exceeds the limit for standard accounts")
    else:
        print("Transaction approved")
elif account_type=='Premium':
    if transaction_amount>1000:
        print("Transaction exceeds the limit for premium accounts")
    else:
        print("Transaction approved")
else:
    print("Wrong account type")

