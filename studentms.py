students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Student Name: ")
            marks = float(input("Enter Marks: "))
            students[roll] = {"Name": name, "Marks": marks}
            print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Details:")
            for roll, details in students.items():
                print(f"Roll No: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        if roll in students:
            print(f"Name: {students[roll]['Name']}")
            print(f"Marks: {students[roll]['Marks']}")
        else:
            print("Student not found!")

    elif choice == "4":
        roll = input("Enter Roll Number: ")
        if roll in students:
            marks = float(input("Enter New Marks: "))
            students[roll]["Marks"] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        roll = input("Enter Roll Number: ")
        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "6":
        if not students:
            print("No student records available.")
        else:
            topper_roll = max(students, key=lambda x: students[x]["Marks"])
            topper = students[topper_roll]
            print("\nTopper Details:")
            print(f"Roll No: {topper_roll}")
            print(f"Name: {topper['Name']}")
            print(f"Marks: {topper['Marks']}")

    elif choice == "7":
        if not students:
            print("No student records available.")
        else:
            total = sum(student["Marks"] for student in students.values())
            average = total / len(students)
            print(f"Average Marks: {average:.2f}")

    elif choice == "8":
        print(f"Total Students: {len(students)}")

    elif choice == "9":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 9.")