students = []
subjects_offered = set()

def add_student():
    student_id = input("Student ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    subjects = input("Subjects (comma-separated): ").split(",")
    subjects = [s.strip() for s in subjects]
    subjects_offered.update(subjects)
    unique_info = (student_id, dob)
    student_data = {
        "id_dob": unique_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }
    students.append(student_data)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students available.")
    else:
        for student in students:
            sid, dob = student["id_dob"]
            print(f"Student ID: {sid} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {', '.join(student['subjects'])}")

def update_student():
    sid = input("Enter Student ID to update: ")
    for student in students:
        if student["id_dob"][0] == sid:
            print("1. Update Age\n2. Update Subjects")
            choice = input("Enter choice: ")
            if choice == "1":
                student["age"] = int(input("Enter new age: "))
                print("Age updated!")
            elif choice == "2":
                subjects = input("Enter new subjects (comma-separated): ").split(",")
                subjects = [s.strip() for s in subjects]
                student["subjects"] = subjects
                subjects_offered.update(subjects)
                print("Subjects updated!")
            return
    print("Student not found.")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for i, student in enumerate(students):
        if student["id_dob"][0] == sid:
            del students[i]
            print("Student deleted!")
            return
    print("Student not found.")

def display_subjects():
    if subjects_offered:
        print("Subjects Offered:", ", ".join(subjects_offered))
    else:
        print("No subjects available.")

def main():
    print("Welcome to the Student Data Organizer!")
    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_subjects()
        elif choice == "6":
            print("Thank you for using the Student Data Organizer!")
            break
        else:
            print("Invalid choice.")

main()
