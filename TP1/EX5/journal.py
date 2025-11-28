from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self.fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        now = datetime.now().isoformat()
        self.fichier.write(f"{now} - {tache}\n")

    def lire(self):
        with open("journal.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
        for ligne in reversed(lignes):
            print(ligne.strip())

    def __exit__(self, exc_type, exc_value, traceback):
        self.fichier.close()
