"""
CP1404/CP5632 Practical
Band Class
"""


from musician import Musician

class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Init a Band"""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string of band"""
        members_info = ", ".join(str(member) for member in self.members)
        return f"{self.name} ({members_info})"

    def add(self, musician):
        """add a musician to the band"""
        self.members.append(musician)

    def play(self):
        """return a string with each musician and their instrument (or none)"""
        result = ""
        for member in self.members:
            result += member.play() + "\n"
        return result
