# Implement a class to hold room information. This should have name and
# description attributes.


class Rooms:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):  # user use
        return f"Room: {self.name}, Description: {self.description}"

    def __repr__(self,):  # computer use
        return f"Room: {self.name}, Description: {self.description}"


room = Rooms("foyer", "Dim light filters in from the south. Dusty passages run north and east.")

print(room)
