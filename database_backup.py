# Day 26 - SQLite Database Backup & Restore System
import sqlite3
import os
import shutil
from datetime import datetime
# Database aur backup folders
DATABASE = "shop.db"
BACKUP_FOLDER = "backups"
# Backup folder na ho to create karo
os.makedirs(BACKUP_FOLDER, exist_ok=True)
# Database connection check karo
def connect_database():
    return sqlite3.connect(DATABASE)
# Database mein sample table create karo
def create_table():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    connection.commit()
    connection.close()
# Database ka backup banao
def create_backup():
    if not os.path.exists(DATABASE):
        print("Database not found!")
        return
    # Current date aur time hasil karo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Backup file ka naam
    backup_file = f"{BACKUP_FOLDER}/backup_{timestamp}.db"
    # Database ki copy banao
    shutil.copy2(DATABASE, backup_file)
    print("Backup created successfully!")
    print("File:", backup_file)
# Available backups show karo
def show_backups():
    backups = os.listdir(BACKUP_FOLDER)
    if not backups:
        print("No backups available!")
        return
    print("\nAvailable Backups:")
    for index, backup in enumerate(backups, start=1):
        print(index, backup)
# Database restore karo
def restore_backup():
    backups = sorted(os.listdir(BACKUP_FOLDER))
    if not backups:
        print("No backups available!")
        return
    show_backups()
    try:
        choice = int(input("\nSelect backup number: "))
        if choice < 1 or choice > len(backups):
            print("Invalid backup number!")
            return
        selected_backup = os.path.join(
            BACKUP_FOLDER,
            backups[choice - 1]
        )
        # Existing database connection band karo
        # (Is program mein restore se pehle connections close hone chahiye)
        # Selected backup restore karo
        shutil.copy2(selected_backup, DATABASE)
        print("Database restored successfully!")
    except ValueError:
        print("Please enter a valid number!")
# Main menu
def main():
    create_table()
    while True:
        print("\n===== DATABASE BACKUP SYSTEM =====")
        print("1. Create Backup")
        print("2. Show Backups")
        print("3. Restore Backup")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            create_backup()
        elif choice == "2":
            show_backups()
        elif choice == "3":
            restore_backup()
        elif choice == "4":
            print("Program closed!")
            break
        else:
            print("Invalid choice!")
# Program start
if __name__ == "__main__":
    main()
    