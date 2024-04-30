# Get the height in centimeters from the user
height_cm = float(input("Enter height in centimeters: "))

# Convert centimeters to inches
height_inch = height_cm / 2.54

# Calculate the height in feet and inches
height_feet = float(height_inch / 12)
height_inches = int(height_inch % 12)

# Print the result
print(f"Your height is {height_feet} feet and {height_inches} inches.")