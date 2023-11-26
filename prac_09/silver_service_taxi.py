"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """init silver taxi service"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """return a string of silver taxi service"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """get the fare"""
        return self.flagfall + super().get_fare()

