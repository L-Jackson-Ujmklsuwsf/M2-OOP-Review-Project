class ParkingMeter:
    
    def __init__(self, minutes_purchased=60):
        self._minutes_purchased = None
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Minutes purchased must be a positive integer.")
        self._minutes_purchased = value



