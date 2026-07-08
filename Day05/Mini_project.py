#Contact Book Search
contacts = ["Ali", "Ahmed", "Sara", "Fatima", "Fahad"]

search = input("Enter Contact Name: ")

found = False

for contact in contacts:

    if contact.lower() == search.lower():

        print("Contact Found:", contact)
        found = True
        break

if found == False:
    print("Contact Not Found")