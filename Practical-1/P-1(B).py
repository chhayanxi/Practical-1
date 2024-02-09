# Input principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the simple interest
print("Simple Interest:", simple_interest)
