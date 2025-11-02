import json
from pathlib import Path

def print_students(students):
    for s in students:
        ln = s.get("L_Name", "")
        fn = s.get("F_Name", "")
        sid = s.get("Student_ID", "")
        em = s.get("Email", "")
        print(f"{ln}, {fn} : ID = {sid} , Email = {em}")

def main():
    data_path = Path(__file__).parent / "student.json"

    # Load original list
    with open(data_path, "r", encoding="utf-8") as f:
        students = json.load(f)

    print("=== Original Student list ===")
    print_students(students)

    # Append your own record (fictional ID + email)
    my_record = {
        "F_Name": "Natasha",
        "L_Name": "Foreman",
        "Student_ID": 99999,
        "Email": "nforeman@example.com"
    }
    students.append(my_record)

    print("\n=== Updated Student list ===")
    print_students(students)

    # Write updated list back to JSON file
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)

    print("\nstudent.json has been updated.")

if __name__ == "__main__":
    main()