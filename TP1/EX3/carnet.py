from contact import Contact
class Carnet:
    def __init__(self):
        self._contacts = []
    def ajouter(self,contact: Contact):
        self._contacts.append(contact)
    def recherche(self, fragment: str):
        fragment = fragment.lower()
        result = []
        for c in self._contacts:
            if fragment in c.nom.lower():
                result.append(c)
        return result
    def affiche_tous(self):
        for c in self._contacts:
            print(c)
    def nombre_contacts(self):
        return len(self._contacts)