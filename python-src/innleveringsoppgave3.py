from actor import Actor
from movie import Movie
class innleveringsoppgave2:

    def __init__(self) -> None:
        self.grafListe = dict()
        
    def lesActors(self, filnavn: str) -> list:
        actorList = list()

        with open(filnavn) as fil:
            for linje in fil:
                if linje:
                    linjeL = linje.strip().split("\t") 
                    actorList.append(Actor(linjeL[2:],linjeL[1],linjeL[0]))
        
        return actorList

    def lesFilmer(self, filnavn: str) -> list:
        filmListe = []
        
        with open(filnavn, 'r') as fil:
            for linje in fil:
                if linje:
                    linjeL = linje.strip().split("\t")
                    filmListe.append(Movie(linjeL[0], linjeL[1], float(linjeL[2])))
        return filmListe

if __name__ == "__main__":
    oppgave2 = innleveringsoppgave2()
    oppgave2.lesActors("../data/marvel_actors.tsv")
    oppgave2.lesFilmer("../data/marvel_movies.tsv")


        
    
    