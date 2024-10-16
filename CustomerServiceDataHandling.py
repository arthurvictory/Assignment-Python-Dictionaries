# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections 
# and loops by creating a system to track customer service tickets.


# Function to open a ticket for the system
def open_ticket(tickets, id, name, issue):
    if id not in tickets:
        tickets[id] = {"Customer": name, "Issue": issue, "Status": "open"}
        print(f"Service Ticket {id} for '{name}' with '{issue}' has been created!")
    else:
        print(f"Service Ticket {id} for '{name}' with '{issue}' has already been made!")


# Function to update tickets from open to closed and visa versa
def update_ticket(tickets, id, status):
    if id in tickets:
        tickets[id]["Status"] = status
        print(f"Service tickets status has been '{status}'")
    else:
        print(f"Service Ticket ID '{id}' was not found.")

# Function to display the tickets
def display_ticket(tickets):
    for id, ticket in tickets.items():
        print(f"Ticket {id}: Customer: {ticket['Customer']}, Issue: {ticket['Issue']}, Status: {ticket['Status']}")


      # Unique ID           Customer Name        issue description    status
service_tickets = {
    "001": {"Customer": "Alice", "Issue": "Login Problem", "Status": "open"},
    "002": {"Customer": "Bob", "Issue": "Payment Issue", "Status": "closed"},
    "003": {"Customer": "Andrew", "Issue": "Internet Connection", "Status": "open"}
}


# function to run the program and add fuctionality
def main_controls():
    while True:
        print("""
                *====Service Tickets====*
            1. Open a new ticket
            2. Update the status of the ticket
            3. Display the tickets
            """)
        
        choice = input("Please make a selection: ")

        if choice == "1":
            ticket_id = input("Enter ticket ID: ")
            name = input("Enter customer's name: ")
            issue = input("Enter the issue description: ")
            open_ticket(service_tickets, ticket_id, name, issue)
        elif choice == "2":
            ticket_id = input("Enter ticket ID to update: ")
            status = input("Enter the new status(Open/Closed): ")
            update_ticket(service_tickets, ticket_id, status)
        elif choice == "3":
            display_ticket(service_tickets)
        elif choice == "4":
            print("The program is shutting down...")
            break
        else:
            print("Please enter a valid option")

main_controls()