import os
from datetime import datetime

class Journal:
    def __init__(self, file="journal.txt"):
        self.file = file

    def add(self, text):
        try:
            with open(self.file, "a") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n{text}\n\n")
            print("Entry added successfully!\n")
        except Exception as e:
            print("Error adding entry:", e)

    def view(self):
        try:
            with open(self.file, "r") as f:
                data = f.read()
                if data.strip():
                    print("Your Journal Entries:\n", data)
                else:
                    print("No entries found.")
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.\n")
        print("Finished viewing entries.\n")

    def search(self, word):
        try:
            with open(self.file, "r") as f:
                data = f.read()
                entries = data.strip().split("\n\n")
                found = False
                for entry in entries:
                    if word.lower() in entry.lower():
                        print("Matching Entry:\n", entry.strip(), "\n")
                        found = True
                if not found:
                    print(f"No entries found for: {word}")
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.\n")
        print("Search complete.\n")


    def delete(self):
        if os.path.exists(self.file):
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                os.remove(self.file)
                print("All entries deleted successfully!\n")
                print("Delete operation complete.\n")
            else:
                print("Deletion cancelled.\n")
            
        else:
            print("No journal entries to delete.\n")
        


print("Welcome to Personal Journal Manager!")
print("You can add, view, search, or delete your journal entries.\n")

j = Journal()

while True:
    print("Main Menu")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    ch = input("Enter your choice (1-5): ")

    if ch == "1":
        text = input("Enter your journal entry: ")
        j.add(text)
    elif ch == "2":
        j.view()
    elif ch == "3":
        word = input("Enter a keyword or date to search: ")
        j.search(word)
    elif ch == "4":
        j.delete()
    elif ch == "5":
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option from the menu.\n")
