# 📚 Database Basics: Tables, Rows, Columns, Primary Keys, and Foreign Keys

## 🧱 Tables
A **table** is a collection of related data stored in rows and columns. Each table typically represents a single entity or concept in the real world.

### Example:
A `Students` table might look like:

| id | name      | age | major          |
|----|-----------|-----|----------------|
| 1  | Alice     | 22  | Computer Science |
| 2  | Bob       | 24  | Mechanical Eng. |
| 3  | Charlie   | 23  | Mathematics     |

---

## 📄 Rows
Each **row** (also called a **record**) in a table represents a single instance of the entity.

- In the `Students` table, each row is one student.
- Example: The row `(1, Alice, 22, Computer Science)` is one student record.

---

## 📊 Columns
Each **column** represents an attribute or field of the entity.

- In the `Students` table:
  - `id` is the student’s identifier
  - `name` is the student’s name
  - `age` is their age
  - `major` is their field of study

---

## 🔑 Primary Key
A **primary key** is a column (or a set of columns) that uniquely identifies each row in a table.

- In `Students`, the `id` column is the primary key.
- No two rows can have the same primary key value.

```sql
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    major VARCHAR(100)
);



## 🔗 Foreign Key
A **foreign key** is a column in one table that refers to the primary key of another table. It creates a relationship between two tables.

### Example:
A `Courses` table:

| course_id | course_name     | student_id |
|-----------|------------------|------------|
| 101       | Algorithms       | 1          |
| 102       | Thermodynamics   | 2          |
| 103       | Calculus         | 3          |

- `student_id` is a **foreign key** referencing `Students.id`.
- This shows which student is enrolled in which course.

```sql
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(id)
);
