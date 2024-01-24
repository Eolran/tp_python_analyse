populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 12, "name" : "Ian" }
]

relationships = [
    (0,1), (0,2), (1,2), (1,4),(2,3), (2,5),
    (3,4), (3,7), (4,5),(4,8), (4,9), (5,7),
    (5,9), (6,7), (6,8), (7,1), (7,8), (8,9),
    (10,1),(10,2),(10,3),(11,12),(11,2),(11,5)
]

# Modifiez la liste populations pour ajouter les relations (liste relationships) de chaque user de cette population, vous pouvez par exemple ajoutez une clé "relation" ainsi qu'une liste vide dans un premier temps. Puis placez les relations de chaque user dans la liste populations en utilisant relationships.
def addRelations():
    for user in populations:
        user["relation"] = []

        for relation in relationships:
            if relation[0] == user["id"]:
                user["relation"].append(relation[1])
                
            elif relation[1] == user["id"]:
                user["relation"].append(relation[0])
# print(populations)


# Calculer la moyenne des relations.
def averageRelations():
    addRelations()
    moyenne = 0
    for user in populations:
        moyenne += len(user["relation"])

    moyenne = round(moyenne / len(populations), 2)
    return moyenne
# print(moyenne)

# Créez une liste représentant les users (id) et le nombre de relation(s) qu'ils possèdent. Et retournez l'utilisateur qui possède le plus de relation(s).
def userRelations():
    averageRelations()
    userIDAndRelations = []
    mostRelations = 0
    for user in populations:
        userIDAndRelations.append({"userID": user["id"], "relationsNumber": len(user["relation"])})
        if len(user["relation"]) > mostRelations:
            mostRelations = len(user["relation"])
            userWithMostRelations = user["name"]

    return userIDAndRelations, userWithMostRelations, mostRelations
# print(userIDAndRelations)
# print(f"userWithMostRelations is {userWithMostRelations} with {mostRelations} relations")


# Trouvez les amis des amis de chaque utilisateur.
def friendsOfFriends():
    userRelations()
    for user in populations:
        user["friendsOfFriends"] = []

        for relation in user["relation"]:
            for friend in populations[relation]["relation"]:
                if friend not in user["friendsOfFriends"] and friend != user["id"]:
                    user["friendsOfFriends"].append(friend)

    return populations