# Creez un model ( une classe ) pour enregistrer les données nettoyées, 
# que vous allez enregistrer dans une table ou un ficher.

import part1
import part2

population = part1.friendsOfFriends()
zipList = part2.zipLevel()

class User:
    def __init__(self, id, name, level, friends, friendsOfFriends):
        self.id = int(id)
        self.name = str(name)
        self.level = int(level)
        self.friends = friends
        self.friendsOfFriends = friendsOfFriends

    def __str__(self):
        return f"User {self.name} with id {self.id} is level {self.level} and has {len(self.friends)} friends and {len(self.friendsOfFriends)} friends of friends"


user1 = User(population[0]["id"], population[0]["name"], zipList[0][1], population[0]["relation"], population[0]["friendsOfFriends"])

print(user1)
# User Alan with id 0 is level 4 and has 2 friends and 8 friends of friends