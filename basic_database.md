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



  # CTE (Common Table Expression)

  A CTE is defined at the beginning of the query. It temporarily holds a result set. You can think of it as a variable that holds a value, but it only exists for the duration of the query. A CTE is defined using the WITH keyword.

  # Why use CTE?
    1. It makes queries readable and maintainable.
    2. CTE helps break down complex queries step by step.
    3. It allows reusing queries.
    4. It increases query performance.
    5. CTE makes it easier to manage complex nested queries or subqueries.


Example of CTE:
  1. Simple CTE: Suppose we have a table employees and you need to find all employees whose salary is greater than the average salary.

  ```sql
    with avg_salary as (
      select avg(salary) as avg_sal
      from employees
    )

    select employee_id, name
    from employees
    cross join avg_salary
    where employees.salary > avg_salary.avg_sal;

  ```


2. Chained CTE: We can also use multiple CTEs or chained CTEs. A chained CTE means you are defining multiple CTEs in a row, where each one can build on the previous.

Suppose we have tables employees and department. Our goal is to find all employees who work in departments where the average salary exceeds 60,000.

  ```sql
  WITH avg_salaries AS (
  SELECT department_id, AVG(salary) AS avg_salary
  FROM employee
  GROUP BY department_id
  ),

  high_avg_departments AS (
    SELECT department_id
    FROM avg_salaries
    WHERE avg_salary > 60000
  )

  SELECT e.employee_id, e.name, e.salary, d.department_name
  FROM employee e
  JOIN high_avg_departments h ON e.department_id = h.department_id
  JOIN department d ON e.department_id = d.department_id;
```

3. Recursive CTEs: A recursive CTE is a way to query hierarchical or tree-structured data, like employees reporting to managers, categories with subcategories, or folder structures.

Suppose we have a table employees. Retrieve the full employee hierarchy starting from top-level managers, including each employee’s level in the organizational structure.

```sql
WITH RECURSIVE emp_hierarchy AS (
  SELECT employee_id, name, manager_id, 1 AS level 
  FROM employee
  WHERE manager_id IS NULL

  UNION ALL

  SELECT e.employee_id, e.name, e.manager_id, eh.level + 1
  FROM employee e
  JOIN emp_hierarchy eh ON e.manager_id = eh.employee_id
)

SELECT *
FROM emp_hierarchy;

```

# Window Functions in SQL

Window functions perform calculations across a set of rows related to the current row.
Unlike aggregate functions (SUM(), AVG()), which return a single value for a group of rows, window functions return a value for every row while still allowing group-based calculations.

They’re incredibly useful for advanced reporting, analytics, and calculations within a partitioned set of data.

To use a window function:

Apply the function (ROW_NUMBER(), RANK(), SUM())

Use the OVER() clause to define the window

Inside OVER() you can use:

  PARTITION BY → group data into windows

  ORDER BY → order rows within the window

  Frame clause → optional, for row ranges

List of window functions:
  1. rank() function: Assigns a rank to each row within a partition, gaps exist between ranks when values tie. Do not take any arguments. 
    suppose we have a table employee. now find employee rank based on salary in each department.

    ```sql
    select employee_id, department, salary
    rank() over(partition by department order by salary desc) as dept_rank
    from employees;
    ```

  2. dense_rank() function: Assigns a rank to each row within a partition but no gaps in rank when values tie.Do not take any arguments.
    suppose we have a table employee. now find employee rank based on salary in each department. and rank must be without skiping numbers.

    ```sql
    select employee_id, department, salary
    dense_rank() over(partition by department order by salary desc) as dept_dense_rank
    from employees;
    ```

  3. row_number() function: Assigns a unique, sequential number to each row within the partition.Do not take any arguments.
    suppose we have a table sales. now find most recent salre for each customer.

    ```sql
    select *
    from (
      select customer_id, sale_date, amount,
      row_number() over(partition by customer_id order by sale_date desc) as rn
      from sales
    ) t
    where rn = 1;
    ```


  4. sum(), max(), min(), avg() functions: Perform aggregate calculations within the window, but keep individual row details. Only accepts one column as an argument.
    suppose we have a table employees. show each employees salary along with the total_salary of their department.

    ```sql
    SELECT 
    employee_id, department, salary,
    SUM(salary) OVER (PARTITION BY department) AS dept_total_salary
    FROM employees;
    ```
  5. count() function: Count the number of rows in each partition. Only accepts one column as an argument.
    suppose we have a table employees. Show how many employees are in each department, next to each employee.
    ```sql
      SELECT 
      employee_id, department,
      COUNT(*) OVER (PARTITION BY department) AS employee_count
      FROM employees;
    ```
  6. lag() function: Access data from the previous row in the partition. Takes up to three arguments: LAG(column, offset, default_value)
    suppose we have a table product_prices. Compare a product’s current price with its previous price.

    ```sql
    SELECT 
      product_id, price_date, price,
      LAG(price, 1, 0) OVER (PARTITION BY product_id ORDER BY price_date) AS previous_price
    FROM product_prices;
    ```
  7. lead() function: Access data from the next row in the partition. Also takes up to three arguments:LEAD(column, offset, default_value)
    suppose we have a table product_prices. see what a product's price will be in the next month.

    ```sql
    SELECT 
      product_id, price_date, price,
      LEAD(price, 1, NULL) OVER (PARTITION BY product_id ORDER BY price_date) AS next_price
    FROM product_prices;

    ```



# Recursive SQL
A recursive query is a query that refers to itself. This means the query executes repeatedly until a certain condition is met. We can achieve a recursive query using CTEs (Common Table Expressions).

## When writing a recursive query, we must include:
  1. a base case
  2. a recursive case
  3. a termination condition to avoid infinite recursion.

## Recursive queries are generally used for hierarchical or tree-like data structures, such as:
  1. Employees reporting to managers
  2. Categories with subcategories
  3. Folders with nested files
  4. Family trees, dependencies, etc.

## Pros of Recursive Queries:
  1. Readable: Easier to understand and maintain than complex joins or loops
  2. Elegant: Ideal for working with hierarchical/tree-structured data (e.g., org charts, categories)
  3. Declarative: Expresses logic clearly in SQL, without needing procedural code
  4. Flexible: Can handle unknown or dynamic depth in hierarchy

## Cons of Recursive Queries:
  1. Deep recursion: Too many levels can hurt performance or hit recursion limits
  2. Missing indexes: Without indexes on join keys (like parent_id), queries slow down
  3. Large datasets: Repeated scans can lead to high CPU and memory usage
  4. Unbounded recursion: Risk of infinite loops if cycles exist and depth limits aren't set
  5. Materialization cost: Intermediate results may consume memory/temp space


    example of recusive query:

    1. Show integers from 1 to 10 in a num column without using built-in functions:

    ```sql
    with recursive nums as (
      select 1 as num
      union
      select num + 1 from nums where num < 10
    )

    select num
    from nums;
    ```

    2. Employee hierarchy: Get manager-to-employee structure including level (depth):

    ```sql
    with recursive emp_hiararchy as (
      select employee_id, name, manager_id, 1 as lavel
      from employees
      where manager_id is null

      union all

      select  employee_id, name, manager_id, lavel + 1
      from employees e
      join emp_hiararchy eh on e.manager_id = eh.employee_id 
    )

    select * 
    from emp_hiararchy
    order by level;
    ```



# Understanding Views vs Materialized Views in SQL

When working with repetitive queries or performance-heavy reporting, two powerful tools can help: Views and Materialized Views.

# View

A View is a virtual table based on a SQL query. It doesn't store data, just the logic. Every time you query it, it fetches live data from the underlying tables.

# Key points:
  1. Does not store data
  2. Always fetches live data from underlying tables
  3. Lightweight and up-to-date
  4. Good for encapsulating logic, simplifying complex queries

# When to use view
  1. Data change frequently
  2. You want always updated result
  3. You don't need speed optimization

# Example

```sql
-- create view
CREATE VIEW monthly_sales AS
SELECT 
  DATE_TRUNC('month', sale_date) AS month,
  SUM(amount) AS total
FROM sales
GROUP BY DATE_TRUNC('month', sale_date);

-- run view
SELECT * FROM monthly_sales;
```

# Materialized view
A materialized view is like a view but its store result of the query physically in the database

# Key points
  1. stores data like a real table
  2. Must be refreshed get updated data
  3. Faster for large or complex queries
  4. good for performance when data doesn't change often

# When to use materialized view
  1. Data changes less often
  2. You want fast reads (e.g., dashboards, reports)
  3. You're okay with refreshing manually or on schedule

# Example

```sql
-- create materialized view
CREATE MATERIALIZED VIEW monthly_sales_mv AS
SELECT 
  DATE_TRUNC('month', sale_date) AS month,
  SUM(amount) AS total
FROM sales
GROUP BY DATE_TRUNC('month', sale_date);

-- run materialized view
SELECT * FROM monthly_sales;

-- refresh materialized view

REFRESH MATERIALIZED VIEW monthly_sales_mv;
```



# Multiple Join
Every backend engineers or database engineers familer with joins. Joins has many types like inner join, left join, right join, full join, cross join etc. basicaly we use joins when we need to get data from multiple tables as a one result set used only one query. So when we joins two table its basicaly easy for us to relate how two table joins work. for using joins with two talbe we need to primay and foreign key relation with two table..also we can join using any other column value which value is unique and this calumn in two tables. but when we need to use multiple joins in a single query then its hard  to understand how its work. someone can not agree with me. but for me first time when i see multi joins query then i can not figure out how its working. then i deep drive into it and figure out how its working. Lets understand multi joins query with examples.

Suppose we have three tables customers, orders and order_items. with this three table customers and orders has one to many relation. Also orders and order_items has one to many relation. Below show these tables:

1. customers
   Every customer can have multiple orders

| customer_id | name        |
|:-----------:|:------------|
| 1           | Alice       | 
| 2           | Bob         | 
| 3           | David       |


2. orders
  Every order can  have multiple order_items

| order_id    | customer_id | order_date |
|:-----------:|:------------|:----------:|
| 101         | 1           | 2024-01-01 |
| 102         | 2           | 2024-01-02 |
| 103         | 3           | 2024-01-01 |
| 104         | 1           | 2024-01-03 |
| 105         | 3           | 2024-01-02 |


3. order_items

| item_id | order_id | product      | quantity |
|:-------:|:---------|:------------:|:--------:|
| 1       | 101      | Pen          | 2        |
| 2       | 101      | Notebook     | 1        |
| 3       | 102      | Pencil       | 4        |
| 4       | 103      | Eraser       | 3        |
| 5       | 103      | Sharpner     | 1        |
| 6       | 104      | Pen          | 4        |
| 7       | 104      | Pencil       | 2        |
| 8       | 105      | Pen          | 4        |
| 9       | 105      | Pencil       | 2        |


# Problem statement:
  Show customer names, their order dates, and each product they ordered with quantity.

  So find these customer with their order details how can we query. with problem statement we need customer name which is in customer table, order date which is in orders table and each product they order with quantity which is in order_items table.

# solution

  So frst we need to check in these table which column or value is same. since customers and orders has one to many relation so customers table primary key customer_id and orders table foreign key customer_id column and value is same. so we need these customer who orders. so for this we can use inner join. inner join return result set where two table customer id match only these rows. lets write query with these two table find customers names amd orders dates.

  ```sql
  select c.name, o.order_id, o.order_date
  from customers as c
  inner join orders as o on c.customer_id = o.customer_id;
  ```

# result
  This query joins the customers and orders tables on customer_id, returning each customers name alogin with their order_id and order_date.

  | name  | order_id | order_date |
  |:------|:---------|:-----------|
  | Alice | 101      | 2024-01-01 |
  | Bob   | 102      | 2024-01-02 |
  | David | 103      | 2024-01-01 |
  | Alice | 104      | 2024-01-03 |
  | David | 105      | 2024-01-02 |

now our main goal is Show customer names, their order dates, and each product they ordered with quantity. in result set we have customer name, order_id and order_date and in order_items table we have product name and product quantity. so if we inner join result table and order_items table based on order_id then we found each customer each orders product quantity. so for example now join result with order_items table

```sql
select r.name, r.order_id, r.order_date, oi.product, oi.quantity
from result as r
inner join order_items as oi on r.order_id = oi.order_iid
```

# result 
 This query joins the result and order_items tables on order_id, returning each customers name alogin with their order_id and order_date, product and quantity.

| name  | order_id | order_date | product   | quantity |
|:------|:---------|:-----------|:----------|:---------|
| Alice | 101      | 2024-01-01 | Pen       | 2        |
| Alice | 101      | 2024-01-01 | Notebook  | 1        |
| Bob   | 102      | 2024-01-02 | Pencil    | 4        |
| David | 103      | 2024-01-01 | Eraser    | 3        |
| David | 103      | 2024-01-01 | Sharpner  | 1        |
| Alice | 104      | 2024-01-03 | Pen       | 4        |
| Alice | 104      | 2024-01-03 | Pencil    | 2        |
| David | 105      | 2024-01-02 | Pen       | 4        |
| David | 105      | 2024-01-02 | Pencil    | 2        |


so using multi join we can achive this result with single query. first join customers and orders on customer_id then join result set with order_items based on order_id

```sql
select c.name, o.order_id, o.order_date, oi.product, oi.quantity
from customers as c
inner join orders as o on c.customer_id = o.customer_id
inner join order_items as oi on o.order_id = oi.order_id
```



# implicit join
Sometimes we use multiple table with from cluse like from a_table, b_table without using any join. so when we use multiple table like this with from clause then its call implicit join. if we don't use any where condition then its implicitly use cross join or cartisian join. in a cross join a_table every row combined with b_table every row. if a_table has 6 row and b_table has 6 row then output table have 36 row. but if we use where condition then its working as a inner join. so then only mathing condition row is fetch a output table.

in implicit join we can use more then two tables. from a_table, b_table, c_table. then how cross join work. first a_table every row combined with b_table every row. then each of those result is combined with every row from c_table. if more then three table then its work like this.


lets show a example for better understanding. 

✅ Problem Statement
You are given an Activity table that tracks machine processing events.

Table: Activity

| id | machine_id | process_id | activity_type | timestamp           |
|----|------------|------------|----------------|---------------------|
| 1  | M1         | P1         | start          | 2025-04-22 10:00:00 |
| 2  | M1         | P1         | end            | 2025-04-22 10:30:00 |
| 3  | M1         | P2         | start          | 2025-04-22 11:00:00 |
| 4  | M1         | P2         | end            | 2025-04-22 11:20:00 |
| 5  | M2         | P1         | start          | 2025-04-22 09:00:00 |
| 6  | M2         | P1         | end            | 2025-04-22 09:45:00 |


Each process will have:

  1. One start row
  2. One end row
  3. For the same machine and same process_id

Goal
  Find the average processing time (in seconds) for each machine, where:
    1. Processing time = end timestamp − start timestamp
    2. Round the average time to 3 decimal places


we can solve this problem many way in sql. but for understanding implicit join we use it for solve this problem.

Query:

 ```sql
 SELECT a.machine_id,
       ROUND(AVG(EXTRACT(EPOCH FROM (b.timestamp - a.timestamp))), 3) AS processing_time
  FROM Activity AS a, Activity AS b
  WHERE a.machine_id = b.machine_id
    AND a.process_id = b.process_id
    AND a.activity_type = 'start'
    AND b.activity_type = 'end'
  GROUP BY a.machine_id;

 ```

 with this query we can get our desire output. so lets breakdown this query for remove all confusion:


Step 1: FROM Activity AS a, Activity AS b
  This does a Cartesian product (every row of a paired with every row of b), creating 6 × 6 = 36 rows.

  We’ll just show a small portion of this huge table:

  | a.id | a.machine_id | a.process_id | a.activity_type | a.timestamp           | b.id | b.machine_id | b.process_id | b.activity_type | b.timestamp           |
|------|--------------|--------------|------------------|------------------------|------|--------------|--------------|------------------|------------------------|
| 1    | M1           | P1           | start            | 2025-04-22 10:00:00    | 1    | M1           | P1           | start            | 2025-04-22 10:00:00    |
| 1    | M1           | P1           | start            | 2025-04-22 10:00:00    | 2    | M1           | P1           | end              | 2025-04-22 10:30:00    |
| 1    | M1           | P1           | start            | 2025-04-22 10:00:00    | 3    | M1           | P2           | start            | 2025-04-22 11:00:00    |
| 1    | M1           | P1           | start            | 2025-04-22 10:00:00    | 4    | M1           | P2           | end              | 2025-04-22 11:20:00    |
| 1    | M1           | P1           | start            | 2025-04-22 10:00:00    | 5    | M2           | P1           | start            | 2025-04-22 09:00:00    |
| ...  | ...          | ...          | ...              | ...                    | ...  | ...          | ...          | ...              | ...                   |

  You can imagine all 36 combinations here.

Step 2: WHERE a.machine_id = b.machine_id
Now we only keep rows where both rows are from the same machine:

| a.id | a.machine_id | a.process_id | a.activity_type | a.timestamp          | b.id | b.machine_id | b.process_id | b.activity_type | b.timestamp          |
|------|--------------|--------------|-----------------|----------------------|------|--------------|--------------|------------------|----------------------|
| 1    | M1           | P1           | start           | 2025-04-22 10:00:00  | 1    | M1           | P1           | start            | 2025-04-22 10:00:00  |
| 1    | M1           | P1           | start           | 2025-04-22 10:00:00  | 2    | M1           | P1           | end              | 2025-04-22 10:30:00  |
| 1    | M1           | P1           | start           | 2025-04-22 10:00:00  | 3    | M1           | P2           | start            | 2025-04-22 11:00:00  |
| 1    | M1           | P1           | start           | 2025-04-22 10:00:00  | 4    | M1           | P2           | end              | 2025-04-22 11:20:00  |
| 2    | M1           | P1           | end             | 2025-04-22 10:30:00  | 1    | M1           | P1           | start            | 2025-04-22 10:00:00  |
| 2    | M1           | P1           | end             | 2025-04-22 10:30:00  | 2    | M1           | P1           | end              | 2025-04-22 10:30:00  |
| 3    | M1           | P2           | start           | 2025-04-22 11:00:00  | 3    | M1           | P2           | start            | 2025-04-22 11:00:00  |
| 3    | M1           | P2           | start           | 2025-04-22 11:00:00  | 4    | M1           | P2           | end              | 2025-04-22 11:20:00  |
| 4    | M1           | P2           | end             | 2025-04-22 11:20:00  | 3    | M1           | P2           | start            | 2025-04-22 11:00:00  |
| 5    | M2           | P1           | start           | 2025-04-22 09:00:00  | 5    | M2           | P1           | start            | 2025-04-22 09:00:00  |
| 5    | M2           | P1           | start           | 2025-04-22 09:00:00  | 6    | M2           | P1           | end              | 2025-04-22 09:45:00  |
| 6    | M2           | P1           | end             | 2025-04-22 09:45:00  | 5    | M2           | P1           | start            | 2025-04-22 09:00:00  |
| 6    | M2           | P1           | end             | 2025-04-22 09:45:00  | 6    | M2           | P1           | end              | 2025-04-22 09:45:00  |


Step 3: AND a.process_id = b.process_id
Now we only keep rows where the process_id also matches:

| a.id | a.machine_id | a.process_id | a.activity_type | a.timestamp | b.id | b.machine_id | b.process_id | b.activity_type | b.timestamp |
|------|--------------|--------------|-----------------|-------------|------|--------------|--------------|-----------------|-------------|
| 1    | M1           | P1           | start           | 10:00       | 1    | M1           | P1           | start           | 10:00       |
| 1    | M1           | P1           | start           | 10:00       | 2    | M1           | P1           | end             | 10:30       |
| 3    | M1           | P2           | start           | 11:00       | 4    | M1           | P2           | end             | 11:20       |
| 5    | M2           | P1           | start           | 09:00       | 6    | M2           | P1           | end             | 09:45       |


Step 5: AND a.activity_type = 'start' AND b.activity_type = 'end'
Now we only keep rows where:

  . a is a "start"

  . b is an "end"


| a.id | a.machine_id | a.process_id | a.activity_type | a.timestamp | b.id | b.machine_id | b.process_id | b.activity_type | b.timestamp |
|------|--------------|--------------|-----------------|-------------|------|--------------|--------------|-----------------|-------------|
| 1    | M1           | P1           | start           | 10:00       | 2    | M1           | P1           | end             | 10:30       |
| 3    | M1           | P2           | start           | 11:00       | 4    | M1           | P2           | end             | 11:20       |
| 5    | M2           | P1           | start           | 09:00       | 6    | M2           | P1           | end             | 09:45       |



✅ Final Result After GROUP BY + SELECT
From this filtered result, we calculate the time difference and average per machine.

| machine_id | processing_time |
|------------|-----------------|
| M1         | 25.000          |
| M2         | 45.000          |



with avobe visualization i try to visualize how eactually iplicit join work.

Pros of Implicit Joins:
  1. Simplicity: Easier for small, straightforward queries.
  2. Concise: Fewer keywords, making the query shorter.

Cons of Implicit Joins:
  1. Less Readable: Harder to understand in complex queries.
  2. Risk of Errors: Can lead to Cartesian products if conditions are missing.
  3. Limited Flexibility: Lacks control over different join types.


Implicit joins are typically used in the following situations:

  1. Simple Queries: When you're working with small, straightforward queries involving only two tables and basic conditions.
  2. Legacy Code: If you're maintaining or working with older codebases that already use implicit joins.
  3. Quick Prototyping: For fast development or quick queries where clarity and readability aren't critical.

However, it's generally better to use explicit joins for most modern SQL queries, as they are more readable and flexible.



# How PostgreSQL Indexes Work and optimize performance

# introduction
as a backend dev our everyday life we use db and fetch data from db using query. when we deal with small amount of data then its not important to consider about performance. generally our query is fast for small amount data by default. but when we need featch data from like 100 milion rows table then only default way its not best for our query performance. its can cause bad impact on out application and overoll user sataticfaction. so for this query performance need. many software like ecommerce, payment_systems, gaming, transportation etc. has million of users and the fetch data from db per seccond .. so if query performance is slow then it affect on overoll software performance. so for backend dev it's important to know how can increase query performance. for increase query performance indexing is most important technique. so in this article i try to explaing what is indexing and how does it work under the hood in postgresql.

# what is indexing?
  indexing is a technique to quickly fetch or felter data from table. indexing speed up query performance. basically indexing is a data structure how can we structure index data and which indexing technique we use for our specific scenario. Much like an index in a book, a database index allows a system to find data without needing to search every row in a database table every time a database table is accessed. Indexes can be created using one or more columns. An index stores a subset of the table’s data (e.g., column values) in a way that optimizes search operations, such as SELECT, WHERE, JOIN, or ORDER BY. However, indexes come with trade-offs, as they increase storage and can slow down write operations (INSERT, UPDATE, DELETE).

# types of indexings postgresql?
  in postgresql db has different types of indexing which is best for different sceinario. types of indexing  in postgresql:

  1. b-tree: b-tree is best for equal comparisons(=) , range queries(<,>,between) and order by queries. b-tree is most commonly used index. in postgresql for primary key and unique constratints b-tree create automatically. example: A customer management system where you frequently query customers by email (equality) or created_at (range).
  ```sql
  -- exact equal 
  create index idx_customer_email on customers (email);
  select * from customers where email = 'jhon@doe@example.com'

  -- range queries
  create index idx_customer_created on customers (created_at);
  select * from customers where created_at between '2023-01-01' and '2023-12-31';
  ```


  2. hash: hash index is best for equal comparisons(=) when you don't need sorting or range queries. can not be used for range queries and rarely better then b-tree except in very high collision hash scenarios. example: A lookup table for product SKUs in an e-commerce platform where only exact matches are needed.

  ```sql
  create index idx_product_sku_hash on products using hash (sku);
  select * from products where sku = 'abc123;
  ```


  3. gin: best for full-text search, array columns, jsonb fields. Slower to write, fast to query. GIN = best for multi-key matching. exmaple: A document management system storing JSONB metadata or full-text search for articles.

  ```sql
  -- search using jsonb key value
  create index idx_document_metadata on documents using gin (metadata jsonb_path_ops);
  select * from documents where metadata @> '{"category": "finance"}';

  -- search from full text search
  create index idx_article_search on articles using gin (to_tsvector('english', content));
  select * from articles where to_tsvector('english', content) @@ to_tsquery('database & performance');

  ```


  4. gist: best for Geospatial data (PostGIS), Custom data types (like boxes, ranges), Nearest-neighbor searches. Supports many extensions (e.g., earthdistance, Flexible, but slower than B-tree for basic operationscube). example: A ride-sharing app that needs to find drivers within a specific geographic radius.
  ```sql
  create index idx_driver_location on drivers using gist (location);
  select * from drivers where location && ST_MakeEnvelope(-122, 37, -121, 38, 4326);
  ```
  5. sp-gist: best for Hierarchical or non-balanced trees, Quadtrees, tries, IP address lookups. Specialized use cases.Efficient for spatial or partitioned data structures. example: A network monitoring system storing IP addresses for efficient range-based lookups.
  ```sql
  create index idx_ip_range on network_logs using spgist (ip_address);
  select * from network_logs where ip_address << '192.168.0.0/16';
  ```

  6. brin: best for very large tables, Columns where values are naturally ordered (e.g., timestamps, IDs). Much smaller than B-tree, Ideal for append-only time-series data, Low maintenance. example: A time-series database for IoT sensor data, where records are appended in chronological order.
  ```sql
  create index idx_sensor_timestamp on sensor_data using brin (timestamp);
  select * from sensor_data where timestamp >= '2025-01-01' and timestamp < '2025-02-01';
  ```

  General Considerations for Choosing an Index
  1. Query Patterns: Analyze your application’s queries (EXPLAIN ANALYZE) to identify bottlenecks and choose the index type that matches the operators used (e.g., =, <, &&, @>).
  2. Data Characteristics: Consider data size, cardinality, and distribution. For example, B-Tree is great for high-cardinality columns, while BRIN suits low-cardinality, ordered data.
  3. Write vs. Read Trade-Off: Indexes improve read performance but slow down writes. For write-heavy workloads, minimize the number of indexes or use BRIN for low overhead.
  4. Storage Constraints: GIN and GiST indexes can be large, so ensure sufficient disk space and monitor index bloa
  


for understanding how index work in postgresql now we use deafult index b-tree in this article.

# how do postgresql store table data?
  Postgres is a Relational Database Management System(RDBMS) built on top of two basic principles

  Data is stored as Rows inside Tables
  Internally data is held in Disk or physical storage(SDD/HDD) as blocks and fetched to RAM when processing.

  Postgres stores the actual data(rows of tables) in heap files. Typically it's fixed to 1GB size. These files are subdivided into blocks of 8Kb. This page/ block is the basic unit of storage for Postgres. Whenever a row inside this has to be read, It will fetch the full block. So, the block size is chosen optimally to fit into the RAM page. New blocks get appended to the heap files when existing blocks are full.

  so now lets breakdown what is disk, files, pages or blocks and heap.

  1. Disk:  PostgreSQL stores all its data on disk means physical storage (SDD/HDD) (unless using in-memory extensions). This ensures data persists after restarts. Each database resides in a data directory (e.g., /var/lib/pgsql/data/base/).

  2. files: Each table or index in PostgreSQL is stored in one or more files. These files live inside subdirectories like base/, organized by OID (Object ID) of the database and table. each table is a binary file.

  ```lua
  base/
  16384/      <-- a specific database
    2619      <-- a specific table
  ```
  If a table grows large, PostgreSQL splits it into multiple files with suffixes like .1, .2, etc. (each up to 1GB on most platforms).

  3. Pages (Blocks): ostgreSQL breaks files into pages (also called blocks) of fixed size — 8KB by default. Each page stores multiple rows (tuples) of the table. Every page has metadata and a slot area for row pointers.

  4. Heap: PostgreSQL uses a heap storage structure for stores all pages for a table. A heap file is an unordered collection of rows. No clustering or sorting by default. Each row (tuple) is placed in the next available spot — not necessarily sequential.

  ✅ Here's how storage works:
    1. Rows are stored in pages (also called blocks).
        a. Each page is typically 8 KB in size.
        b. A page can hold multiple rows, depending on their size.
    2. The table itself is stored as a heap of pages:
      a. The pages are not ordered by any column.
      b. PostgreSQL just appends new rows to the first page with enough free space.
      c. There's no built-in ordering — it's an unordered heap table.
    3. When a row is written, it is placed into one of the pages using free space map (FSM) to find a page with room.
    4. Each row (tuple) has metadata, like:
      a. xmin, xmax: transaction visibility
      b. ctid: tuple ID (includes (page_id, offset))

  rows are stored in pages, and the collection of those pages is called a "heap" (not the rows within a page).

  blog link about storage; https://www.linkedin.com/pulse/postgres-physical-storage-tarun-annapareddy/



# Primary Key & Default B-Tree Index
  When you define a primary key in PostgreSQL. PostgreSQL automatically creates a unique index on the primary key column using a B-Tree index.

# B-Tree Index
  1. B-Tree (Balanced Tree) is the default index type in PostgreSQL.

  2. It organizes data in a sorted tree structure, allowing efficient:

    1. Exact lookups (WHERE id = 5)

    2. Range queries (WHERE id BETWEEN 1 AND 100)

    3. Ordered operations (ORDER BY id)

Think of it like a sorted tree where each level helps eliminate half the search space — very efficient (O(log n) complexity).

# What is a Clustered Index?
A clustered index is not a separate index type in PostgreSQL — it's a way of physically ordering the table's rows based on the index. You can manually cluster a table using:

```sql
CLUSTER users USING users_pkey;
```
This means:
  1. PostgreSQL rewrites the table rows in the order of the index.
  2. Only one index can be used for clustering.
  3. It’s a one-time operation — the table does not stay clustered if new rows are added or updated later.
  4. To maintain clustering, you must run CLUSTER again.

# How it works:
  1. PostgreSQL creates a temporary copy of the table, sorts the data by the index, and rewrites it back to disk.
  2. It doesn't keep the clustering — unlike some other databases like SQL Server or MySQL (InnoDB), where clustering is automatic with primary keys.


# What is a Non-Clustered Index?
  All regular indexes in PostgreSQL (including primary key indexes unless CLUSTER is run) are non-clustered by default.

# How non-clustered indexes work:
  1. The index stores pointers (tuple identifiers: CTIDs) to the actual rows in the heap.
  2. When you query using the index, PostgreSQL:
    3. Finds matching keys in the B-Tree
    4. Uses CTIDs to fetch full row data from the heap (table)


# What is a B-Tree index in PostgreSQL?

  1. A B-Tree (Balanced Tree) index is the default and most common index type in PostgreSQL.
  2. It stores sorted data in a tree structure.
  3. It's very efficient for searching with operators like =, <, <=, >, >=, BETWEEN, and IN.
  4. The "B" in B-Tree stands for Balanced — meaning all leaf nodes (where the actual data pointers live) are at the same depth. No matter where you look, it takes about the same number of steps.
  5. PostgreSQL uses the tree to quickly find where the value should be. It navigates from root → child → leaf (logarithmic time, O(log n)) and finds rows fast.


# How B-Tree Works:
  1. For a single column:

    1. PostgreSQL builds a tree with sorted keys from that column.
    2. Each node in the tree holds keys and pointers to child nodes.
    3. Leaf nodes store references (pointers) to the actual rows (tuples) in the table.

  2. For composite (multi-column) indexes:

    1. The tree sorts first by the first column, then within that by the second column, then third, and so on.
    2. It's like sorting a spreadsheet: first by last_name, then by first_name, etc.


# single column index

```sql
CREATE INDEX idx_users_email ON users (email);
```

# For single column index query usages b-tree:
  1. SELECT * FROM users WHERE email = 'a@example.com';  Exact match = is perfect for B-Tree.
  2. SELECT * FROM users WHERE email > 'b@example.com';  >, <, >=, <= are great for B-Tree.
  3. SELECT * FROM users WHERE email LIKE 'abc%';  Prefix search is good, B-Tree can help.

# For single column index query not usage b-tree:
  1. SELECT * FROM users WHERE lower(email) = 'a@example.com';  Function on column (lower(email)) breaks index unless you have a function index.
  2. SELECT * FROM users WHERE email LIKE '%abc';  % at the beginning prevents B-Tree use.


# Composite Index (Multi-Column)
```sql
CREATE INDEX idx_users_last_first ON users (last_name, first_name);
```
# For Composite index query usages b-tree:
  1. SELECT * FROM users WHERE last_name = 'Smith'; Only uses first column — OK.
  2. SELECT * FROM users WHERE last_name = 'Smith' AND first_name = 'John'; Uses both columns — ideal.
  3. SELECT * FROM users WHERE last_name > 'S'; Can do range scan on first column.
  4. SELECT * FROM users WHERE last_name = 'Smith' AND first_name > 'J';  Exact match first, then range on second — good.

# For Composite column index query not usage b-tree:
  1. SELECT * FROM users WHERE first_name = 'John'; Skips first column — can't use index efficiently.

# Rules to Remember:

  1. B-Tree works best for: =, <, <=, >, >=, BETWEEN, LIKE 'abc%'.
  2. B-Tree doesn't work when:
    1. You put functions on columns (unless using function-based index).
    2. You do wildcard % at start (e.g., LIKE '%abc').
    3. You skip columns in composite index.


