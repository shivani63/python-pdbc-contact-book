import pymysql
from prettytable import PrettyTable

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="mycontactlist"
    )
except pymysql.MySQLError as e:
    print("Database connection failed:", e)
    exit()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL
)
""")
conn.commit()


def show_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    if not rows:
        print("No contacts found.")
        return

    table = PrettyTable(["ID", "Name", "Phone"])
    for row in rows:
        table.add_row(row)
    print(table)


def create_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    if not phone.isdigit():
        print("Phone number must contain digits only.")
        return

    cursor.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Contact created successfully!")


def update_contact():
    cid = input("Enter contact ID to update: ")
    phone = input("Enter new phone: ").strip()

    if not cid.isdigit() or not phone.isdigit():
        print("Invalid input.")
        return

    cursor.execute(
        "UPDATE contacts SET phone=%s WHERE id=%s",
        (phone, cid)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("No contact found with this ID.")
    else:
        print("Contact updated successfully!")


def search_contact():
    keyword = input("Enter name or phone to search: ")

    cursor.execute(
        "SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s",
        (f"%{keyword}%", f"%{keyword}%")
    )
    rows = cursor.fetchall()

    if not rows:
        print("No contact found.")
        return

    table = PrettyTable(["ID", "Name", "Phone"])
    for row in rows:
        table.add_row(row)
    print(table)


def delete_contact():
    cid = input("Enter contact ID to delete: ")

    if not cid.isdigit():
        print("Invalid ID.")
        return

    cursor.execute("DELETE FROM contacts WHERE id=%s", (cid,))
    conn.commit()

    if cursor.rowcount == 0:
        print("No contact found with this ID.")
    else:
        print("Contact deleted successfully!")


def menu():
    while True:
        print("\n--- My Contact Book ---")
        print("1. Show Contacts")
        print("2. Create Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            create_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


menu()
cursor.close()
conn.close()
