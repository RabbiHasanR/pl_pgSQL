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
