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

```












# Normalization:
    basically normalization is a process to organize data in database and reduce and remove redundency or duplication data in table.

# why do we need noralization?

    normalization need for fixed insert anomaly, update anomaly and delete anomaly.

    insert anomaly is when  insert new data in table only for two column not for every columns then other columns is empty .
    update anomaly is when update data for one column but this data is in multiple row then update every row column for this data.
    delete anomaly is when delete row then somedata is deleted forever and not back again..which is need in future.

    also reduce or remove redundency data in table.

    so avoid these problems we need normalization.


# denormalization table examples

| emp-id | emp-name       | contact-no   | dept.        | dept.mang        |
|-------:|:--------------:|:------------:|:------------:|:----------------:|
| 101    | John Doe       | 1234567890   | Sales        | Robert Johnson   |
| 102    | Jane Smith     | 9876543210   | Sales        | Robert Johnson   |
| 103    | Mike Brown     | 5551234567   | Marketing    | Sarah Williams   |
| 104    | Emily Davis    | 4449876543   | Marketing    | Sarah Williams   |
| 105    | Alex Johnson   | 2223334444   | IT           | David Thompson   |
| 106    | Olivia Wilson  | 1112223333   | IT           | David Thompson   |



    in above table has data redundency and if insert, update and delete data then its causes insert,updata, delete anomaly.



# basic normalization with above table how data redundency remove or reduce.

# make two tables from this one table.

# department table

| dept-id | dept-name   | dept-mang        |
|-------:|:------------|:----------------:|
| 1      | Sales       | Robert Johnson   |
| 2      | Marketing   | Sarah Williams   |
| 3      | IT          | David Thompson   |


# employee table


| emp-id | emp-name      | contact-no   | dept-id |
|-------:|:-------------:|:------------:|:------:|
| 101    | John Doe      | 1234567890   |   1    |
| 102    | Jane Smith    | 9876543210   |   1    |
| 103    | Mike Brown    | 5551234567   |   2    |
| 104    | Emily Davis   | 4449876543   |   2    |
| 105    | Alex Johnson  | 2223334444   |   3    |
| 106    | Olivia Wilson | 1112223333   |   3    |




with avobe example show how normalization organize data and reduce or remove redundency



# types of normalization
    normalization has many types like 1st form, 2nd form, 3rd form, bcnf, 4th form, 5th form etc.


# 1st normal form
    For 1st normal form,

    in a column multi values not allowed.
    column value must be domain specific.
    every column name must be unique.
    doesn't matter which order data is sorted.

# denormalize table 

| student_id | name            | course                                     |
|-----------:|:---------------:|:------------------------------------------:|
| 201        | Alice Johnson   | Math, Science, History                     |
| 202        | Bob Smith       | English, Science                           |
| 203        | Charlie Brown   | Math, Computer Science, Physics            |
| 204        | Daisy Wilson    | Biology, Chemistry                         |
| 205        | Evan Taylor     | History, English, Political Science        |
| 206        | Fiona Martinez  | Math, Physics, Chemistry, Computer Science |



# convert 1st normal form

| student_id | name            | course            |
|-----------:|:---------------:|:-----------------:|
| 201        | Alice Johnson   | Math              |
| 201        | Alice Johnson   | Science           |
| 201        | Alice Johnson   | History           |
| 202        | Bob Smith       | English           |
| 202        | Bob Smith       | Science           |
| 203        | Charlie Brown   | Math              |
| 203        | Charlie Brown   | Computer Science  |
| 203        | Charlie Brown   | Physics           |
| 204        | Daisy Wilson    | Biology           |
| 204        | Daisy Wilson    | Chemistry         |
| 205        | Evan Taylor     | History           |
| 205        | Evan Taylor     | English           |
| 205        | Evan Taylor     | Political Science |
| 206        | Fiona Martinez  | Math              |
| 206        | Fiona Martinez  | Physics           |
| 206        | Fiona Martinez  | Chemistry         |
| 206        | Fiona Martinez  | Computer Science  |


# convert 1st normal form another approch


| student_id | name            | course_1          | course_2         | course_3           | course_4          |
|-----------:|:---------------:|:-----------------:|:----------------:|:------------------:|:-----------------:|
| 201        | Alice Johnson   | Math              | Science          | History            | NULL              |  
| 202        | Bob Smith       | English           | Science          | NULL               | NULL              |
| 203        | Charlie Brown   | Math              | Computer Science | Physics            | NULL              |
| 204        | Daisy Wilson    | Biology           | Chemistry        | NULL               | NULL              |
| 205        | Evan Taylor     | History           | English          | Political Science  | NULL              |
| 206        | Fiona Martinez  | Math              | Physics          | Chemistry          | Computer Science  |



# drawback of 1st normal form
    same data in multiple rows for multiple time
    difficult to update all instance or reperated data. so problem of update anomalise.
    insert partial data leads to null value and incomplete records. problem of insert anomalise.
    deleating a row may remove vital information unintentionaly. problem of delete anomaliise.



# 2nd normal form
    for 2nd normal form

    table should be in 1st normal form
    partialy dipendency not allowed, need to reduce patially dependency.


# what is partially dependency?
    for understand partially dependency first need to know about dependency or functional dependency.

    dependency or functional dependency:  suppose one table has three columns id, name , address and id is primary key... so in this table with id i can find specific row but with name or address i can't find specific row because name or address can be duplicate. so  here name and address depend on id . so this call dependency or functional dependency.


# Functional Dependency Table Example

| id  | name        | address             |
|-----|------------|--------------------|
| 1   | John Doe   | 123 Main St        |
| 2   | Alice Smith| 456 Park Ave       |
| 3   | Bob Brown  | 789 Elm St         |
| 4   | John Doe   | 123 Main St        |
| 5   | Alice Smith| 456 Park Ave       |

## Functional Dependencies:

| Functional Dependency        | Explanation                                              |
|------------------------------|----------------------------------------------------------|
| **id → name, address**        | `id` uniquely determines both `name` and `address`.       |
| **name → address (Invalid)**  | Not valid, same name can have multiple addresses.         |
| **(name, address) → id**      | Together `name` and `address` can determine `id`.          |

## Explanation:

- `id` is the **Primary Key**, so:




partially dependency: suppose on table has student_id, name, address, course_id, course_name, credit, grade. and student_id is primary key.  also this table has composite key. partial dependency occurs using composite key..when any row identify using multiple columns then use composite key. this table composite key
is student_id and course_id. now check partial dependency in this table. non key columns course_name, credit depends on course_id  not depends on student_id...also non key columns name, address depends on student_id not course_id..so when use composite key as student_id and course_id then course_name, credit depends on composite key also name, address depends on composite key..so its called partial dependency.



# Partial Dependency Table Example

| student_id | name        | address        | course_id | course_name      | credit | grade |
|-----------:|:------------|:--------------|:---------:|:-----------------|:------:|:-----:|
| 1          | John Doe    | 123 Main St   | CSE101    | Computer Science |   3    |  A    |
| 1          | John Doe    | 123 Main St   | MTH101    | Mathematics      |   4    |  B    |
| 2          | Alice Smith | 456 Park Ave  | CSE101    | Computer Science |   3    |  B+   |
| 2          | Alice Smith | 456 Park Ave  | PHY101    | Physics          |   3    |  A-   |
| 3          | Bob Brown   | 789 Elm St    | MTH101    | Mathematics      |   4    |  A    |

---

## Functional Dependencies:

| Dependency                                         | Type                 | Explanation                                        |
|---------------------------------------------------|---------------------|----------------------------------------------------|
| **(student_id, course_id) → grade**                | Full Dependency      | Grade depends on both `student_id` & `course_id`.   |
| **student_id → name, address**                     | Partial Dependency   | `name` & `address` depend only on `student_id`.     |
| **course_id → course_name, credit**                | Partial Dependency   | `course_name` & `credit` depend only on `course_id`.|

---

## Why Partial Dependency?

- The **composite primary key** is `(student_id, course_id)`.
- Attributes like `name`, `address`, `course_name`, `credit` depend **only on part of the key**, not the full key.
- This violates **2NF (Second Normal Form)**.

---

## Solution:

To remove partial dependency:

1. Split the table:
    - **Student Table:** `student_id, name, address`
    - **Course Table:** `course_id, course_name, credit`
    - **Enrollment Table:** `student_id, course_id, grade`



# Normalized Tables (2NF)

## 🟢 Student Table

| student_id | name        | address        |
|-----------:|:------------|:--------------|
| 1          | John Doe    | 123 Main St   |
| 2          | Alice Smith | 456 Park Ave  |
| 3          | Bob Brown   | 789 Elm St    |

---

## 🟢 Course Table

| course_id | course_name       | credit |
|:--------:|:------------------|:------:|
| CSE101   | Computer Science  |   3    |
| MTH101   | Mathematics       |   4    |
| PHY101   | Physics           |   3    |

---

## 🟢 Enrollment Table

| student_id | course_id | grade |
|-----------:|:--------:|:-----:|
| 1          | CSE101   |  A    |
| 1          | MTH101   |  B    |
| 2          | CSE101   |  B+   |
| 2          | PHY101   |  A-   |
| 3          | MTH101   |  A    |

---

## 🎯 Explanation:
- **Student Table:** Stores student-specific data (no redundancy).
- **Course Table:** Stores course-specific data (no redundancy).
- **Enrollment Table:** Manages the relationship between students & courses, along with the `grade`.

All partial dependencies are removed! ✅





# 3rd Normal Form
    table should be 2nd normal form
    transitve dependency not allowed


    Transitive dependency:  In a table if any non key column depend on another non key columns then it's called transitive dependency.



## ❌ Original Table (2NF with Transitive Dependency)

| course_id | course_name        | credit | teacher_id | teacher_name |
|:--------:|:-------------------|:------:|:---------:|:------------:|
| CSE101   | Computer Science   |   3    | T01       | John Doe     |
| MTH101   | Mathematics        |   4    | T02       | Alice Smith  |
| PHY101   | Physics            |   3    | T03       | Bob Brown    |
| ENG101   | English Literature |   2    | T04       | Sarah Green  |

### 🔍 Issue:
- **Transitive Dependency:**
  - `course_id → teacher_id → teacher_name`
- Teacher name depends on `teacher_id`, not directly on `course_id`.

---



## ✅ 3rd Normal Form (3NF) Solution

### 📄 **Course Table**

| course_id | course_name        | credit | teacher_id |
|:--------:|:-------------------|:------:|:---------:|
| CSE101   | Computer Science   |   3    | T01       |
| MTH101   | Mathematics        |   4    | T02       |
| PHY101   | Physics            |   3    | T03       |
| ENG101   | English Literature |   2    | T04       |

---

### 📄 **Teacher Table**

| teacher_id | teacher_name |
|:---------:|:------------:|
| T01       | John Doe     |
| T02       | Alice Smith  |
| T03       | Bob Brown    |
| T04       | Sarah Green  |

---





# Boyce-Codd normal form
    table must be in 3rd normal form
    remove key column dependency on non key column
    remove insert,update and delete anomaly

## 🔥 Table Structure:

| student_name | course_name        | instructor_name |
|:-----------:|:-------------------|:---------------:|
| Alice       | Computer Science   | John Doe        |
| Bob         | Mathematics        | Alice Smith     |
| Charlie     | Physics            | Bob Brown       |
| David       | Computer Science   | John Doe        |
| Emma        | Mathematics        | Alice Smith     |

---

## 🎯 **Primary Key:**
- **(student_name, course_name)** → Composite Primary Key

---

## 🔍 **Dependency:**

- **Functional Dependency:**  
  `course_name → instructor_name`

---

## 🚨 **Problem:**

- **`course_name` is NOT a candidate key.**
- **Instructor depends on `course_name` alone (non-prime attribute), violating BCNF!**
- **Cource name depends on instructor_name column.here course_name is primary key. so when key column depends on non key column then its violating BCNF!**

---

## ⚠️ **Anomalies Present:**

### 1. **Insert Anomaly:**
- Cannot insert a new course & instructor without having at least one student enrolled.
  
  _Example:_  
  Can't add: course_name = "Chemistry", instructor_name = "Dr. Smith"   without a student!



---

### 2. **Update Anomaly:**
- Instructor's name appears multiple times.
- Updating instructor for a course → **must update all rows**.

_Risk:_ Forgetting some rows → **data inconsistency**.

---

### 3. **Delete Anomaly:**
- Deleting all students enrolled in a course → **lose instructor info**.

_Example:_  
If all students drop "Mathematics", **lose who teaches it!**

---

## 🛠️ **Solution (BCNF Decomposition):**

### 📄 **Student Enrollment Table:**

| student_name | course_name        |
|:-----------:|:-------------------:|
| Alice       | Computer Science    |
| Bob         | Mathematics         |
| Charlie     | Physics             |
| David       | Computer Science    |
| Emma        | Mathematics         |

---

### 📄 **Course Instructor Table:**

| course_name        | instructor_name |
|:------------------:|:--------------:|
| Computer Science   | John Doe       |
| Mathematics        | Alice Smith    |
| Physics            | Bob Brown      |

---

## ✅ **Benefits After BCNF:**

- No redundancy.
- No anomalies.
- Clean separation of **student-course** and **course-instructor** data.

---




# 📘 4th Normal Form (4NF) in Database Normalization

## 🧠 What is 4NF?

4th Normal Form is a level of database normalization that addresses **multivalued dependencies**.  
A relation is in **4NF** if:

1. It is in **Boyce-Codd Normal Form (BCNF)**.
2. It has **no multivalued dependencies** (MVDs).

---

## 🧪 Example Table (Violating 4NF)

| student_id | skill         | hobby         |
|:----------:|:-------------:|:-------------:|
| S01        | Python        | Chess         |
| S01        | Java          | Chess         |
| S01        | Python        | Painting      |
| S01        | Java          | Painting      |

---

### 🎯 Issue:
- A student can have **multiple skills** and **multiple hobbies** independently.
- This creates **multivalued dependencies**:
  - `student_id →→ skill`
  - `student_id →→ hobby`
- Every combination of skill and hobby is stored — **causing redundancy**.

---

## ⚠️ Anomalies in 4NF Violation:

### 🔁 **Insert Anomaly:**
- Cannot add a new skill or hobby independently.
- Example: Adding `"C++"` as a skill for `S01` requires pairing it with **all hobbies**.

### 🛑 **Delete Anomaly:**
- Deleting a skill-hobby pair may result in loss of unrelated information.
- Example: Deleting `(Python, Chess)` may accidentally remove knowledge of `"Python"` if it's the last occurrence.

### ✏️ **Update Anomaly:**
- If a student improves a skill (e.g., renaming `"Java"` to `"Java SE"`), this change must be updated in **every row where that skill is paired with a hobby**.
- **Risk:** Missing any row leads to **inconsistent data**.

---

## ✅ Decomposition into 4NF

### 📄 **Student Skills Table**

| student_id | skill   |
|:----------:|:-------:|
| S01        | Python  |
| S01        | Java    |

---

### 📄 **Student Hobbies Table**

| student_id | hobby     |
|:----------:|:---------:|
| S01        | Chess     |
| S01        | Painting  |

---

## ✔️ Benefits of 4NF

- Eliminates **multivalued dependencies**
- Prevents **insert, update, and delete anomalies**
- Reduces **redundancy**
- Improves **data consistency**

---

## 📌 Summary:

| Normal Form | Focus Area                   |
|-------------|------------------------------|
| 1NF         | Atomic values (no repeating groups) |
| 2NF         | No partial dependencies       |
| 3NF         | No transitive dependencies    |
| BCNF        | Every determinant is a candidate key |
| **4NF**     | No multivalued dependencies   |

---





# 📗 5th Normal Form (5NF) – Project-Join Normal Form (PJNF)

## 🧠 What is 5NF?

A relation is in **5th Normal Form (5NF)** or **Project-Join Normal Form (PJNF)** when:

1. It is already in **4NF**.
2. It cannot be **further decomposed** into two or more **smaller relations** without **loss of data** when joined back.

5NF deals with **join dependencies** and ensures **lossless join decomposition**.

---

## 🧪 Example: Table Violating 5NF

Let’s say a company stores relationships between **Consultants**, **Projects**, and **Technologies** used.

| consultant | project     | technology   |
|:----------:|:-----------:|:------------:|
| Alice      | Banking App | Java         |
| Alice      | Banking App | Python       |
| Alice      | HR System   | Java         |
| Bob        | Banking App | Java         |

---

### 🎯 Problem:
The combinations are **not truly independent**. For instance, not all combinations of `consultant-project-technology` may be valid — only specific ones are.

- You **can't split this** into just `consultant-project`, `consultant-technology`, and `project-technology` and expect to reconstruct it exactly.
- This is a **join dependency** problem → handled in **5NF**.

---

## ⚠️ Anomalies in 5NF Violation

### 🛑 Insert Anomaly:
- You cannot add that **Alice uses Python** on **HR System** without also inserting irrelevant or invalid combinations.

### ✏️ Update Anomaly:
- Updating a consultant’s skill or project may require modifying **many rows** with risk of inconsistency.

### ❌ Delete Anomaly:
- Removing one row might cause **loss of valid relationships** among other attributes.

---

## ✅ 5NF Decomposition Example

### 📄 Consultant–Project Table

| consultant | project     |
|:----------:|:-----------:|
| Alice      | Banking App |
| Alice      | HR System   |
| Bob        | Banking App |

---

### 📄 Consultant–Technology Table

| consultant | technology |
|:----------:|:----------:|
| Alice      | Java       |
| Alice      | Python     |
| Bob        | Java       |

---

### 📄 Project–Technology Table

| project     | technology |
|:-----------:|:----------:|
| Banking App | Java       |
| Banking App | Python     |
| HR System   | Java       |

---

### 🔁 When joined properly, they reproduce only **valid combinations** without redundancy.

---

## ✅ Summary of Normal Forms

| Normal Form | Handles...                     |
|-------------|--------------------------------|
| 1NF         | Atomic values                  |
| 2NF         | No partial dependencies        |
| 3NF         | No transitive dependencies     |
| BCNF        | Determinants are candidate keys |
| 4NF         | No multivalued dependencies    |
| **5NF**     | No join dependencies           |

---

## 🧩 Use Case for 5NF
- Complex many-to-many relationships with multiple attributes.
- Situations where combinations of three or more entities are only valid together.












## ACID 

# 🧪 ACID Properties in Databases

In the context of databases, **ACID** is an acronym that describes a set of properties that guarantee database transactions are processed reliably.

---

## 🔹 A — Atomicity

**Definition**: A transaction is all or nothing. If one part of the transaction fails, the entire transaction fails, and the database is left unchanged.

**Real-World Example**:  
Imagine withdrawing money from an ATM.  
- Step 1: Deduct $100 from your bank account.  
- Step 2: Dispense $100 in cash.  
If the cash doesn’t come out (Step 2 fails), the amount shouldn't be deducted (Step 1 is also rolled back).

**In a database**:
```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE cash_machine SET cash = cash - 100;

COMMIT; -- Or ROLLBACK if any update fails



## 🔹 C — Consistency

**Definition**: A transaction must bring the database from one valid state to another, maintaining data integrity.

**Real-World Example**:  
If a student is registered for a course, the number of enrolled students should be updated correctly.

**In a database**:
```sql
-- Before: 29 students enrolled
INSERT INTO enrollments (student_id, course_id) VALUES (5, 101);
-- After: 30 students enrolled
UPDATE courses SET enrolled = enrolled + 1 WHERE course_id = 101;
```
If something goes wrong, the database should not reflect an incomplete state.

## 🔹 I — Isolation

**Definition**: Concurrent transactions should not interfere with each other. Each transaction should behave as if it’s the only one running.

**Real-World Example**:  
Two users try to book the last available concert ticket at the same time. Isolation ensures that only one transaction succeeds and the other is either delayed or fails—preventing double-booking.

**In a database**:
- Without isolation: Both users see "1 ticket left" and both proceed.
- With isolation: One transaction locks the ticket record until it finishes.

---

## 🔹 D — Durability

**Definition**: Once a transaction is committed, it will remain so, even in the case of a system crash or power failure.

**Real-World Example**:  
You pay your utility bill online. Once it says "Payment Successful," the payment must remain recorded—even if your browser crashes or the server restarts.

**In a database**:
- Committed transactions are saved to non-volatile storage.
- Recovery processes ensure the data is restored after crashes.

---

## 🧠 Summary Table

| Property    | Meaning                                | Real-World Analogy                         |
|-------------|-----------------------------------------|---------------------------------------------|
| Atomicity   | All or nothing                          | ATM withdrawal that deducts but fails to deliver cash must roll back |
| Consistency | Keeps data valid across operations      | Registering a student must also update class enrollment |
| Isolation   | Transactions run without stepping on each other | Two users can't book the same plane seat simultaneously |
| Durability  | Once done, it stays done                | Paid bills don't disappear after a power outage |

---

ACID properties are the gold standard for database reliability. They ensure your applications remain consistent, reliable, and fault-tolerant—even under heavy load or unexpected crashes. 💡💽




# basic sql

# 📘 SQL SELECT Statement - Complete Guide

The `SELECT` statement is the most commonly used command in SQL. It allows you to **retrieve data from one or more tables** in a relational database.

---

## 🔹 Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```


## 🔹 To Select All Columns

To retrieve all columns from a table, use the asterisk `*`:

```sql
SELECT * FROM table_name;
```


## 🧾 Example

Assume you have a table named `employees`:

| id | name     | department | salary | hire_date  |
|----|----------|------------|--------|------------|
| 1  | Alice    | HR         | 50000  | 2020-01-15 |
| 2  | Bob      | IT         | 65000  | 2019-03-10 |
| 3  | Charlie  | IT         | 70000  | 2021-06-01 |
| 4  | Diana    | Finance    | 48000  | 2022-08-20 |

---

## ✅ Select Specific Columns

You can fetch only specific columns from a table:

```sql
SELECT name, salary FROM employees;
```



## ✅ Select Specific Columns

You can fetch only specific columns from a table:

```sql
SELECT name, salary FROM employees;
```

## 🎯 Using WHERE Clause

Filter rows based on a condition:

```sql
SELECT * FROM employees WHERE department = 'IT';
```

## 💰 WHERE with Comparison Operators

You can use operators like =, >, <, >=, <=, !=:

```sql
SELECT name, salary FROM employees WHERE salary > 60000;
```


## 📌 DISTINCT

Remove duplicates from the result:

```sql
SELECT DISTINCT department FROM employees;
```

## 🔃 ORDER BY

Sort results by one or more columns:

```sql
SELECT * FROM employees ORDER BY salary DESC;

```

## 🎯 LIMIT

Limit number of rows returned:

```sql
SELECT * FROM employees LIMIT 3;

```


## ➕ Aliases

Give a temporary name to columns or tables for better readability:

```sql
SELECT name AS employee_name, salary AS income FROM employees;

```

## 🔎 LIKE

Used for pattern matching with wildcards (%, _):

```sql
SELECT * FROM employees WHERE name LIKE 'A%';
```

## 🧮 Aggregation Functions

Functions like COUNT, AVG, MAX, MIN, SUM:

```sql
SELECT COUNT(*), AVG(salary), MAX(salary), MIN(salary), SUM(salary) FROM employees;

```

## 📚 GROUP BY

Group data for aggregate analysis:

```sql
SELECT department, COUNT(*) AS total_employees FROM employees GROUP BY department;

```

## 🧨 HAVING

Filter groups after aggregation:

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

```

## 🔗 JOIN

Combine rows from multiple tables based on a related column:

```sql
SELECT employees.name, departments.location
FROM employees
JOIN departments ON employees.department_id = departments.id;

```


## 🚀 Real World Use Case

An example combining multiple features:

```sql
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
WHERE department != 'HR'
GROUP BY department
ORDER BY avg_salary DESC;


```


## 🧠 Tips

- Use `LIMIT` during testing to avoid large outputs.
- Combine `WHERE`, `ORDER BY`, `GROUP BY` for powerful queries.
- `AS` makes results cleaner and more understandable.
- Always format and comment complex queries for maintainability.
- Use `EXPLAIN` to analyze query performance.

---

## ✅ Summary Table

| Clause       | Description                              |
|--------------|------------------------------------------|
| `SELECT`     | Choose columns to display                |
| `FROM`       | Specify table(s) to query from           |
| `WHERE`      | Filter the records                       |
| `GROUP BY`   | Group rows based on column(s)            |
| `HAVING`     | Filter groups after aggregation          |
| `ORDER BY`   | Sort the output                          |
| `LIMIT`      | Restrict number of rows returned         |

---





# SQL `UPDATE` Statement Explained

The SQL `UPDATE` statement is used to modify existing records in a table. It is one of the most commonly used Data Manipulation Language (DML) commands.

---

## 📌 Syntax

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```


## 🧾 Example

Assume you have a table named `employees`:

| id | name     | department | salary | hire_date  |
|----|----------|------------|--------|------------|
| 1  | Alice    | HR         | 50000  | 2020-01-15 |
| 2  | Bob      | IT         | 65000  | 2019-03-10 |
| 3  | Charlie  | IT         | 70000  | 2021-06-01 |
| 4  | Diana    | Finance    | 48000  | 2022-08-20 |

---



## 🎯 Update Single Row Example

```sql
UPDATE employees
SET salary = 70000
WHERE id = 2;



```


## 🔄 Update Multiple Columns

```sql
UPDATE employees
SET name = 'Charles', salary = 65000
WHERE id = 3;

```


## ❌ Update Without WHERE (Not Recommended)

```sql
UPDATE employees
SET department = 'Operations';
```

## 🛠️ Use with Subqueries

```sql
UPDATE employees
SET salary = (
    SELECT AVG(salary)
    FROM employees
    WHERE department = 'IT'
)
WHERE department = 'HR';
```






# Best Practices for Using SQL `UPDATE` Statement and Summary

---

## 🏆 Best Practices

1. **Always Use the WHERE Clause:**
   - When updating records, always ensure that a `WHERE` clause is specified. Without it, all rows in the table will be updated.
   - Example:
     ```sql
     UPDATE employees
     SET salary = 50000;
     ```
     This would update the salary of every employee in the table!

2. **Limit Updates to Small Batches:**
   - If you need to update many rows, consider doing it in smaller batches to avoid performance issues and lock contention.
   - Example:
     ```sql
     UPDATE employees
     SET salary = salary * 1.05
     WHERE department = 'IT'
     LIMIT 100;
     ```

3. **Use Transactions:**
   - For important updates, wrap them in a transaction to ensure atomicity. This means the update will either be fully applied or fully rolled back if something goes wrong.
   - Example:
     ```sql
     BEGIN TRANSACTION;
     
     UPDATE employees
     SET salary = 60000
     WHERE id = 1;
     
     COMMIT;
     ```

4. **Backup Data Before Large Updates:**
   - Before applying major changes, always make sure you have a backup of your data to prevent accidental data loss.

5. **Test Before Applying:**
   - Always test your `UPDATE` queries on a sample dataset before running them in production. This will help catch errors.

---

## 📚 Summary

- The `UPDATE` statement in SQL is used to modify existing records in a table.
- It typically includes:
  - **`SET`**: Defines which columns to update and what new values to set.
  - **`WHERE`**: Specifies which rows should be updated.
- Always ensure the **`WHERE`** clause is used to prevent unintended updates.
- Transactions provide a way to ensure that your updates are applied atomically.
- It's a good practice to backup your data before performing large updates and test changes on a smaller set first.

---


# SQL INSERT Statement

The `INSERT` statement in SQL is used to add new records to a table in the database. It is one of the most commonly used SQL operations, allowing data to be stored in relational databases.

---

## 🔹 Basic Syntax

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

##  Insert a Single Row

```sql
INSERT INTO employees (id, name, department, salary)
VALUES (1, 'John Doe', 'IT', 50000);
```

##  Insert Multiple Rows

```sql
INSERT INTO employees (id, name, department, salary)
VALUES 
  (2, 'Jane Smith', 'HR', 60000),
  (3, 'Mike Johnson', 'Finance', 70000),
  (4, 'Sara Lee', 'Marketing', 55000);
```

##  Insert Data Using Subquery

```sql
INSERT INTO new_employees (id, name, department, salary)
SELECT id, name, department, salary
FROM old_employees
WHERE department = 'IT';

```

##   Using DEFAULT Keyword

```sql
INSERT INTO employees (id, name, department, salary)
VALUES (6, 'Emily Davis', 'Finance', DEFAULT);
```


##   Insert With Auto-Increment Field
Assuming id is auto-increment:
```sql
INSERT INTO employees (name, department, salary)
VALUES ('Chris Green', 'Operations', 75000);
```


##   ✅ SQL Transaction Example for INSERT
Let's say you're inserting into two related tables: employees and salaries. You want to ensure that either both inserts succeed, or neither happens.

```sql
START TRANSACTION;

-- Insert into employees table
INSERT INTO employees (employee_id, name, department)
VALUES (101, 'Alice Johnson', 'Engineering');

-- Insert into salaries table
INSERT INTO salaries (employee_id, salary)
VALUES (101, 85000);

-- If everything is OK, commit the transaction
COMMIT;

-- If anything goes wrong (like a duplicate ID, a foreign key failure, etc.), you can roll back:

-- ROLLBACK;

```

## 🛠 Best Practices

- ✅ Ensure column values match the data types.
- ✅ Use transactions when inserting into multiple related tables.
- ✅ Use batch inserts for better performance.
- ✅ Avoid inserting duplicate data using `WHERE NOT EXISTS` or constraints.
- ✅ Sanitize input to prevent SQL injection.
- ✅ Use parameterized queries in application code (especially with Python, Java, etc.).
- ✅ Use indexes carefully — too many indexes can slow down inserts.
- ✅ Handle NULLs explicitly if needed to maintain data consistency.

---

## 📌 Summary

| Topic                        | Details                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| Add a single row            | Use `INSERT INTO table (...) VALUES (...)`                             |
| Add multiple rows           | Use multiple value sets in one query                                   |
| Insert from another table   | Use `INSERT INTO ... SELECT ... FROM`                                  |
| Use default values          | Omit column or use `DEFAULT`                                           |
| Handle auto-increment       | Omit the auto-increment column                                         |
| Best performance            | Use batch insert with transactions                                     |
| Prevent duplicates          | Use `NOT EXISTS`, `IGNORE`, or unique constraints                      |

---



# 🧾 SQL `DELETE` Statement — Explained with Examples

The `DELETE` statement is used to **remove rows** from a table in a database.

---

## 📌 Basic Syntax

```sql
DELETE FROM table_name
WHERE condition;
```


##   Delete a Specific Row
Deletes the row where the employee id is 101.
```sql
DELETE FROM employees
WHERE id = 101;

```


##    Delete Rows Based on a Condition
Deletes all orders placed before January 1, 2024.
```sql
DELETE FROM orders
WHERE order_date < '2024-01-01';
```


##   Delete All Rows (Dangerous!)
Deletes every row in the customers table. The table structure stays, but it’s empty now.

```sql
DELETE FROM customers;
```

##    Using DELETE with Subquery
Deletes all employees who work in the HR department.

```sql
DELETE FROM employees
WHERE department_id IN (
    SELECT id FROM departments WHERE name = 'HR'
);
```


##    Delete with JOIN (Vendor-Specific)
Deletes employees who belong to the Finance department.
```sql
DELETE employees
FROM employees
JOIN departments ON employees.department_id = departments.id
WHERE departments.name = 'Finance';
```



# Database relationships



# 📘 Everything About Database Relationships (With Examples)

In a relational database, **relationships** define how data in one table relates to data in another. They are fundamental to database normalization, avoiding data redundancy, and ensuring data integrity.

---

## 🔗 Why Relationships Matter

Imagine managing a university database. You wouldn’t want to store the full student info every time they enroll in a course. Instead, you'd link a **Student** table with a **Course** table through a relationship.

---

## 🔶 Types of Database Relationships

---

### 1. One-to-One (1:1)

Each row in **Table A** is linked to only one row in **Table B**, and vice versa.

**Use Case**: Storing user profile info separately from login credentials.

#### 🧾 Example:

```sql
-- Users Table
CREATE TABLE Users (
  user_id INT PRIMARY KEY,
  username VARCHAR(100)
);

-- UserProfiles Table
CREATE TABLE UserProfiles (
  profile_id INT PRIMARY KEY,
  user_id INT UNIQUE,
  bio TEXT,
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
```

Each user has one unique profile.


# 🔁 One-to-Many (1:N) Relationship in Databases

A **One-to-Many** relationship means that **one row in a table (parent)** can be associated with **many rows in another table (child)**, but **each child row refers to only one parent**.

---

## ✅ Real-World Example

### Scenario: Customers and Orders

- One customer can place multiple orders.
- Each order belongs to only one customer.

---

## 📋 Table Design

```sql
-- customers table parent
CREATE TABLE Customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);


-- orders table child
CREATE TABLE Orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  amount DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
```

The customer_id in the Orders table is a foreign key pointing to Customers.
This enforces referential integrity.


# 🔁 Many-to-Many (N:M) Relationship in Databases

A **Many-to-Many** relationship means that **one row in a table (parent)** can be associated with **many rows in another table (child)**, and **each row in the child table can also be associated with many rows in the parent table**.

---

## ✅ Real-World Example

### Scenario: Students and Courses

- A student can enroll in multiple courses.
- A course can have multiple students.

---

## 📋 Table Design

In a Many-to-Many relationship, we typically need a **junction (or bridge) table** to represent the relationship between the two entities.

```sql
--Students Table (Parent)
CREATE TABLE Students (
  student_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

-- Courses Table (Parent)
CREATE TABLE Courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(100)
);

-- Enrollments Table (Junction Table)

CREATE TABLE Enrollments (
  student_id INT,
  course_id INT,
  enrollment_date DATE,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES Students(student_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
```
The Enrollments table establishes the many-to-many relationship between Students and Courses.

Both student_id and course_id are foreign keys referencing the Students and Courses tables, respectively.


# 🔁 Self-Reference Relationship in Databases

A **Self-Reference Relationship** (also known as a **Recursive Relationship**) occurs when a table references itself. This means that a row in the table can be related to another row in the same table.

---

## ✅ Real-World Example

### Scenario: Employees and Managers

- An **employee** can have a **manager**.
- A **manager** is also an **employee**, which creates a self-referencing relationship.

In a company hierarchy, an employee can report to a manager, and that manager can report to someone higher up, forming a recursive relationship.

---

## 📋 Table Design

In a self-reference relationship, we need to use a **foreign key** that points back to the same table.

### Employees Table (Self-Referencing)

```sql
CREATE TABLE Employees (
  employee_id INT PRIMARY KEY,
  name VARCHAR(100),
  position VARCHAR(100),
  manager_id INT,
  FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);
```

manager_id is a foreign key referencing the same table (Employees) to indicate who the manager of the employee is.

The relationship is self-referential because both the employee and the manager are in the same table.




# Database joins

# SQL JOINs Explained: INNER, LEFT, RIGHT, FULL, CROSS, NATURAL, SELF

This document explains the three most commonly used SQL joins: **INNER JOIN**, **LEFT JOIN**, and **RIGHT JOIN** with simple examples and visualizations.

---

## 📘 What is a JOIN?

A `JOIN` is used in SQL to combine rows from two or more tables, based on a related column between them.

---

## 🔹 1. INNER JOIN

### ✅ Description:
Returns only the rows that have **matching values in both tables**.

### 🧾 Syntax:
```sql
SELECT *
FROM table1
INNER JOIN table2 ON table1.common_column = table2.common_column;
```


#Example: Joining Employees with Departments

We have two tables: employees and departments.

---

## 🗃️ Table 1: employees

| id | name   | department_id |
|----|--------|----------------|
| 1  | Alice  | 1              |
| 2  | Bob    | NULL           |
| 3  | Carol  | 2              |


## 🗃️ Table 2: departments

| id | name      |
|----|-----------|
| 1  | HR        |
| 2  | IT        |
| 3  | Finance   |



## inner join query example
```sql
    select e.name, d.name as department
    from employees e
    inner join departments d on e.department_id = d.id;
```

## result

| name | department      |
|------|-------------------|
| Alice  | HR            |
| Carol  | IT            |



Only employees with matching department IDs are shown.



## 🔹 2. LEFT JOIN (LEFT OUTER JOIN)

### ✅ Description:
Returns all records from the left table, and matched records from the right table. Non-matches on the right are filled with NULL.

### 🧾 Syntax:
```sql
SELECT *
FROM table1
LEFT JOIN table2 ON table1.common_column = table2.common_column;

```



## left join query example
```sql
    SELECT e.name, d.name AS department
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

```

## result

| name | department      |
|------|-------------------|
| Alice  | HR            |
| Bob  | NULL            |
| Carol | IT |


Includes Bob, even though he has no department.




## 🔹 3. RIGHT JOIN (RIGHT OUTER JOIN)

### ✅ Description:
Returns all records from the right table, and matched records from the left table. Non-matches on the left are filled with NULL.

### 🧾 Syntax:
```sql
SELECT *
FROM table1
RIGHT JOIN table2 ON table1.common_column = table2.common_column;

```



## left join query example
```sql
    SELECT e.name, d.name AS department
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```

## result

| name | department      |
|------|-------------------|
| Alice  | HR            |
| Carol | IT |


If a department had no employee, it would still appear with NULL in name.


# 🧠 SQL JOIN Summary Table

This table summarizes the behavior of the most common types of SQL JOINs.

| JOIN Type   | Returns                                             |
|-------------|-----------------------------------------------------|
| INNER JOIN  | Only matched rows from both tables                  |
| LEFT JOIN   | All rows from the left table + matched rows from right |
| RIGHT JOIN  | All rows from the right table + matched rows from left |

---

## 💡 Quick Tips

- Use **INNER JOIN** when you only need related data.
- Use **LEFT JOIN** to include everything from the left table, even if unmatched.
- Use **RIGHT JOIN** to include everything from the right table, even if unmatched.




# 🔄 SQL FULL OUTER JOIN

A `FULL OUTER JOIN` combines the results of both `LEFT JOIN` and `RIGHT JOIN`. It returns **all rows** from both tables, and matches rows where possible. If there's no match, the result will contain `NULL` for the missing side.

---

## 🧾 Syntax

```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.common_column = table2.common_column;
```



## full join query example
```sql
    SELECT e.name AS employee, d.name AS department
    FROM employees e
    FULL OUTER JOIN departments d
    ON e.department_id = d.id;
```

## result

| name | department      |
|------|-------------------|
| Alice  | HR            |
| Carol | IT |
| NULL | Finance |
| Bob | NULL |



---

## 👍 Pros of FULL OUTER JOIN

- ✅ **Comprehensive Data Retrieval**: Returns all matched and unmatched rows from both tables.
- ✅ **Data Audit & Reconciliation**: Great for identifying mismatched or orphaned data on either side.
- ✅ **Combines LEFT and RIGHT JOIN Results**: Useful for complex reporting scenarios where both unmatched records are important.

---

## 👎 Cons of FULL OUTER JOIN

- ❌ **Not Supported in MySQL**: MySQL doesn't have native `FULL OUTER JOIN`; workarounds are needed using `UNION`.
- ❌ **May Include Many NULLs**: If many unmatched rows exist, result may contain lots of `NULL` values.
- ❌ **Performance Overhead**: More resource-intensive than `INNER JOIN`, especially on large datasets with lots of unmatched rows.

---

## 🚀 When to Use FULL OUTER JOIN

You should use `FULL OUTER JOIN` when:

- You want **all rows** from both tables, **with or without matches**.
- You need to identify:
  - Orphan records (e.g. employees with no department or departments with no employees).
  - Differences or gaps in two datasets (e.g. expected vs actual, inventory vs sales).
- You are building a **data validation, audit, or sync report**.

---




# ✖️ SQL CROSS JOIN Explained

A `CROSS JOIN` returns the **Cartesian product** of two tables. That means it pairs **every row** from the first table with **every row** from the second table.

---

## 🧾 Syntax

```sql
SELECT *
FROM table1
CROSS JOIN table2;
```


---

## 🧠 Key Point

A `CROSS JOIN` produces the **Cartesian product** of two tables:

- Each row from the first table is **combined with every row** from the second table.
- Result size = rows in Table A × rows in Table B.
- No `ON` clause is needed.

---

## 📦 Example: Employees × Departments

We want to pair each employee with **every department** to generate all possible assignments.

---

### 🗃️ Table 1: employees

| id | name   |
|----|--------|
| 1  | Alice  |
| 2  | Bob    |

---

### 🗃️ Table 2: departments

| id | name      |
|----|-----------|
| 1  | HR        |
| 2  | IT        |
| 3  | Finance   |

---

### 🔍 SQL Query

```sql
SELECT e.name AS employee, d.name AS department
FROM employees e
CROSS JOIN departments d;
```


## ✅ Result

| employee | department |
|----------|------------|
| Alice    | HR         |
| Alice    | IT         |
| Alice    | Finance    |
| Bob      | HR         |
| Bob      | IT         |
| Bob      | Finance    |

---

## ✅ Result of a CROSS JOIN

A `CROSS JOIN` returns the **Cartesian product** of two tables:

- If Table A has `m` rows and Table B has `n` rows,
- The result will have **m × n rows**.

### Example:

If we CROSS JOIN:

- 2 employees
- 3 departments

➡️ The result will have **2 × 3 = 6 rows**, showing every possible pairing.

---

## 🚀 Use Cases

- Generating **all possible combinations** of two datasets
- Creating **scheduling matrices** (e.g., employees × shifts)
- Building **test data** with multiple dimension combinations
- Modeling **product variants** (e.g., sizes × colors)

---

## 👍 Pros of CROSS JOIN

- ✅ Simple way to produce **all combinations** between two datasets
- ✅ No `ON` condition required
- ✅ Ideal for **combinatorial** logic or brute-force testing
- ✅ Useful in **pivot** or **matrix-style** reports

---

## 👎 Cons of CROSS JOIN

- ❌ **Result size grows quickly** with larger tables
- ❌ **Performance hit** on big datasets — use with filters where possible
- ❌ **Can be misused accidentally** if `JOIN` is used without `ON`
- ❌ Not commonly needed in everyday queries — often for specific modeling tasks

---



# 🌿 SQL NATURAL JOIN

A `NATURAL JOIN` automatically joins two tables **based on columns with the same name and data type** in both tables. It **eliminates the need for an explicit `ON` clause**.

---

## 🧾 Syntax

```sql
SELECT *
FROM table1
NATURAL JOIN table2;
```

✅ No ON clause is required. The database finds and uses all common columns automatically.

### ❗ To use NATURAL JOIN, we rename columns to match:

To make a `NATURAL JOIN` work, the **column names must be identical** in both tables.

For example, let's rename the `id` column in the `departments` table to `department_id` to match the `employees` table:

```sql
-- Rename column to match
ALTER TABLE departments RENAME COLUMN id TO department_id;
```

## 🧾 Natural join SQL Query

```sql
SELECT name, department_name
FROM employees
NATURAL JOIN departments;
```

## ✅ Result Table

| name  | department_name |
|-------|------------------|
| Alice | HR               |
| Bob   | IT               |
| Carol | Finance          |

- The `NATURAL JOIN` automatically matches rows from the two tables based on the **`department_id`** column.
- No need for an explicit `ON` clause; the join is handled automatically by matching columns with the same name.



## 🚀 Use Case

Use a `NATURAL JOIN` when:
- You have **consistent and standardized column names** across your tables.
- You need a **quick and simple join** without specifying join conditions.
- Ideal for **ad-hoc queries** where you want to join tables based on common columns, especially when column names are clear and predictable.
- Great for **exploratory data analysis** where you need to quickly combine related tables without worrying about manually specifying matching columns.

---

## 👍 Pros of NATURAL JOIN

- ✅ **Less code**: No need to specify `ON` clause — automatically matches columns with the same name and type.
- ✅ **Simple syntax**: Clean and concise, especially for straightforward joins.
- ✅ **Automatic column matching**: Helps when working with standardized tables that follow consistent naming conventions.
- ✅ **Faster to write**: Perfect for rapid development or quick data exploration when you know the schema is well-structured.

---

## 👎 Cons of NATURAL JOIN

- ❌ **Implicit logic**: The join condition is automatic, which can lead to unintended columns being matched if multiple columns share the same name.
- ❌ **Column name dependency**: Requires **exact column name matches** and identical data types, which may not always be the case.
- ❌ **Hard to debug**: If the schema changes or column names change, the `NATURAL JOIN` may silently fail or produce incorrect results.
- ❌ **Lack of control**: No fine-grained control over which columns are being used for the join, which may cause issues in more complex scenarios.

---



# 🔄 SQL Self Join

A **Self Join** is a regular join, but it joins a table with itself. This is useful when you need to compare rows within the same table, such as when an entity is related to another instance of itself.

---

## 🧾 Syntax

```sql
SELECT a.column_name, b.column_name
FROM table_name a
JOIN table_name b
ON a.common_column = b.common_column;
```

In this syntax, the table is aliased as a and b, which are used to distinguish between the two instances of the same table.


## 📦 Example: Employee Manager Relationship

Imagine we have an `employees` table where each employee has a `manager_id` pointing to their manager's `id` in the same table.

### 🗃️ employees

| id  | name   | manager_id |
|-----|--------|------------|
| 1   | Alice  | NULL       |
| 2   | Bob    | 1          |
| 3   | Carol  | 1          |
| 4   | Dave   | 2          |

- `Alice` is the **manager** (no manager).
- `Bob` and `Carol` report to **Alice**.
- `Dave` reports to **Bob**.

---

## 🔍 SQL Query for Self Join

We want to find out who manages whom.

```sql
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.id;
```

This query joins the employees table with itself, using aliases e1 and e2 to distinguish between the two instances of the same table.


## ✅ Result

| employee | manager |
|----------|---------|
| Bob      | Alice   |
| Carol    | Alice   |
| Dave     | Bob     |

In this result:
- `Bob` and `Carol` report to `Alice`.
- `Dave` reports to `Bob`.

---

## 🚀 Use Case

Use a **Self Join** when:
- **Hierarchical Data**: When you need to model relationships such as **employee-manager** or **parent-child** in a single table.
- **Comparing Rows**: When you need to compare rows within the same table, for instance, finding employees who have the same manager or calculating relationships between the same type of entities.
- **Recursive Relationships**: When you have recursive relationships, such as family trees, folder structures, or organizational hierarchies.

---


---

## 👍 Pros of Self Join

- ✅ **Comparing Rows within the Same Table**: Self joins allow you to compare rows within the same table without needing multiple copies of the data.
- ✅ **Hierarchical Data**: Ideal for querying **recursive relationships** such as parent-child structures, like employees and managers, or products and categories.
- ✅ **Efficiency in Simple Cases**: When used properly, a self join can be an efficient solution for certain types of queries, like finding employees under the same manager.
- ✅ **Simplicity for Basic Queries**: For small tables or simple hierarchical structures, self joins can simplify the query logic.

---

## 👎 Cons of Self Join

- ❌ **Complexity in Large Datasets**: As the dataset grows larger, self joins can become more complex and harder to manage, especially if you have many relationships or nested joins.
- ❌ **Performance Overhead**: Self joins may lead to performance issues if the table is large, as the join essentially creates a Cartesian product between rows.
- ❌ **Alias Confusion**: Using aliases (`e1`, `e2`) to distinguish between instances of the same table can be confusing, especially in more complex queries.
- ❌ **Not Always Intuitive**: Self joins can be difficult to understand, especially when there are multiple levels of hierarchy or when they’re used for more advanced comparisons.

---



# Subquery in SQL
A subquery is simply a query nested inside another query. It’s used when we need to perform multiple operations in steps, or when filtering or selecting data based on another query’s result. A subquery is also called a nested query or inner query.

Subqueries can be classified into several types. Below are the main types, along with examples:



a. Scalar Subquery
A scalar subquery returns only one row and one column. It is executed first, independently, and its result is then used by the outer query.

  Example 1: One row with one column
  Suppose we have a table called employee, and we want to retrieve all employees whose salary is higher than the average salary. In this case, we can use a scalar subquery.

  SELECT employee_id, name, salary
  FROM employee
  WHERE salary > (
    SELECT AVG(salary)
    FROM employee
  );

  Example 2: One row with multiple columns
  Suppose we have a table called employees, Find all employees who work in the same department and job role as Alice:

  SELECT *
  FROM employees
  WHERE (department_id, job_id) = (
    SELECT department_id, job_id
    FROM employees
    WHERE name = 'Alice'
  );




b. Multi-row Subquery
A multi-row subquery returns multiple rows, and it can return either one column or multiple columns.

  1. Multiple rows with a single column
  Suppose we have two tables: employee and department. We want to find all departments that are used in the employee table.

  SELECT department_name
  FROM department
  WHERE department_id IN (
    SELECT DISTINCT department_id
    FROM employee
  );

  2. Multiple rows with multiple columns
  Suppose we have employees and promotions tables. Find all employees who match any department and job combination listed in the promotions table.

  SELECT employee_id, name, department_id, job_id
  FROM employees
  WHERE (department_id, job_id) IN (
    SELECT department_id, job_id
    FROM promotions
  );



c. Correlated Subquery
A correlated subquery depends on values from the outer query. It cannot be executed independently because it is evaluated once for every row of the outer query.

Example:
Suppose we have an employees table, and we want to find employees whose salary is higher than the average salary of their own department.

SELECT name
FROM employees e1
WHERE salary > (
  SELECT AVG(salary)
  FROM employees e2
  WHERE e1.department_id = e2.department_id
);
In this example, the subquery is run once for each row in the outer query.


Where Can We Use Subqueries?
  Subqueries can be used in:

  SELECT clause

  FROM clause

  WHERE clause

  HAVING clause

  Even inside INSERT, UPDATE, and DELETE statements