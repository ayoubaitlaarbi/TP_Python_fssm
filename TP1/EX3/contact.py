class Contact :
    def __init__(self,nom , telephone,email):
        self.nom = nom
        self.telephone = telephone
        self.email = email
    def initiale(self):
        return self.nom[0].upper()