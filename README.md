
# 🎫 Customer Ticket Management System

This project is a simple **Customer Ticket Management System** built using **Python and MySQL**.  
It helps manage customer complaints and issues efficiently by allowing you to create, view, update, and delete support tickets through a command-line interface.

---

## ⚙️ Technologies Used
- 🐍 Python 3  
- 🗄️ MySQL  
- 🔗 mysql-connector-python

---

## 🚀 Features
- ➕ Add new customer tickets  
- 📋 View all existing tickets  
- ✏️ Update ticket status (Open / In Progress / Closed)  
- ❌ Delete tickets  
- 💾 Store data permanently in MySQL database

---

## 🧩 How to Run the Project

### 1️⃣ Create the Database and Table in MySQL
Open MySQL and run:
CREATE DATABASE customer_support;

USE customer_support;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    issue_description TEXT,
    status VARCHAR(50)
);
2️⃣ Install the Required Library
pip install mysql-connector-python
3️⃣ Run the Python Program
python ticket_system.py

