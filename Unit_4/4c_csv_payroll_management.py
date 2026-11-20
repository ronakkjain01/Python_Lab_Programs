import csv

n = int(input("Enter number of employees: "))
with open("payroll.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Employee ID",
        "Name",
        "Basic Salary",
        "Allowance",
        "Deduction",
        "Net Salary"
    ])
    for i in range(n):
        print("\nEnter Employee Details")
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        basic = float(input("Enter Basic Salary: "))
        allowance = float(input("Enter Allowance: "))
        deduction = float(input("Enter Deduction: "))
        net_salary = basic + allowance - deduction
        writer.writerow([
            emp_id, name, basic,
            allowance, deduction, net_salary
        ])
print("\n--- PAYROLL RECORDS ---")
with open("payroll.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
