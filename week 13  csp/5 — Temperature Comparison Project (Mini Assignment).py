# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

# Asks the user for today’s temperature.
temp=int(input("Insert Temperature " \
" :"))

# Prints whether it’s cold, warm, or hot using comparison operators.
if temp > 50 and temp <= 85 :
    print(" The weather is seems to be perfect")
elif temp <= 50 and -10 < temp:
        print("its very cold, wear a jakcet!")
elif temp >= 86 and temp <= 109:
    print("Its very hot!!!!!")
else:
 print("Extreme temp warning, STAY INSIDE")

