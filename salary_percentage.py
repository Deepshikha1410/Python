# Get the salary raise percentage from the user
raised_salary_percentage = float(input("Enter the salary per :"))

# Define the employee data
employee = {"Name": "Gaurav" , "existing_salary": 900}

# Calculate the incr salary
incremented_salary = employee["existing_salary"] * (1 + raised_salary_percentage / 100)

# Print the incr salary 
print(f"The incremented salary for {employee['Name']} is {incremented_salary} INR")