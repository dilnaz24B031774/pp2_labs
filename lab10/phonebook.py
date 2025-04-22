import psycopg2
import csv

# Подключение к БД
def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="phonebook_bd",
        user="postgres",
        password="5432" 
    )

# Ввод из консоли
def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO phonebook (first_name, last_name, phone)
                VALUES (%s, %s, %s)
            """, (first_name, last_name, phone))
    print("Added!")

# Загрузка из CSV
def insert_from_csv(path):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cur.execute("""
                        INSERT INTO phonebook (first_name, last_name, phone)
                        VALUES (%s, %s, %s)
                    """, (row['first_name'], row['last_name'], row['phone']))
    print("CSV imported!")

# Обновление номера по имени
def update_user(first_name, new_phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE phonebook SET phone = %s WHERE first_name = %s
            """, (new_phone, first_name))
    print("Updated!")

# Показать всех
def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            for row in cur.fetchall():
                print(row)

# Поиск по имени
def query_by_name(first_name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM phonebook WHERE first_name = %s
            """, (first_name,))
            print(cur.fetchall())

# Удаление по имени
def delete_user(first_name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM phonebook WHERE first_name = %s
            """, (first_name,))
    print("Deleted!")

# Меню
def menu():
    while True:
        print("\n1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update user")
        print("4. View all")
        print("5. Search by first name")
        print("6. Delete user")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("Enter CSV path: "))
        elif choice == '3':
            update_user(input("First name to update: "), input("New phone: "))
        elif choice == '4':
            query_all()
        elif choice == '5':
            query_by_name(input("First name: "))
        elif choice == '6':
            delete_user(input("First name to delete: "))
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
