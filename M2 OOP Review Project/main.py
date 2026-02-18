
from IfCarIsParked import IfCarIsParked
from ParkingMeter import ParkingMeter
from PoliceOfficer import PoliceOfficer


def run_inspection(car, meter, officer):
    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print(f"{car.make} {car.model} is legally parked.\n")


def main():

    # Scenario 1
    print("==== Scenario 1 ====")
    car1 = IfCarIsParked("Toyota", "Camry", "Red", "XYZ123", 30)
    meter1 = ParkingMeter(40)
    officer1 = PoliceOfficer("John Doe", "5678")
    run_inspection(car1, meter1, officer1)

    # Scenario 2
    print("==== Scenario 2 ====")
    car2 = IfCarIsParked("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    officer2 = PoliceOfficer("Jane Smith", "1234")
    run_inspection(car2, meter2, officer2)

    # Scenario 3
    print("==== Scenario 3 ====")
    car3 = IfCarIsParked("Ford", "Mustang", "Black", "LMN456", 190)
    meter3 = ParkingMeter(60)
    officer3 = PoliceOfficer("James Brown", "4321")
    run_inspection(car3, meter3, officer3)

    # Scenario 4
    print("==== Scenario 4 ====")
    officer4 = PoliceOfficer("Sarah Green", "9999")

    cars = [
        (IfCarIsParked("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
        (IfCarIsParked("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
        (IfCarIsParked("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)),
        (IfCarIsParked("Mazda", "3", "Blue", "MAZ321", 45), ParkingMeter(60)),
    ]

    for car, meter in cars:
        run_inspection(car, meter, officer4)

        
if __name__ == "__main__":
 main()
 print("This concludes the report! :D ")

 

 