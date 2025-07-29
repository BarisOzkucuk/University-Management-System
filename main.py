import sqlite3
import os

def create_database():
    if os.path.exists("student.db"):
        os.remove("student.db")

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE  students (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INTEGER,
            email VARCHAR(255) UNIQUE,
            city VARCHAR(255)
        )
    """)


    cursor.execute("""
        CREATE TABLE  Courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR(255) NOT NULL,
            credits INTEGER,
            instructor VARCHAR(255)
        )
    """)



def insert_sample_data(cursor):
    students = [
            (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
            (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
            (3, 'Carol White', 12, 'carol@gmail.com', 'Boston'),
            (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
            (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]
    cursor.executemany("INSERT INTO students  VALUES (?, ?, ?, ?, ?)", students)

    courses = [
        (1, 'Python Programming', 3, 'Dr. Anderson'),
        (2, 'Web Development', 4, 'Prof. Wilson'),
        (3, 'Data Science', 3, 'Dr. Taylor'),
        (4, 'Moblie Apps', 2, 'Prof. Garcia'),
       
    ]
    cursor.executemany("INSERT INTO Courses  VALUES (?, ?, ?, ?)", courses)

    print("Sample data inserted successfully.")

def basic_sql_operations(cursor):
    # Query all students
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("All students:")
    for student in students:
        print(student)

    # Query all courses
    cursor.execute("SELECT * FROM Courses")
    courses = cursor.fetchall()
    print("\nAll courses:")
    for course in courses:
        print(course)

    # Query students by age
    cursor.execute("SELECT * FROM students WHERE age = 20")
    students_age_20 = cursor.fetchall()
    print("\nStudents with age 20:")
    for student in students_age_20:
        print(student)

    # Query courses with credits greater than 3
    cursor.execute("SELECT * FROM Courses WHERE credits > 3")
    courses_credits_gt_3 = cursor.fetchall()
    print("\nCourses with credits greater than 3:")
    for course in courses_credits_gt_3:
        print(course)

    # Query students by city
    cursor.execute("SELECT * FROM students WHERE city = 'New York'")
    students_city_ny = cursor.fetchall()
    print("\nStudents from New York:")
    for student in students_city_ny:
        print(student)
    
    # Query courses by instructor
    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    courses_instructor_dr_anderson = cursor.fetchall()
    print("\nCourses taught by Dr. Anderson:")
    for course in courses_instructor_dr_anderson:
        print(course)

    # Query students by name
    cursor.execute("SELECT * FROM students WHERE name = 'Alice Johnson'")
    student_alice = cursor.fetchone()
    print("\nStudent Alice Johnson:")
    print(student_alice)

    # Query courses by credits
    cursor.execute("SELECT * FROM Courses WHERE credits = 3")
    courses_credits_3 = cursor.fetchall()
    print("\nCourses with credits 3:")
    for course in courses_credits_3:
        print(course)

    # Query students by email
    cursor.execute("SELECT * FROM students WHERE email = 'alice@gmail.com'")
    student_alice_email = cursor.fetchone()
    print("\nStudent with email alice@gmail.com:")
    print(student_alice_email)

    # Query courses by instructor
    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    courses_instructor_dr_anderson = cursor.fetchall()
    print("\nCourses taught by Dr. Anderson:")
    for course in courses_instructor_dr_anderson:
        print(course)

    # Query students by age
    cursor.execute("SELECT * FROM students WHERE age = 20")
    students_age_20 = cursor.fetchall()
    print("\nStudents with age 20:")
    for student in students_age_20:
        print(student)
def sql_update_delete_operation(conn,cursor):
    cursor.execute("INSERT INTO students Values(6,'Baris',20,'baris@gmail.com','New York')")
    conn.commit()

    cursor.execute("UPDATE students SET age = 21 WHERE name = 'Baris'")
    conn.commit()

    cursor.execute("DELETE FROM students WHERE name = 'Baris'")
    conn.commit()

def aggregate_functions(cursor):
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()
    print(f"Total number of students: {count[0]}")

    cursor.execute("SELECT AVG(age) FROM students")
    avg_age = cursor.fetchone()
    print(f"Average age of students: {avg_age[0]}")

    cursor.execute("SELECT MIN(age) FROM students")
    min_age = cursor.fetchone()
    print(f"Minimum age of students: {min_age[0]}")

    cursor.execute("SELECT MAX(age) FROM students")
    max_age = cursor.fetchone()
    print(f"Maximum age of students: {max_age[0]}")

    cursor.execute("SELECT SUM(credits) FROM Courses")
    sum_credits = cursor.fetchone()
    print(f"Total credits of all courses: {sum_credits[0]}")


def main():
    conn, cursor = create_database()
    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_operation(conn,cursor)
        aggregate_functions(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()



if __name__ == "__main__":
    main()