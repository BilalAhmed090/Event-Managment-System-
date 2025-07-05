

import re
from datetime import datetime

class EventManagement:
    def __init__(self):
        self.clients = {}  # Initialize clients dictionary
        self.staff = {
            "security": [],
            "vendors": [],
            "suppliers": []
        }
        self.admin_password = "admin"  # Simple password for admin login

    def client_login(self):
        while True:
            print("\n1. Make a New Booking\n2. View Past Bookings\n3. Delete a Booking\n4. Exit")
            choice = input("Enter option (1/2/3/4): ")
            if choice == '1':
                self.make_booking()
            elif choice == '2':
                self.view_past_bookings()
            elif choice == '3':
                self.delete_client_booking()
            elif choice == '4':
                print("Exiting client interface...")
                break
            else:
                print("Invalid option. Please choose 1, 2, 3, or 4.")

    def admin_login(self):
        password = input("Enter admin password: ")
        if password == self.admin_password:
            self.admin_interface()
        else:
            print("Invalid password. Access denied.")

    def admin_interface(self):
        while True:
            print("\nAdmin Interface")
            print("1. View All Bookings")
            print("2. Manage Venue Security")
            print("3. Manage Staff")
            print("4. Confirm Payments")
            print("5. View All Staff")
            print("6. Cancel Booking")
            print("7. Exit")
            choice = input("Enter option (1/2/3/4/5/6/7): ")
            if choice == '1':
                self.view_all_bookings()
            elif choice == '2':
                self.manage_venue_security()
            elif choice == '3':
                self.manage_staff()
            elif choice == '4':
                self.confirm_payments()
            elif choice == '5':
                self.view_all_staff()
            elif choice == '6':
                self.delete_client_booking()
            elif choice == '7':
                print("Exiting admin interface...")
                break
            else:
                print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")

            
                

    def view_all_bookings(self):
        print("\nAll Bookings:")
    
    # Collect all bookings into a single list
        all_bookings = []
        for cnic, bookings in self.clients.items():
            for booking in bookings:
                all_bookings.append({
                    "cnic": cnic,
                    "event": booking['event'],
                    "date": booking['date'],
                    "venue": booking['venue'],
                    "total_cost": booking['total_cost']
                })

    # Sort bookings by date
        sorted_bookings = sorted(all_bookings, key=lambda x: x['date'])

    # Display the sorted bookings
        if sorted_bookings:
            for booking in sorted_bookings:
                print(f"Client CNIC: {booking['cnic']}, Event: {booking['event']}, Date: {booking['date'].strftime('%d/%m/%Y')}, Venue: {booking['venue']}, Total Cost: PKR {booking['total_cost']}")
        else:
            print("No bookings found.")
    def delete_booking(self):
        cnic = input("Enter the client's CNIC to delete a booking: ")
        if cnic in self.clients:
            print("Client's Bookings:")
            for index, booking in enumerate(self.clients[cnic]):
                print(f"{index + 1}. Event: {booking['event']}, Date: {booking['date'].strftime('%d/%m/%Y')}, Venue: {booking['venue']}, Total Cost: PKR {booking['total_cost']}")
            booking_index = int(input("Enter the booking number to delete: ")) - 1
            if 0 <= booking_index < len(self.clients[cnic]):
                deleted_booking = self.clients[cnic].pop(booking_index)
                print(f"Booking for event '{deleted_booking['event']}' on {deleted_booking['date'].strftime('%d/%m/%Y')} deleted successfully.")
            else:
                print("Invalid booking number.")
        else:
            print("Client not found.")
            
            
    def view_all_staff(self):
        print("\nAll Staff:")
    
        # Collect all staff names along with their roles
        all_staff = []
        for role, members in self.staff.items():
            for member in members:
                all_staff.append((member, role))  # Store as a tuple (name, role)

    # Sort the staff names alphabetically
        sorted_staff = sorted(all_staff, key=lambda x: x[0])  # Sort by name

    # Display the sorted staff names
        if sorted_staff:
            print("Sorted Staff List:")
            for name, role in sorted_staff:
                print(f"{name} (Role: {role.capitalize()})")
        else:
            print("No staff hired.")

    def manage_venue_security(self):
        print("\nManage Venue Security:")
        action = input("Do you want to (1) Add Security Staff or (2) Remove Security Staff? (Enter 1 or 2): ")
        if action == '1':
            staff_name = input("Enter the name of the security staff to add: ")
            self.staff["security"].append(staff_name)
            print(f"Security staff '{staff_name}' added successfully.")
        elif action == '2':
            staff_name = input("Enter the name of the security staff to remove: ")
            if staff_name in self.staff["security"]:
                self.staff["security"].remove(staff_name)
                print(f"Security staff '{staff_name}' removed successfully.")
            else:
                print(f"Security staff '{staff_name}' not found.")
        else:
            print("Invalid option.")

    def manage_staff(self):
        print("\nManage Staff:")
        action = input("Do you want to (1) Add Staff, (2) Remove Staff, or (3) View All Staff? (Enter 1, 2, or 3): ")
    
        if action == '1':
            staff_type = input("Enter staff type (security/vendors/suppliers): ").lower()
            staff_name = input("Enter the name of the staff to add: ")
            if staff_type in self.staff:
                self.staff[staff_type].append(staff_name)
                print(f"{staff_type.capitalize()} '{staff_name}' added successfully.")
            else:
                print("Invalid staff type.")
    
        elif action == '2':
            staff_type = input("Enter staff type (security/vendors/suppliers): ").lower()
            staff_name = input("Enter the name of the staff to remove: ")
            if staff_type in self.staff and staff_name in self.staff[staff_type]:
                self.staff[staff_type].remove(staff_name)
                print(f"{staff_type.capitalize()} '{staff_name}' removed successfully.")
            else:
                print(f"{staff_type.capitalize()} '{staff_name}' not found.")
    
        elif action == '3':
         # Collect all staff names
            all_staff = []
            for role, members in self.staff.items():
                all_staff.extend(members)  # Add all members to the list

            # Sort the staff names
            sorted_staff = sorted(all_staff)

            # Display the sorted staff names
            print("\nSorted List of All Staff:")
            for name in sorted_staff:
                print(name)
    
        else:
            print("Invalid option.")

    def confirm_payments(self):
        print("\nConfirm Payments:")
        cnic = input("Enter the CNIC of the client to confirm payment: ")
        if cnic in self.clients:
            for booking in self.clients[cnic]:
                print(f"Event: {booking['event']}, Date: {booking['date'].strftime('%d/%m/%Y')}, Venue: {booking['venue']}, Total Cost: PKR {booking['total_cost']}")
            confirm = input("Do you want to confirm payment for all bookings? (yes/no): ").lower()
            if confirm == 'yes':
                print(f"Payments confirmed for client with CNIC: {cnic}.")
            else:
                print("Payment confirmation canceled.")
        else:
            print(f"No bookings found for CNIC {cnic}.")

    def make_booking(self):
        print("Making a New Booking...")
        cnic = input("Enter your CNIC: ")
        name = input("Enter your name: ")
        contact = input("Enter your Contact Number: ")
        email = input("Enter your Email ID: ")

        if cnic not in self.clients:
            self.clients[cnic] = []

        date = self.get_valid_date("Enter date of event (DD/MM/YYYY): ")
        event_name = input("Choose the type of event \n-----------------------\nCorporate Event \nWedding Reception \nAnniversary Party \nGraduation Party \nAward Ceremony \n-----------------------\nChoose the type of Event: ")

        # Venue selection
        venues = {
            "The Pearl Palace": 500000,
            "The Clifton Marquee": 650000,
            "Courtyard Venues": 450000,
            "The Garden Oasis": 550000,
            "The Skyline Banquet Hall": 700000,
            "The Skyloft Banquet": 650000,
            "The Mansion Marquee": 750000
        }
        print("\nAvailable Venues:")
        for idx, (venue, price) in enumerate(venues.items(), 1):
            print(f"{idx}. {venue} - PKR {price}")

        selected_venue_idx = int(input("Select a venue by number: ")) - 1
        selected_venue = list(venues.keys())[selected_venue_idx]
        venue_price = venues[selected_venue]

        # Time of day selection
        time_of_day = input("Is the event during the day or night? (day/night): ").lower().strip()
        if time_of_day == "night":
            venue_price *= 1.2  # Increase price for night events

        print(f"Selected venue: {selected_venue} with cost PKR {venue_price}")

        seats = self.get_valid_seats()

        catering_choice = input("Choose catering option (internal/external): ").lower().strip()

        total_food_cost = 0
        theme_price = 0
        total_technical_cost = 0
        ticket_quantity = 0
        ticket_price = 100
        agency_price = 0

        if catering_choice == "internal":
            print("Catering: Internal selected.")
            food_options = [
                ("Pasta", 1000), ("Salad", 500), ("Soup", 700), ("Rice", 400), ("Cake", 800),
                ("Grilled Chicken", 1200), ("Vegetable Stir-fry", 1000), ("Beef Wellington", 2000),
                ("Mushroom Risotto", 1500), ("Lasagna", 1300), ("Roast Beef", 1800), ("Prawns", 2200),
                ("Chicken Wings", 900), ("Vegetable Platter", 600), ("Fried Rice", 600), ("Mashed Potatoes", 500),
                ("Fruit Salad", 700), ("Cheese Platter", 1500), ("Spring Rolls", 800), ("Tacos", 600),
                ("Sandwiches", 500), ("Pizza", 1000), ("Burgers", 700), ("Fries", 400), ("Moussaka", 1400),
                ("Paella", 1800), ("Quiche", 900), ("Chili", 1100), ("BBQ Ribs", 2000), ("Curry Chicken", 1200),
                ("Dumplings", 800), ("Grilled Fish", 1800 ), ("Mac and Cheese", 900), ("Steak", 2500),
                ("Fried Chicken", 1200), ("Steamed Vegetables", 500), ("Vegetarian Tacos", 700),
                ("Crispy Chicken Tenders", 900), ("Vegetable Samosas", 600), ("Stuffed Mushrooms", 1000),
                ("Pork Ribs", 2000), ("Pasta Salad", 800), ("Chicken Caesar Salad", 1000), ("Garlic Bread", 400),
                ("Brownie", 600), ("Cupcakes", 500), ("Fruit Tart", 800), ("Chocolate Mousse", 700),
                ("Ice Cream", 400), ("Fruit Punch", 600), ("Lemonade", 400)
            ]
            print("\nChoose your food options:")
            for idx, (food, price) in enumerate(food_options, 1):
                print(f"{idx}. {food} - PKR {price}")

            selected_foods = input("Enter the numbers of the foods you want, separated by commas: ").split(',')
            food_choices = []
            for idx in selected_foods:
                try:
                    food_idx = int(idx.strip()) - 1
                    food, price = food_options[food_idx]
                    food_choices.append(food)
                    total_food_cost += price
                except (ValueError, IndexError):
                    print(f"Invalid choice: {idx.strip()}. Please enter valid numbers.")

            print(f"\nSelected foods: {', '.join(food_choices)}")
            print(f"Total food cost: PKR {total_food_cost}")

            decoration_themes = [
                ("Blue and Silver Theme", 10000), ("Gold and White Theme", 15000), ("Red and Black Theme", 12000),
                ("Black and Gold Theme", 18000), ("White and Green Theme", 13000), ("Pink and White Theme", 11000),
                ("Golden and Red Theme", 14000), ("Elegant Black Theme", 16000), ("Bohemian Style", 17000),
                ("Modern Chic Theme", 19000), ("Rustic Charm", 15000), ("Vintage Romance", 16000), 
                ("Floral Elegance", 18000), ("Bright Pastels", 12000), ("Neon Lights Theme", 20000)
            ]
            print("\nChoose decoration theme:")
            for idx, (theme, price) in enumerate(decoration_themes, 1):
                print(f"{idx}. {theme} - PKR {price}")

            selected_theme_idx = input("Enter the number of the decoration theme you want: ")
            try:
                theme_choice = decoration_themes[int(selected_theme_idx) - 1]
                theme_name, theme_price = theme_choice
                print(f"Selected decoration theme: {theme_name}")
                print(f"Decoration cost: PKR {theme_price}")
            except (ValueError, IndexError):
                print(f"Invalid choice: {selected_theme_idx}. Please select a valid number.")

        elif catering_choice == "external":
            print("Catering: External selected.")
            # External catering logic can be added if needed.

        else:
            print("Invalid catering choice. Please select either 'internal' or 'external'.")

        technical_equipment = input("Do you need technical equipment? (yes/no): ").lower().strip()
        if technical_equipment == "yes":
            equipment_options = [
                ("Microphone", 1000), ("Speaker", 1500), ("Projector", 2500), ("Lighting", 2000)
            ]
            print("\nAvailable Technical Equipment:")
            for idx, (equipment, price) in enumerate(equipment_options, 1):
                print(f"{idx}. {equipment} - PKR {price}")

            selected_equipment = input("Enter the numbers of the equipment you need, separated by commas: ").split(',')
            for idx in selected_equipment:
                try:
                    equipment_idx = int(idx.strip()) - 1
                    equipment, price = equipment_options[equipment_idx]
                    total_technical_cost += price
                except (ValueError, IndexError):
                    print(f"Invalid choice: {idx.strip()}. Please enter valid numbers.")

        parking_tickets = input("Do you need parking tickets? (yes/no): ").lower().strip()
        if parking_tickets == "yes":
            ticket_quantity = int(input(f"How many tickets do you need (Price per ticket: PKR {ticket_price})? "))
            print(f"Total parking ticket cost: PKR {ticket_quantity * ticket_price}")

        photography = input("Do you want photography services? (yes/no): ").lower().strip()
        if photography == "yes":
            photography_agencies = [
                ("Blue Light Studios", 40000), ("The Canva Studio", 50000), ("Jimmy's Studio", 60000), ("Star Studio", 75000)
            ]
            print("\nPhotography Agencies and Prices:")
            for idx, (agency, price) in enumerate(photography_agencies, 1):
                print(f"{idx}. {agency} - PKR {price}")

            selected_photography = input("Enter the number of the agency you want: ")
            try:
                agency_choice = photography_agencies[int(selected_photography) - 1]
                agency_name, agency_price = agency_choice
                print(f"Selected photography agency: {agency_name}")
                print(f"Photography cost: PKR {agency_price}")
            except (ValueError, IndexError):
                print("Invalid choice. Please select a valid number.")

        total_cost = total_food_cost + theme_price + total_technical_cost + venue_price + (ticket_quantity * ticket_price) + agency_price
        print(f"Total cost of your booking: PKR {total_cost}")

        booking = {
            "name": name,
            "cnic": cnic,
            "date": datetime.strptime(date, "%d/%m/%Y"),  # Convert date to datetime object
            "event": event_name,
            "seats": seats,
            "venue": selected_venue,
            "food": food_choices,
            "decoration": theme_name if 'theme_name' in locals() else None,
            "total_cost": total_cost
        }

        self.clients[cnic].append(booking)
        print(f"Booking confirmed for {name} on {date} at {selected_venue}.")

        # Payment method
        payment_method = input("Choose payment method (cash/bank): ").lower().strip()
        if payment_method == "cash":
            print("You have chosen to pay by cash.")
        elif payment_method == "bank":
            bank_name = input("Enter your bank name: ")
            account_number = input("Enter your account number: ")
            print(f"You have chosen to pay by bank transfer to {bank_name}, Account Number: {account_number}.")
        else:
            print("Invalid payment method selected. Please choose either 'cash' or 'bank'.")

        # Print receipt
        print("\n--- Receipt ---")
        print(f"Name: {name}")
        print(f"CNIC: {cnic}")
        print(f"Contact: {contact}")
        print(f"Email: {email}")
        print(f"Event: {event_name}")
        print(f"Date: {date}")
        print(f"Venue: {selected_venue}")
        print(f"Seats: {seats}")
        print(f"Food Choices: {', '.join(food_choices)}")
        print(f"Decoration Theme: {theme_name if 'theme_name' in locals() else 'None'}")
        print(f"Total Cost: PKR {total_cost}")
        print(f"Payment Method: {'Cash' if payment_method == 'cash' else 'Bank Transfer'}")
        if payment_method == "bank":
            print(f"Bank Name: {bank_name}")
            print(f"Account Number: {account_number}")
        print("-------------------")

    def get_valid_date(self, prompt):
        while True:
            date = input(prompt)
            if self.validate_date(date):
                return date
            else:
                print("Invalid date format. Please use DD/MM/YYYY.")

    def validate_date(self, date_str):
        date_regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        return bool(re.match(date_regex, date_str))

    def get_valid_seats(self):
        while True:
            try:
                seats = int(input("Enter number of seats: "))
                if 0 < seats <= 1000:
                    return seats
                else:
                    print("Seats not available. Please enter a valid number (max 1000).")
            except ValueError:
                print("Please enter a valid number.")

    def view_past_bookings(self):
        cnic = input("Enter your CNIC to view past bookings: ")
        if cnic in self.clients and self.clients[cnic]:
            print(f"Your Past Bookings for CNIC {cnic}:")

        # Sort bookings by venue name and then by date
            sorted_bookings = sorted(self.clients[cnic], key=lambda x: (x['venue'], x['date']))

            for booking in sorted_bookings:
                print(f"Event: {booking['event']} on {booking['date'].strftime('%d/%m/%Y')} at {booking['venue']} with {booking['seats']} seats, Total Cost: PKR {booking['total_cost']}.")
        else:
            print(f"No bookings found for CNIC {cnic}.")

    def delete_client_booking (self):
        cnic = input("Enter your CNIC to delete a booking: ")
        if cnic in self.clients and self.clients[cnic]:
            print("Your past bookings:")
            for idx, booking in enumerate(self.clients[cnic]):
                print(f"{idx + 1}. Event: {booking['event']} on {booking['date'].strftime('%d/%m/%Y')} at {booking['venue']} with {booking['seats']} seats, Total Cost: PKR {booking['total_cost']}.")
            try:
                choice = int(input("Enter the number of the booking you want to delete: ")) - 1
                if 0 <= choice < len(self.clients[cnic]):
                    del self.clients[cnic][choice]
                    print("Booking deleted successfully.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"No bookings found for CNIC {cnic}.")

    def main(self):
        while True:
            print("\nWelcome to Event Management System")
            print("1. Client Login")
            print("2. Admin Login")
            print("3. Exit")
            choice = input("Enter choice (1/2/3): ")
            if choice == '1':
                self.client_login()
            elif choice == '2':
                self.admin_login()
            elif choice == '3':
                print("Exiting system...")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")

# To run the program
if __name__ == "__main__":
    event_management_system = EventManagement()
    event_management_system.main()



