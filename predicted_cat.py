import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change this to your MySQL username
        password=""  # Change this to your MySQL password
    )

def create_database():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS cat")
    db.close()

def connect_to_cat():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change this to your MySQL username
        password="",  # Change this to your MySQL password
        database="cat"
    )

def create_table():
    db = connect_to_cat()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            regno VARCHAR(20) PRIMARY KEY,
            names VARCHAR(100) NOT NULL
        )
    """)
    db.close()

def register_student():
    db = connect_to_cat()
    cursor = db.cursor()
    regno = input("Enter Registration Number: ")
    names = input("Enter Student Name: ")
    try:
        cursor.execute("INSERT INTO student (regno, names) VALUES (%s, %s)", (regno, names))
        db.commit()
        print("Student registered successfully!")
    except mysql.connector.IntegrityError:
        print("Error: Registration number already exists.")
    db.close()

def view_students():
    db = connect_to_cat()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    if students:
        print("\nRegistered Students:")
        for student in students:
            print(f"Reg No: {student[0]}, Name: {student[1]}")
    else:
        print("No students found.")
    db.close()

def update_student():
    db = connect_to_cat()
    cursor = db.cursor()
    regno = input("Enter Registration Number of student to update: ")
    new_name = input("Enter New Name: ")
    cursor.execute("UPDATE student SET names = %s WHERE regno = %s", (new_name, regno))
    db.commit()
    if cursor.rowcount:
        print("Student record updated successfully!")
    else:
        print("No student found with that Registration Number.")
    db.close()

def delete_student():
    db = connect_to_cat()
    cursor = db.cursor()
    regno = input("Enter Registration Number of student to delete: ")
    cursor.execute("DELETE FROM student WHERE regno = %s", (regno,))
    db.commit()
    if cursor.rowcount:
        print("Student record deleted successfully!")
    else:
        print("No student found with that Registration Number.")
    db.close()

def main():
    create_database()
    create_table()
    while True:
        print("\nStudent Management System")
        print("1. Register Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
