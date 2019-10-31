# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description

    def __str__(self):  # user use
        return f"Your Starting Room: {self.room_name},\n Description: {self.room_description}"

    def __repr__(self,):  # computer use
        return f"Your Starting Room: {self.room_name},\n Description: {self.room_description}"


# room = Room("foyer","Dim light filters in from the south. Dusty passages run north and east.")

# print(room)
