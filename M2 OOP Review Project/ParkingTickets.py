import math

class ParkingTicket:

    def __init__(self, car, officer, illegal_minutes):
        self.car = car
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        
        # First hour should be $25, every hour after that is an additional $10
   
        hours = math.ceil(self.illegal_minutes / 60)
        fine = 25

        if hours > 1:
            fine += (hours - 1) * 10

        return float(fine)

    def __str__(self):
        return (f"\n--- Parking Ticket :( ---\n"
                f"{self.car}\n"
                f"Illegal Time: {self.illegal_minutes}\n"
                f"Fine (USD): ${self.fine:.2f}\n"
                f"Officer Name: {self.officer_name}\n"
                f"Badge Number: {self.badge_number}\n")


