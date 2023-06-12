# Task-2 Scripting
# With the same attachment, use each worksheet as a CSV file and write a script (Bash or Python) that generates the same report. Data is to be read from the CSV files not from a database.


import csv

# Read departments data from CSV
with open('departments.csv', 'r') as file:
    departments_data = list(csv.reader(file))

# Read employees data from CSV
with open('employees.csv', 'r') as file:
    employees_data = list(csv.reader(file))

# Read salaries data from CSV
with open('salaries.csv', 'r') as file:
    salaries_data = list(csv.reader(file))

# Create a dictionary to store department-wise salary data
department_salaries = {}

# Iterate through the employees data to calculate department-wise total salary and count
for row in employees_data:
    emp_id, _, dept_id = row
    salary = next((amt for emp_id, month, amt in salaries_data if emp_id == emp_id), 0)
    if dept_id in department_salaries:
        department_salaries[dept_id]['total_salary'] += int(salary)
        department_salaries[dept_id]['count'] += 1
    else:
        department_salaries[dept_id] = {'total_salary': int(salary), 'count': 1}

# Calculate average monthly salary for each department
department_averages = {}
for dept_id, data in department_salaries.items():
    average_salary = data['total_salary'] / data['count']
    department_averages[dept_id] = average_salary

# Sort the departments based on average monthly salary in descending order
sorted_departments = sorted(department_averages.items(), key=lambda x: x[1], reverse=True)

# Generate the report for top 3 departments
print("DEPT_NAME")
print("AVG_MONTHLY_SALARY (USD)")
for dept_id, average_salary in sorted_departments[:3]:
    department_name = next((name for id, name in departments_data if id == dept_id), '')
    print(department_name)
    print(average_salary)
    print()
