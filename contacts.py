contacts = {}  # Dictionary to store contacts

def add_contact(contacts):
  name = input("Enter contact name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email (optional): ")
  address = input("Enter address (optional): ")
  contact_details = {"name": name, "phone": phone, "email": email, "address": address}
  # Generate unique identifier (replace with a better method)
  new_id = len(contacts) + 1
  contacts[new_id] = contact_details
  print(f"Contact added successfully! (ID: {new_id})")

def view_contacts(contacts):
  if not contacts:
    print("No contacts found!")
    return
  print("-" * 50)
  print(" | ID | Name          | Phone Number  |")
  print("-" * 50)
  for contact_id, details in contacts.items():
    print(f" | {contact_id:3} | {details['name']:15} | {details['phone']:13} |")
  print("-" * 50)

# Similar functions for search_contact, update_contact, and delete_contact

def main_menu(contacts):
  while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
      add_contact(contacts)
    elif choice == '2':
      view_contacts(contacts)
    elif choice == '3':
      search_term = input("Enter search term (name or phone number): ")
      search_contact(contacts, search_term)
    # Implement other functionalities based on user choice
    elif choice == '6':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main_menu(contacts)
