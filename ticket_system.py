
import mysql.connector
from datetime import datetime
try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="Janani@123",  
        database="customers_support"
    )
    cursor = con.cursor()
    print("\n✅ Connected to MySQL Database Successfully!\n")

except mysql.connector.Error as err:
    print(f"❌ Database Connection Failed: {err}")
    exit()
def create_ticket():
    print("\n🎟️ Create a New Ticket")
    name = input("Enter Customer Name: ")
    issue = input("Enter Issue Description: ")
    status = "Open"
    query = "INSERT INTO tickets (customer_name, issue, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, issue, status))
    con.commit()
    print("✅ Ticket Created Successfully!")
def view_tickets():
    print("\n📋 All Tickets")
    cursor.execute("SELECT * FROM tickets")
    rows = cursor.fetchall()
    if not rows:
        print("No tickets found.")
    else:
        print("-------------------------------------------------------------")
        print("Ticket ID | Customer Name | Issue | Status | Date Created")
        print("-------------------------------------------------------------")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        print("-------------------------------------------------------------")
def update_ticket():
    print("\n🛠️ Update Ticket Status")
    ticket_id = input("Enter Ticket ID: ")
    new_status = input("Enter New Status (Open/In Progress/Resolved): ")
    cursor.execute("UPDATE tickets SET status=%s WHERE ticket_id=%s", (new_status, ticket_id))
    con.commit()
    if cursor.rowcount == 0:
        print("❌ No Ticket Found with that ID.")
    else:
        print("✅ Ticket Updated Successfully!")
def delete_ticket():
    print("\n❌ Delete Ticket")
    ticket_id = input("Enter Ticket ID: ")
    cursor.execute("DELETE FROM tickets WHERE ticket_id=%s", (ticket_id,))
    con.commit()
    if cursor.rowcount == 0:
        print("❌ No Ticket Found with that ID.")
    else:
        print("✅ Ticket Deleted Successfully!")
def main_menu():
    while True:
        print("\n--- Customer Ticket Management System ---")
        print("1. Create Ticket")
        print("2. View All Tickets")
        print("3. Update Ticket Status")
        print("4. Delete Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            update_ticket()
        elif choice == '4':
            delete_ticket()
        elif choice == '5':
            print("\n👋 Exiting... Thank you for using the system!")
            break
        else:
            print("⚠️ Invalid Option! Please Try Again.")
if __name__ == "__main__":
    main_menu()
    cursor.close()
    con.close()
