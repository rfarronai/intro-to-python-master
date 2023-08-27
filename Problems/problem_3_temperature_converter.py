"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""
# Ask for a temperature in Fahrenheit
temp_f = float(input("Temp in F: "))

# Calculate it in Celsius
temp_c = (temp_f - 32) * 5 / 9

# Tell the user what it is
print(f"Temp in C: {round(temp_c, 2)}")
