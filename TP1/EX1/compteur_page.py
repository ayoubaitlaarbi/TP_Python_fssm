class CompteurPage:
     total_visites = 0
     def __init__(self, url: str):
          self.url = url 
          CompteurPage.total_visites +=1
          self.visites_par_page = 0

     def afficher_stats(self)-> str:
          return "Page {self.url} - vistes globles :{CompteurPage.total_visites}"
     def enregistrer_lecture(self):
          self.visites_par_page +=1

