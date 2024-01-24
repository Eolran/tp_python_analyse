# Soit les deux listes suivantes : students et levels ces deux listes sont de même longueur 
# et correspondent respectivement aux noms des étudiants et à leur niveau d'étude, à l'aide 
# de la fonction zip et d'une itération affichez le nom et le niveau de chaque étudiant.

students = [
    "Alan",
    "Albert",
    "Jhon",
    "Brice",
    "Alexendra",
    "Brad",
    "Carl",
    "Dallas",
    "Dennis",
    "Edgar",
    "Erika",
    "Isaac",
    "Ian" 
]

levels = [4,2,3,5,7,8,2,6,4,3,5, 7, 5]

def zipLevel():
    zipList = list(zip(students, levels))
    return zipList