class CompteBancaire:
    def __init__(self,titulaire: str , solde_init = 0):
        self._titulaire = titulaire 
        self.__solde = solde_init
        self._operations = []

        self._operations.append(f"Creation de compte")

    def deposer(self , montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"deposer : {montant}")
        else:
            print("Mantant is not valide !")

    def retirer(self , montant):
        if 0 < montant < self.__solde:
            self.__solde -= montant
            self._operations.append(f"retirer : {montant}")
        else:
            print("Mantant is not valide !")


    @property
    def solde(self):
        return self.__solde
    def __str__(self):
        return f"Titulaire : {self._titulaire} , solde : {self.solde} $"
class CompteEpargne(CompteBancaire):
    def __init__(self,titulaire,solde_init = 0,taux = 0.2):
        super().__init__(titulaire,solde_init)
        self._taux = taux

    def calculer_interet(self):
        self.deposer(self.solde * self._taux)




if __name__ == "__main__":
    compte = CompteBancaire("Ali",1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    #compte.solde = 500 

