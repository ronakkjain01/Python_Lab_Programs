while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")
        with open("students.txt", "a") as file:
            file.write(roll + "," + name + "," + marks + "\n")
        print("Student record added successfully!")
    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                print("\n--- STUDENT RECORDS ---")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No student records found!")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
