from operator import indexOf
from tracemalloc import start
from actor import Actor
from movie import Movie
from itertools import chain
from collections import deque
class Graph:

    def hentVerdier(self) -> tuple:
        return(int(len(list(chain(*self.hovedGraf.values())))/2), len(self.hovedGraf.keys()))
    
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
                filmListe.append((actor, movie))
            for actor in movie.actors:
                filmListe.remove((actor, movie))
                self.hovedGraf[actor] += filmListe
                filmListe.append((actor, movie))

    # Tips for running time:
    # 1: Dont use "in" to check if node is visited O(n) complexity
    # 2: Use deque and not list.pop(0) that is also O(n) complexity
    def BFSvisit(self, startNode:Actor, sluttNode:Actor) -> None:
        
        queue = deque()
        startNode.visited = True
        queue.append(startNode)

        #While queue is not empty
        while len(queue) > 0:
            #Remove first item
            nodeKey = queue.popleft()

            #if statement for printing final path
            if nodeKey == sluttNode:
                pathList = []
                g = nodeKey
                while g != None:
                    pathList.insert(0,g)
                    g = g.forrige
                
                #Just a large clumsy graphical print section
                t = 0
                print("=" *35)
                for actor in pathList:
                    spaces = int(len(actor.name)/2)
                    if indexOf(pathList, actor) == len(pathList)-1:
                        if t%2 == 1:
                            print(" " *20 , actor)
                            print("="* (21 + len(actor.name)))
                            return
                        if t%1 == 0:
                            print(actor)
                            print("="* (21 + len(actor.name)))
                            return

                    if t % 2 == 1:
                        print(" " *20 , actor)
                        for i in range(0, 20, 2):
                            if i == 10:
                                print(" "* (16-i+spaces-int(len(pathList[indexOf(pathList, actor)+1].movieWithLast.name)/2)), pathList[indexOf(pathList, actor)+1].movieWithLast)
                                continue
                            print(" "* (20-i) + " "*spaces + "/")
                    
                    else:
                        print(actor)
                        for i in range(0, 20, 2):
                            if i == 10:
                                print(" "* (16-i+spaces-int(len(pathList[indexOf(pathList, actor)+1].movieWithLast.name)/2)), pathList[indexOf(pathList, actor)+1].movieWithLast)
                                continue
                            print(" "*spaces + " "*i + "\\" )
                    t += 1
            
                return
            #fi
            
            #Visits alle the neighbours of the node that was just removed from the queue, and places the unvisited
            # neighbours on the back of the deque    
            for naboer in self.hovedGraf[nodeKey]:
                if not naboer[0].visited: 
                    naboer[0].visited = True
                    naboer[0].forrige = nodeKey
                    naboer[0].movieWithLast = naboer[1]
                    queue.append(naboer[0])
        print("finnes ingen vei")
    #This method makes sure alle nodeclusters are visited, (not yet)
    #As per now, this method finds the actual created actorobject from a given actorId.  
    def BFSfull(self,  nmIdStart:str,nmIdSlutt:str):
        
        for actor in self.hovedGraf.keys():
            if actor.id == nmIdSlutt:
                sluttNode = actor
            if actor.id == nmIdStart:
                startNode = actor
        self.BFSvisit(startNode,sluttNode)