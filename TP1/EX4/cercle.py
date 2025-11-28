from math import pi
class Cercle:
    def __init__(self, rayon: float):
        self._rayon = None 
        self.rayon = rayon
    @property
    def rayon(self):
        return self._rayon
    @rayon.setter
    def rayon(self,valeur: float):
        if valeur <= 0:
            raise ValueError("le rayon doit etre strictement positif.")
        self._rayon = valeur
    @property
    def perimetre(self):
        return 2* pi * self._rayon
    @property
    def surface(self):
        return pi * self._rayon**2
    def agrandir(self,pourcentage: float):
        self._rayon += pourcentage *self._rayon /100
    
    
        
