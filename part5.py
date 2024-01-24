# Créez une classe Parse, soit la chaîne de caractères suivantes, 
# utilisez les fonctions strip() et split() pour retournez une structure
# comportant uniquement des numériques, vous testerez votre 
# méthode sur la chaîne suivante : 
phrase = '8790: bonjour le monde:8987:7777:Hello World:    9007' 

class Parser:
    def __init__(self, parser, string):
        self.string = string
        self.parser = parser

    def parse(self):
        self.string = self.string.split(self.parser)

        for i in range(len(self.string)):
            self.string[i] = self.string[i].strip()

        num = []
        for i in range(len(self.string)):
            if self.string[i].isnumeric():
                num.append(int(self.string[i]))
        return num
    
p = Parser(":", phrase).parse()

print(p)

# Ecrire une classe HasCap qui lorsqu'on renvoie tous les mots/particules 
# d'un texte t commençant par une majuscule dans un dictionnaire en comptant 
# le nombre d'occurence de ces mots/particules.

phrase = "Le langage Python est placé sous une licence libre proche de la licence BSD6 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux7, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser."

class HasCap:
    def __init__(self, string):
        self.string = string

    def hasCap(self):
        words = []
        self.string = self.string.split(" ")
        for word in self.string:
            if word[0].isupper():
                words.append({word: self.string.count(word)})
        
        return words
    
h = HasCap(phrase).hasCap()

print(h)