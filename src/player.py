# Write a class to hold player information, e.g. what room they are in
# currently.

class Players:
    def __init__(self, player, room): 
        self.player = player
        self.room = room  
    def __str__(self):
        return f"Player: {self.player}, Room: {self.room}"
    def __repr__(self,):
        return f"Player: {self.player}, Room: {self.room}"

