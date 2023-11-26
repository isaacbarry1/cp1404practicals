from prac_09.silver_service_taxi import SilverServiceTaxi

"""Test Silver Taxi Class"""

taxi = SilverServiceTaxi("Test Silver Taxi", 75, 4)
taxi.drive(30)


print(taxi.get_fare())

