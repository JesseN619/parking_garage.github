class ParkingGarage():

    def __init__(self, tickets = [1,2,3,4,5,6,7,8,9,10], current_ticket = {}, parking_spaces = [1,2,3,4,5,6,7,8,9,10]):
        self.tickets = tickets
        self.current_ticket = current_ticket
        self.parking_spaces = parking_spaces

    def take_ticket(self):
        user_ticket = self.tickets.pop()
        self.current_ticket[user_ticket]=''
        self.parking_spaces.pop()
        self.show_tickets()
        while True:
            ask_4_money = input("Would you like to pay now? Type 'pay' to pay for your ticket, type 'no' to pay later: ")
            if ask_4_money == 'pay':
                self.pay_4_parking()
                return
            elif ask_4_money == 'no':
                return
            else:
                print("Sorry, not a valid answer.")
    
    def show_tickets(self):
        print(f"Available tickets: {self.tickets}")
        print(f"Available parking spaces: {self.parking_spaces}")
        print(f"Taken tickets: {self.current_ticket}")

    def pay_4_parking(self):
        self.show_tickets()
        while True:
            ticket_number = input("Enter the number of the ticket you want to pay: ")
            if ticket_number.isnumeric():
                ticket_number = int(ticket_number)
            else:
                print("Enter a valid ticket number.")
                continue
            
            if ticket_number not in self.current_ticket:
                print("Enter a valid ticket number.")
            elif self.current_ticket[ticket_number] == "paid":
                print("This ticket has already been paid.")
            else:
                money = input("Please type any key to pay.")
                self.current_ticket[ticket_number] = "paid"
                print("Thank you for your payment. You have 15 minutes to leave.")
                break

    def leave_garage(self):
        ticket_number = input("Enter your ticket number: ")
        while True:
            if ticket_number.isnumeric():
                ticket_number = int(ticket_number)
            else:
                print("Enter a valid ticket number.")
                continue

            if ticket_number not in self.current_ticket:
                print("Enter a valid ticket number.")
            else:
                while True:
                    if self.current_ticket[ticket_number] == 'paid':
                        del self.current_ticket[ticket_number]
                        self.tickets.append(ticket_number)
                        self.parking_spaces.append(ticket_number)
                        print("Thank you. Have a nice day.")
                        return
                    else:
                        print("Ticket has not been paid. You must pay before leaving.")
                        self.pay_4_parking()
                break

    def run_garage(self):
        print("Welcome to J and K's parking garage!")
        while True:
            self.show_tickets()
            user = input("Type 'take' to take a ticket, type 'pay' to pay for parking and type 'leave' to leave. ")
            if user == 'take':
                self.take_ticket()
            elif user == 'pay':
                self.pay_4_parking()
            elif user == 'leave':
                self.leave_garage()
            elif user == 'quit':
                return
            else:
                print("That's not a valid response. Please try again.")
parking_garage = ParkingGarage()

parking_garage.run_garage()