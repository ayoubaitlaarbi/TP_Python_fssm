from article import article

a1 = article("A100", "Clavier mécanique", 45.0, 10)
a2 = article("A200", "Souris gaming", 25.0, 20)
a3 = article("A300", "Écran 24 pouces", 150.0, 5)

for a in (a1 ,a2,a3):
    print(a)


total = sum(a.valeur_stock() for a in (a1,a2,a3))
print(f"Valeur d'inventaire : {total:.2f} $")

a1.approvisionner(10)