class CompteBancaire:
    counte = 0
    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial
        CompteBancaire.counte += 1
        self.id = CompteBancaire.counte

    def deposer(self, montant):
        if montant > 0:
             self.__solde += montant

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant

    def get_solde(self):
        return self.__solde

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []
    def ajouter_compte(self,compte: CompteBancaire):
        self.comptes.append(compte)
    def afficher(self):
        print(f"Client : {self.nom}")
        for c in self.comptes:
            print(f"Compte #{c.id}, Solde : {c.get_solde()}€")

cli = Client("Yassir")
compte1 = CompteBancaire(100)
compte2 = CompteBancaire(100)

compte1.deposer(300)
compte2.retirer(50)

cli.ajouter_compte(compte1)
cli.ajouter_compte(compte2)

cli.afficher()
