from ParkingTickets import ParkingTicket

class PoliceOfficer:

    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, parked_car, parking_meter):
       
        # Checks to see if a car is parked illegally
        
        if parked_car.minutes_parked > parking_meter.minutes_purchased:
            illegal_minutes = parked_car.minutes_parked - parking_meter.minutes_purchased
            return ParkingTicket(parked_car, self, illegal_minutes)
        return None

