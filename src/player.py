# Write a class to hold player information, e.g. what room they are in
# currently.

class Players:
    def __init__(self, player, start_room): 
        self.player = player
        self.room = start_room 
    def change_room(self, new_room ):
        self.room = new_room
    def __str__(self): #user use
        return f"Player: {self.player}, Room: {self.room}"
    def __repr__(self,): #computer use
        return f"Player: {self.player}, Room: {self.room}"

# player = Players("Melanie", "Foyer")

# print(Players)
# print(player)

