attendance = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("\nEnter student name: ")
    status = input("Enter attendance (Present/Absent): ")
    attendance[name] = status
print("\n--- ATTENDANCE REPORT ---")
present = 0
absent = 0
for name, status in attendance.items():
    print(name, ":", status)
    if status.lower() == "present":
        present += 1
    else:
        absent += 1
print("\nTotal Present:", present)
print("Total Absent:", absent)
print("Total Students:", n)
