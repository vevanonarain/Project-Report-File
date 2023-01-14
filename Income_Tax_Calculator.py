salary = int(input("Enter your salary(including deductions) per annum: "))

if salary <= 250000:
    print("You don't have to pay any tax!")

if salary >= 250001 and salary <= 500000:
    print(f"You have to pay Rupees {(salary - 250000) * 0.05} for income tax")

if salary >= 500000 and salary <= 750000:
    print(f"You have to pay Rupees {12500 + ((salary - 500000) * 0.10)} for income tax")

if salary >= 750001 and salary <= 1000000:
    print(f"You have to pay Rupees {37500 + ((salary - 750000) * 0.15)} for income tax")

if salary >= 1000001 and salary <= 1250000:
    print(f"You have to pay Rupees {75000 + ((salary - 1000000) * 0.20)} for income tax")

if salary >= 1250001 and salary <= 1500000:
    print(f"You have to pay Rupees {125000 + ((salary - 1250000) * 0.25)} for income tax")

if salary >= 1500000:
    print(f"You have to pay Rupees {187500 + ((salary - 1500000) * 0.30)} for income tax")