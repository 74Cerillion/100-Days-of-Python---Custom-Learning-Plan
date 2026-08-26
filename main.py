from contact import Contact
import sys

Jon = Contact("Jon", "1234567890", "deez@gmail.com")
Emily = Contact("Emily", "2345678901", "nuts@gmail.com")
Kim = Contact("Kim", "3456789012", "haha@gmail.com")
James = Contact("James", "4567890123", "gotem@gmail.com")

translation = {
    "Jon": Jon,
    "Emily": Emily,
    "Kim": Kim,
    "James": James,
}

def main():
        while True:
             
            print("CONTACT MANAGER")
            print("\n1: Add Contacts\n2: View Contacts\n3: Search Contacts\n4: Delete Contact\n5: Exit")

            while True:
                choice = input("Choose a number 1-5 based on the menu above and what" \
                "action you'd like to perform: ")
                if int(choice) in range(1, 6):
                    break
                else:
                    print("Invalid Input, please choose from the provided menu")

            if choice in ['1']:
                Name = input("Name: ")
                Phone = input("Phone Number: ")
                Email = input("Email Address: ")

                Name = Contact(Name, Phone, Email)

                translation["{}".format(Name)] = Name

            if choice in ['2', '3']:
                desired = input("Contact Name to output: ")

                desired = translation[desired]

                desired.formatContact()

            if choice == '4':
                deleted = input("Contact Name to delete: ")

                del translation[deleted]

            if choice == '5':
                sys.exit()

if __name__ == '__main__':
    main()