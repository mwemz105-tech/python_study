# Q1
litres = float(input("Enter the number of litres purchased: "))
        
if litres > 25:
    print("  FREE car wash ")
elif litres > 15:
    print("FREE drink and snack")
elif litres > 10:
    print("FREE shirt")
else:
    print("Purchase more than 10 litres to qualify for rewards!")

print("litres")



# Q2 Network Speed Performance Classifier

speed = float(input("Enter network speed in Mbps: "))
        
if speed < 0:
            print("Invalid: Speed cannot be negative!")
elif speed < 5:
            print("PERFORMANCE: POOR - Very slow connection")
elif speed < 25:
            print("PERFORMANCE: GOOD - Acceptable for browsing")
elif speed < 100:
            print("PERFORMANCE: VERY GOOD - Suitable for streaming")
else:
            print("PERFORMANCE: EXCELLENT - High-speed connection")
            
    
print("speed")


# Q3 

total_bill = float(input("Enter the total bill amount: $"))
num_people = int(input("Enter the number of people: "))
        
# Input validation
if total_bill <= 0:
    print("Error: Bill amount must be positive!")
elif num_people <= 0:
    print("Error: Number of people must be at least 1!")
else:
    amount_per_person = total_bill / num_people
print(f" Bill Summary:")
print(f"Total bill: ${total_bill:.2f}")
print(f"Number of people: {num_people}")
print(f"Each person pays: ${amount_per_person:.2f}")
            


