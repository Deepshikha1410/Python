# Get the source,destination fare in INR from the user
source =(input("Enter source name: "))
destination =(input("Enter destination destination: "))
fare = float(input("Enter the fare in INR: "))
discount_rate = float(input("Enter the discount rate: "))


# Calculate the discount 
discount = fare *(discount_rate / 100)

#After discount the fare 
after_fare = fare - discount

# Print the result
print(f"Fare from {source} to {destination} is {fare}INR ,After applied discount of {discount_rate}% it is {after_fare} INR.")