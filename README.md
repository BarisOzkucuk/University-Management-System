# 🎓 Student & Course Management System (Python & SQLite)

A backend automation script developed in **Python** to demonstrate database management fundamentals. This project utilizes the **SQLite3** library to perform advanced SQL operations, including **Aggregate Functions**, **Transaction Management**, and **Bulk Insertions**, without relying on ORMs.

## 🗄️ Overview

This project simulates a university database system. It programmatically creates a relational database environment to manage students and courses, demonstrating how to execute raw SQL queries for data analysis and manipulation.

* **Tech Stack:** Python 3.x
* **Database:** SQLite (Embedded)
* **Key Concepts:** CRUD, Aggregate Functions (AVG, SUM, COUNT), Transaction Control.

## 🚀 Features

### 1. Database & Table Management
* **Auto-Initialization:** Checks and resets the workspace by recreating `student.db` on every run.
* **Multi-Table Structure:** Manages two distinct entities:
    * `Students` (ID, Name, Age, Email, City)
    * `Courses` (ID, Course Name, Credits, Instructor)

### 2. Advanced Data Operations
* **Bulk Insertion:** Uses `executemany()` to insert multiple records efficiently in a single batch.
* **Complex Queries:** Filters data based on specific criteria (e.g., "Credits > 3", "Students from New York").
* **Transaction Safety:** Implements `conn.commit()` to ensure data integrity during Insert/Update/Delete operations.

### 3. Data Analysis (Aggregates)
The system performs on-the-fly statistical analysis using SQL aggregate functions:
* **COUNT:** Calculates total registered students.
* **AVG:** Determines the average age of students.
* **MIN/MAX:** Identifies the youngest and oldest students.
* **SUM:** Calculates the total credit load of all courses.

## 🛠️ Technical Highlights

This project serves as a proof-of-concept for:

* **Raw SQL Proficiency:** demonstratred through direct usage of `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `WHERE` clauses.
* **Cursor Management:** Proper handling of database cursors for fetching results (`fetchone`, `fetchall`).
* **Error Handling:** robust `try-except-finally` blocks to manage database connections and ensure resources are closed properly.

## 💻 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/BarisOzkucuk/student-database-project.git](https://github.com/BarisOzkucuk/student-database-project.git)
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd student-database-project
    ```
3.  **Run the script:**
    ```bash
    python main.py
    ```
    *Output will be displayed in the terminal and a `student.db` file will be created.*

## 📂 Project Structure

```text
student-database-project/
├── main.py           # Core script containing all SQL logic
├── student.db        # Generated database file (created at runtime)
├── .gitignore        # Git configuration
└── README.md         # Documentation

ℹ️ Acknowledgements
This project is part of the Python Bootcamp curriculum by Atıl Samancıoğlu. Refactored and expanded by Barış Özküçük to include aggregate functions and course management logic.
