# clear_output() is commented out because it is not available outside jupyter notebook
# Use jupyter notebook for proper functionality of this program

# from IPython.display import clear_output

class ParkingGarage():

    def __init__(self, tickets = [1,2,3,4,5,6,7,8,9,10], current_ticket = {}, parking_spaces = [1,2,3,4,5,6,7,8,9,10]):
        self.tickets = tickets
        self.current_ticket = current_ticket
        self.parking_spaces = parking_spaces

    def take_ticket(self):
        user_ticket = self.tickets.pop()
        self.current_ticket[user_ticket]='not paid'
        self.parking_spaces.pop()
        self.show_tickets()
        while True:
            ask_4_money = input("Would you like to pay now? Type 'pay' to pay for your ticket, type 'no' to pay later: ")
            if ask_4_money == 'pay':
                # clear_output()
                self.pay_4_parking()
                return
            elif ask_4_money == 'no':
                # clear_output()
                return
            else:
                print("Sorry, not a valid answer.")
    
    def show_tickets(self):
        print(f"\nAvailable tickets: {self.tickets}")
        print(f"Available parking spaces: {self.parking_spaces}")
        print(f"Taken tickets: {self.current_ticket}\n")

    def pay_4_parking(self):
        self.show_tickets()
        while True:
            ticket_number = input("Enter the number of the ticket you want to pay or type 'cancel' to return to main menu: ")
            if ticket_number == 'cancel':
                # clear_output()
                return
            elif ticket_number.isnumeric():
                ticket_number = int(ticket_number)
            else:
                print("Enter a valid ticket number.")
                continue
            
            if ticket_number not in self.current_ticket:
                print("That's not your ticket number.")
            elif self.current_ticket[ticket_number] == "paid":
                print("This ticket has already been paid.")
            else:
                while True:
                    money = input("Please type 'pay' to pay for your ticket or 'cancel' to return to main menu. ")
                    if money.lower() == 'cancel':
                        # clear_output()
                        return
                    elif money.lower() != 'pay':
                        print("That's not a valid payment method. ")
                    else:
                        self.current_ticket[ticket_number] = "paid"
                        # clear_output()
                        print("Thank you for your payment. You have 15 minutes to leave.")
                        return

    def leave_garage(self):
        while True:
            self.show_tickets()
            ticket_number = input("Enter your ticket number: ")
            if ticket_number.isnumeric():
                ticket_number = int(ticket_number)
            else:
                # clear_output()
                print("Enter a valid ticket number.")
                continue

            if ticket_number not in self.current_ticket:
                # clear_output()
                print("That's not your ticket number. Please enter your ticket number.")
            else:
                while True:
                    if self.current_ticket[ticket_number] == 'paid':
                        del self.current_ticket[ticket_number]
                        self.tickets.append(ticket_number)
                        self.parking_spaces.append(ticket_number)
                        print("Thank you. Have a nice day.")
                        return
                    else:
                        # clear_output()
                        print("Ticket has not been paid. You must pay before leaving.")
                        self.pay_4_parking()
                break

    def run_garage(self):
        print("Welcome to J and K's parking garage!")
        while True:
            self.show_tickets()
            user = input("Type 'take' to take a ticket, type 'pay' to pay for parking, type 'leave' to leave the garage, \nor type 'quit' to quit. \n")
            if user == 'take':
                # clear_output()
                self.take_ticket()
            elif user == 'pay':
                # clear_output()
                self.pay_4_parking()
            elif user == 'leave':
                # clear_output()
                self.leave_garage()
            elif user == 'quit':
                return
            else:
                print("That's not a valid response. Please try again.")
                
parking_garage = ParkingGarage()

parking_garage.run_garage()