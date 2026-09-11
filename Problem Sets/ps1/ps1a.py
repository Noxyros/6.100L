## 6.100L PSet 1: Part A
## Name: Yohan
## Collaborators: None

#############################################################################
## Get user input for yearly_salary, portion_saved, and cost_of_dream_home ##
#############################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: .")) / 100
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#############################################################
## Initialize other variables that we need for the program ##
#############################################################
portion_down_payment = 0.25
down_payment = portion_down_payment * cost_of_dream_home
amount_saved = 0
r = 0.05
months = 0
percentage_of_monthly_salary = (yearly_salary / 12) * portion_saved

########################################################################################
## Determine how many months would it takes to get the down payment of the dream home ##
########################################################################################
while amount_saved <  down_payment:
    amount_saved += amount_saved  * (r / 12)
    amount_saved += percentage_of_monthly_salary
    months += 1

print("Number of months:", months)