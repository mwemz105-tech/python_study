age=input('Whats your age:')
age=int(age)
if age>=18:
    licence=input('Do you have a driving liscence:')
    if licence=='yes':
        print("Eligible to drive")
    else:
        print("Not eligible to drive")
else:
    print("you are too young to drive")

credit_score=input('Whats your credit score:')
annual_income=input('Whats your annual income:')
credit_score=float(credit_score)
annual_income=float(annual_income)
if credit_score>=700:
    if annual_income>=50000:
        print("Loan approved")
    else:
        print("Income requiremennt not met")
else:
    print("Credit score too low")
