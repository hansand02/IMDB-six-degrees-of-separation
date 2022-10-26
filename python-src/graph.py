from actor import Actor
from movie import Movie
from itertools import chain
class Graph:


    def hentVerdier(self) -> tuple:
        
        def flatten_dict_values(dictionary):
            return chain(*dictionary.values())
        
        return((len(list(flatten_dict_values(self.hovedGraf))))/2, len(self.hovedGraf.keys()))

    def __init__(self) -> None:
        self.actorDict =  {}
        self.filmDict = {}
        self.hovedGraf = None
        
    def les(self, movies:str, actors:str) -> None:
        self.lesFilmer(movies)
        self.lesActors(actors)
         
    def lesActors(self, filnavn: str) -> dict:
        #self.actorDict becomes k,v = actorId, ActorObject
        #Open file, read actors by id, name and movies played in
        #Create new Actor object from this, iterate over all movies played in, and add this object in the actors list in Movie. 
        with open(filnavn) as fil:
            for linje in fil:
                if linje:
                    linjeL = linje.strip().split("\t") 
                    skuespiller = (Actor(linjeL[2:],linjeL[1],linjeL[0]))
                    self.actorDict[linjeL[0]] = skuespiller
                    for title in linjeL[2:]:
                        #This check is necessary because movie may not be in IMDB database
                        if title in self.filmDict:
                            self.filmDict[title].actors.append(skuespiller)

    def lesFilmer(self, filnavn: str) -> dict:
        #makes self.filmDict a dictionary k,v = movieId, MovieObject
        try:
            assert len(self.actorDict) == 0
        except: 
            print("lesActors must be run befor lesFilmer")

        with open(filnavn, 'r') as fil:
            for linje in fil:
                if linje:
                    linjeL = linje.strip().split("\t")
                    self.filmDict[linjeL[0]] = Movie(linjeL[0], linjeL[1], float(linjeL[2]))

    def lagGraf(self):

        self.hovedGraf = {k:[] for k in self.actorDict.values()}
        for movie in self.filmDict.values():
            filmListe = []
            for actor in movie.actors:
                filmListe.append((actor, movie, movie.rating))
            for actor in movie.actors:
                filmListe.remove((actor, movie, movie.rating))
                self.hovedGraf[actor] += filmListe
                filmListe.append((actor, movie, movie.rating))




if __name__ == "__main__":
    oppgave2 = Graph()
    oppgave2.les("../data/movies.tsv", "../data/actors.tsv")
    oppgave2.lagGraf()
    print(oppgave2.hentVerdier())