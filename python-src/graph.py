from importlib.resources import path
from platform import node
from actor import Actor
from movie import Movie
from itertools import chain
class Graph:

    def hentVerdier(self) -> tuple:
        return(int((len(list(chain(*self.hovedGraf.values()))))/2), len(self.hovedGraf.keys()))
    
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

    def lagGraf(self) -> None:

        self.hovedGraf = {k:[] for k in self.actorDict.values()}
        for movie in self.filmDict.values():
            filmListe = []
            for actor in movie.actors:
                filmListe.append((actor, movie, movie.rating))
            for actor in movie.actors:
                filmListe.remove((actor, movie, movie.rating))
                self.hovedGraf[actor] += filmListe
                filmListe.append((actor, movie, movie.rating))

    def BFSvisit(self, startNode:Actor, visited:list, sluttNode:Actor) -> None:
        queue = [startNode] # Queue 
        visited.append(startNode)
        while queue:
            nodeKey = queue.pop(0)
            if nodeKey == sluttNode:
                pathList = []
                g = nodeKey
                while g != None:
                    pathList.insert(0,g)
                    g = g.forrige
                for actors in pathList:
                    print(actors)
                return
            for naboer in self.hovedGraf[nodeKey]:
                if naboer[0] not in visited:  
                    naboer[0].forrige = nodeKey if naboer[0].forrige == None else None
                    visited.append(naboer[0])
                    queue.append(naboer[0])
        print("finnes ingen vei")
        
    def BFSfull(self, nmIdSlutt:str, nmIdStart:str):
        visited = []
        for actor in self.hovedGraf.keys():
            if actor.id == nmIdSlutt:
                sluttNode = actor
                print("hei")
            if actor.id == nmIdStart:
                startNode = actor
                print("HEi")
        print("Start", startNode)
        print("Slutt", sluttNode)
        self.BFSvisit(startNode,visited,sluttNode)