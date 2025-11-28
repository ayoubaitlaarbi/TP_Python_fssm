
from compteur_page import CompteurPage

p1 = CompteurPage("https://example.com/")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

for p in (p1, p2, p3):
        print(p.afficher_stats())
print(CompteurPage.total_visites)

p1.enregistrer_lecture()
p1.enregistrer_lecture()

print(p1.visites_par_page)