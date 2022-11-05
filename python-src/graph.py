from operator import indexOf
from tracemalloc import start
from actor import Actor
from movie import Movie
from itertools import chain
from collections import deque
import time  
class Graph:

    def __init__(self) -> None:
        self.actorDict =  {}
        self.filmDict = {}
        self.hovedGraf = {}
        self.kanter = 0
        self.noder = 0
        self.currentVisitBoolean = True

    #Returns nodes and edges actually in self.hovedGraf. Safe, but not fast
    def kontrollerVerdier(self) -> tuple:
        return(int(len(list(chain(*self.hovedGraf.values())))/2), len(self.hovedGraf.keys()))
    
    #Returns the stored values for edges and nodes, fast, but not safe. 
    def hentVerdier(self) -> tuple:
        return (int(self.kanter/2), self.noder)
    
    #Simplifying external use of reading from file
    def les(self, movies:str, actors:str) -> None:
        self.lesFilmer(movies)
        self.lesActors(actors)

    #self.actorDict becomes key, value = actorId, ActorObject
    def lesActors(self, filnavn: str) -> None:
        #Open file, read actors by id, name and movies played in
        #Create new Actor object from this, iterate over all movies played in, and add this object in the actors list in Movie. 
        with open(filnavn, encoding="utf-8") as fil:
            for linje in fil:
                if linje:
                    self.noder +=1
                    linjeL = linje.strip().split("\t") 
                    skuespiller = (Actor(linjeL[2:],linjeL[1],linjeL[0]))
                    self.actorDict[linjeL[0]] = skuespiller
                    for title in linjeL[2:]:
                        #This check is necessary because movie may not be in IMDB database
                        if title in self.filmDict:
                            self.filmDict[title].actors.append(skuespiller)

    #creates self.filmDict a dictionary key,value = movieId, MovieObject
    def lesFilmer(self, filnavn: str) -> None:
        try:
            assert len(self.actorDict) == 0
        except: 
            print("lesActors must be run befor lesFilmer")
    
        with open(filnavn, encoding="utf-8") as fil:
            for linje in fil:
                if linje:
                    linjeL = linje.strip().split("\t")
                    self.filmDict[linjeL[0]] = Movie(linjeL[0], linjeL[1], float(linjeL[2]))

    #creates self.hovedGraf: key,value = ActorObject, ListOfTuples -> [(ActorObject, MovieObject), ..., ...,]
    def lagGraf(self) -> None:
        
        self.hovedGraf = {k:[] for k in self.actorDict.values()}
        for movie in self.filmDict.values():
            filmListe = []
            for actor in movie.actors:
                filmListe.append((actor, movie))
            for actor in movie.actors:
                filmListe.remove((actor, movie))
                self.hovedGraf[actor] += filmListe
                self.kanter += len(filmListe)
                filmListe.append((actor, movie))

    #Makes visual print of the path
    def printGrafSti(self, pathList:list) -> None:
        print("=" *35)
        for index, actor in enumerate(pathList):
            
            spaces = int(len(actor.name)/2)
            isRightSide = index%2 == 1

            if index == len(pathList)-1:
                if isRightSide:
                    print(" " *20 , actor)
                    return print("="* (21 + len(actor.name)))       
                if not isRightSide:
                    print(actor, actor.totalWeight)
                    return print("="* (21 + len(actor.name)))         

            if isRightSide:
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
    
    #"Resets" graph so BFSfull or nyDijkstra can be run back to back on the same graph
    def resettGraf(self):
        self.currentVisitBoolean = not self.currentVisitBoolean
    
    #Finds the actual actor objects that correspond to input ids.
    def lagActorFraId(self, nmIdStart:str,nmIdSlutt:str) -> tuple:
        for actor in self.hovedGraf.keys():
            #Both if in case start and end is the same
            if actor.id == nmIdSlutt:
                sluttNode = actor
            if actor.id == nmIdStart:
                startNode = actor 
        return (startNode, sluttNode)
    
    #This method does the unwegihted BFS search (OPPGAVE 2)
    def BFSfull(self,  nmIdStart:str,nmIdSlutt:str):
        
            tuple = self.lagActorFraId(nmIdStart, nmIdSlutt)
            startNode, sluttNode = tuple[0], tuple[1]
            queue = deque()
            startNode.visited = self.currentVisitBoolean
            startNode.forrige = None
            queue.append(startNode)

            #While queue is not empty
            while len(queue) > 0:
                #Remove first item
                nodeKey = queue.popleft()

                #if statement for creating final path
                if nodeKey == sluttNode:
                    pathList = []
                    currentNode = nodeKey

                    #Build pathlist
                    while currentNode != None:
                        pathList.insert(0,currentNode)
                        currentNode = currentNode.forrige
    
                    self.printGrafSti(pathList)
                    self.resettGraf()
                    return
                #fi
                
                #Visits alle the neighbours of the node that was just removed from the queue, and places the unvisited
                # neighbours on the back of the deque    
                for naboer in self.hovedGraf[nodeKey]:
                    if not naboer[0].visited == self.currentVisitBoolean: 
                        naboer[0].visited = self.currentVisitBoolean
                        naboer[0].forrige = nodeKey
                        naboer[0].movieWithLast = naboer[1] #For usage in resultprinting
                        queue.append(naboer[0])
            print("finnes ingen vei")

    #Works very well, very fast and works with the same path several times in a role 
    def nyDijkstra(self, nmIdStart:str, nmIdSlutt:str) -> None:
        
        actors = self.lagActorFraId(nmIdStart, nmIdSlutt)
        startNode, sluttNode = actors[0],actors[1]
        startNode.visited, startNode.forrige, startNode.totalWeight, sluttNode.totalWeight = self.currentVisitBoolean, None, 0, 10
        que = deque()
        priorityuQue = [deque() for i in range(610)]
        que.append(startNode)
        priorityuQue[0].append(startNode)

        
        while len(que) > 0:

            poppetNode = que.popleft()
            #Since the lowest possible resistance is 10-9.2 = 0.8; n = 0.8 is the safe number
            #But for runtimeflex put n = 2.6 
            if poppetNode.totalWeight+ 2.6> sluttNode.totalWeight:   
                continue

            for tuples in self.hovedGraf[poppetNode]:
                
                if tuples[0].totalWeight > poppetNode.totalWeight + (10-tuples[1].rating):
                    kopi = tuples[0]
                    kopi.totalWeight = round(poppetNode.totalWeight + (10-tuples[1].rating), 1)  #Have to add this because python cant do 1.6 + 2.7 correct....
                    kopi.forrige = poppetNode
                    kopi.movieWithLast = tuples[1]    
                    kopi.visited = self.currentVisitBoolean  
                    que.append(kopi) 
                    priorityuQue[int((kopi.totalWeight)*10)].append(kopi)
        
        #Sjekk <3  
        while any(priorityuQue):
            #Remove first item
            for dq in priorityuQue:
                if dq:
                    popNode = dq.popleft()
                    
                    break
        
            if popNode == sluttNode:
                pathList = []
                currentNode = popNode
                #Build pathlist
                while currentNode != None:
                    pathList.insert(0,currentNode)
                    currentNode = currentNode.forrige

                self.printGrafSti(pathList)
                self.resettGraf()
                print(f"Total weight: {popNode.totalWeight}\n")
                """ for actors in self.hovedGraf.keys():
                    actors.totalWeight = 100 """
                return
            popNode.totalWeight = 10



        

            
