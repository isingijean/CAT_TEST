import json

# Function to display the menu
def display_menu():
    print("\n=== Parcel Management ===")
    print("1. View All Parcels")
    print("2. Search for a Parcel")
    print("3. Add a New Parcel")
    print("4. Update a Parcel")
    print("5. Delete a Parcel")
    print("6. Exit")
    choice = input("Please select an option (1-6): ")
    return choice

# Function to display all parcels
def view_parcels(parcels):
    if parcels:
        print("\n=== All Parcels ===")
        for parcel_id, parcel in parcels.items():
            print(f"ID: {parcel_id} - Location: {parcel['location']}, Type: {parcel['type']}, Size: {parcel['size']} sqm, Price: ${parcel['price']}, Master Plan: {parcel['master_plan']}")
    else:
        print("No parcels found.")

# Function to add a new parcel
def add_parcel(parcels):
    print("\n=== Add a New Parcel ===")
    parcel_id = input("Enter Parcel ID: ")
    location = input("Enter Parcel Location: ")
    parcel_type = input("Enter Parcel Type (e.g., Residential, Commercial): ")
    size = float(input("Enter Parcel Size (in sqm): "))
    master_plan = input("Enter Parcel Master Plan: ")
    price = float(input("Enter Parcel Price ($): "))
    
    # Confirm the information
    print(f"\nConfirm the details:")
    print(f"ID: {parcel_id}, Location: {location}, Type: {parcel_type}, Size: {size} sqm, Price: ${price}, Master Plan: {master_plan}")
    
    confirm = input("Do you want to save this parcel? (y/n): ").lower()
    if confirm == 'y':
        parcels[parcel_id] = {
            "location": location,
            "type": parcel_type,
            "size": size,
            "master_plan": master_plan,
            "price": price
        }
        print("Parcel added successfully!")
    else:
        print("Parcel not added.")

# Function to search for a parcel by ID
def search_parcel(parcels):
    parcel_id = input("\nEnter Parcel ID to search: ")
    if parcel_id in parcels:
        parcel = parcels[parcel_id]
        print(f"\nParcel Found: ID: {parcel_id}, Location: {parcel['location']}, Type: {parcel['type']}, Size: {parcel['size']} sqm, Price: ${parcel['price']}, Master Plan: {parcel['master_plan']}")
    else:
        print("Parcel not found.")

# Function to delete a parcel by ID
def delete_parcel(parcels):
    parcel_id = input("\nEnter Parcel ID to delete: ")
    if parcel_id in parcels:
        confirm = input(f"Are you sure you want to delete Parcel {parcel_id}? (y/n): ").lower()
        if confirm == 'y':
            del parcels[parcel_id]
            print(f"Parcel {parcel_id} deleted successfully.")
        else:
            print("Parcel deletion canceled.")
    else:
        print("Parcel not found.")

# Function to update a parcel's details
def update_parcel(parcels):
    parcel_id = input("\nEnter Parcel ID to update: ")
    if parcel_id in parcels:
        print(f"Current details for Parcel {parcel_id}:")
        parcel = parcels[parcel_id]
        print(f"Location: {parcel['location']}, Type: {parcel['type']}, Size: {parcel['size']} sqm, Price: ${parcel['price']}, Master Plan: {parcel['master_plan']}")
        
        # Ask user what they want to update
        location = input(f"Enter new Location (current: {parcel['location']}): ") or parcel['location']
        parcel_type = input(f"Enter new Type (current: {parcel['type']}): ") or parcel['type']
        size = input(f"Enter new Size (current: {parcel['size']} sqm): ")
        size = float(size) if size else parcel['size']
        master_plan = input(f"Enter new Master Plan (current: {parcel['master_plan']}): ") or parcel['master_plan']
        price = input(f"Enter new Price (current: ${parcel['price']}): ")
        price = float(price) if price else parcel['price']
        
        # Confirm the updates
        print(f"\nUpdated details for Parcel {parcel_id}:")
        print(f"Location: {location}, Type: {parcel_type}, Size: {size} sqm, Price: ${price}, Master Plan: {master_plan}")
        
        confirm = input("Do you want to save these changes? (y/n): ").lower()
        if confirm == 'y':
            parcels[parcel_id] = {
                "location": location,
                "type": parcel_type,
                "size": size,
                "master_plan": master_plan,
                "price": price
            }
            print("Parcel updated successfully!")
        else:
            print("Parcel update canceled.")
    else:
        print("Parcel not found.")

# Function to save the parcels data to a JSON file
def save_data(parcels, filename="parcels_data.json"):
    with open(filename, 'w') as file:
        json.dump(parcels, file)
    print(f"Data saved to {filename}")

# Function to load the parcels data from a JSON file
def load_data(filename="parcels_data.json"):
    try:
        with open(filename, 'r') as file:
            parcels = json.load(file)
        print(f"Data loaded from {filename}")
        return parcels
    except FileNotFoundError:
        print(f"No data file found, starting with an empty dataset.")
        return {}

# Main function to control the program flow
def main():
    parcels = load_data()
    
    while True:
        choice = display_menu()

        if choice == '1':
            view_parcels(parcels)
        elif choice == '2':
            search_parcel(parcels)
        elif choice == '3':
            add_parcel(parcels)
        elif choice == '4':
            update_parcel(parcels)
        elif choice == '5':
            delete_parcel(parcels)
        elif choice == '6':
            save_data(parcels)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
