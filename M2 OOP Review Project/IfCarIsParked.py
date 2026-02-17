class IfCarIsParked:
   

    def __init__(self, make, model, color, license_number, minutes_parked=60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = None
        self.minutes_parked = minutes_parked  # validation through setter

    @property
    def minutes_parked(self):
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Minutes parked must be a positive integer.")
        self._minutes_parked = value

    def __str__(self):
        return (f"Car: {self.make} {self.model}\n"
                f"Color: {self.color}\n"
                f"License Number: {self.license_number}\n"
                f"Minutes Parked: {self.minutes_parked}")


