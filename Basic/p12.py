# Calculate income tax
# Calculate income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:

# For example, suppose the income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000



n = int(input("Enter income: "))

if n > 20000:
    print("income tax: " ,((n-20000)*0.2) + (10000*0.1))
elif n > 10000:
    print("income tax: " ,(10000*0.1))
else:
    print("no income tax")