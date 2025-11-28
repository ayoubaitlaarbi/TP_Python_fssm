class article :
    def __init__(self ,reference: str,designation: str,prix_ht: float,stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock
    def valeur_stock(self) -> float:
        return self.prix_ht * self.stock
    def __str__(self):
        return f"Ref {self.reference} - {self.designation} : {self.stock} unites a {self.prix_ht} $ HT"
    
    def approvisionner(self, qte: int):
        self.stock +=qte
        with open("mouvements.log","a",encoding="utf-8")as f:
            f.write(f"Approvisionnement {qte}  unités pour {self.reference} — Nouveau stock : {self.stock}\n")
                    