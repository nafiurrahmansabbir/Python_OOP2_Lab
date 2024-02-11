principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the number of years: "))

interest = (principal * rate * time) / 100

print(f"Your interest is {interest}")