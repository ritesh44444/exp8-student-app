from pathlib import Path
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("students.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                branch TEXT NOT NULL,
                marks INTEGER NOT NULL
            )
        """)

        count = connection.execute(
            "SELECT COUNT(*) FROM students"
        ).fetchone()[0]

        if count == 0:
            connection.executemany(
                "INSERT INTO students (roll_no, name, branch, marks) VALUES (?, ?, ?, ?)",
                [
                    (101, "Aman", "CSE", 85),
                    (102, "Priya", "ECE", 91),
                    (103, "Rahul", "IT", 78),
                ],
            )


@app.route("/")
def index():
    with get_connection() as connection:
        students = connection.execute(
            "SELECT roll_no, name, branch, marks FROM students ORDER BY roll_no"
        ).fetchall()
    return render_template("students.html", students=students)


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
