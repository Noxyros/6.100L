## 6.100L PSet 1: Part C
## Name: Yohan
## Collaborators: None

##############################################################
##            Get user input for initial deposit            ##
##############################################################
initial_deposit = float(input("Enter the initial deposit: "))

#############################################################
## Initialize other variables that we need for the program ##
#############################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment = portion_down_payment * cost_of_dream_home
months = 36

low, high = 0.0, 1.0
r = (low+high) / 2
steps =  0

max_amount_saved = amount_saved = initial_deposit * (1 + high / 12) ** months

############################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home ##
############################################################################################
while abs(amount_saved - down_payment) > 100:
    if max_amount_saved < down_payment:
        r = None
        break
    amount_saved = initial_deposit * (1 + r / 12) ** months
    if amount_saved > down_payment:
        high = r
    else:
        low = r
    r  = (high + low) / 2
    steps += 1

print("Best savings rate:", r)
print("Steps in bisection search:", steps)