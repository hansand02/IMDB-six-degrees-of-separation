from graph import Graph
import timeit 
import dis
import time
EXPECTEDVALUES = (5068918,119205)


if __name__ == "__main__":

    #To make a boolean for graph validity
    #A double check to the already implemented "test()"
    def sjekk(graf:Graph, verdier:tuple) -> bool:
        return graf.kontrollerVerdier() == EXPECTEDVALUES

    def arbeid() -> None:
        oppgave2 = Graph()
        
        def bygg():    
            oppgave2.les("../data/movies.tsv", "../data/actors.tsv")
            oppgave2.lagGraf()
        
        def Hjelpefunksjon():
            print("Oppgave 1\n")
            stringBygg = f"{timeit.timeit(bygg, number=1):.5f}s to build graph"
            stringTest = f"{timeit.timeit(test, number=1):.5f}s to validate graph"
            print("\n"+stringBygg)
            print(stringTest+ "\n")
            print("Oppgave 2")
            stringSearch = f"{timeit.timeit(searchUnweighted, number=1):.5f}s to search shortest path x5"
            print(stringSearch+"\n")
            stringSearchWeighted = f"{timeit.timeit(searchWeighted, number=1):.5f}s to search easiest path x5"
            print(stringSearchWeighted + "\n")

        def test():
            verdier = oppgave2.hentVerdier()
            print(f"Nodes: {verdier[1]} \nEdges: {verdier[0]}")
            assert verdier == EXPECTEDVALUES
        
        
        def searchUnweighted():
            oppgave2.BFSfull("nm2255973","nm0000460")  
            oppgave2.BFSfull("nm0424060","nm0000243")  
            oppgave2.BFSfull("nm4689420","nm0000365")  
            oppgave2.BFSfull("nm0000288","nm0001401")  
            oppgave2.BFSfull("nm0031483","nm0931324")  

        def searchWeighted(): 
            oppgave2.nyDijkstra("nm2255973","nm0000460")  
            oppgave2.nyDijkstra("nm2255973","nm0000460")  
            oppgave2.nyDijkstra("nm2255973","nm0000460")  
            oppgave2.nyDijkstra("nm2255973","nm0000460")  
            """ oppgave2.nyDijkstra("nm0424060","nm0000243")  
            oppgave2.nyDijkstra("nm4689420","nm0000365")  
            oppgave2.nyDijkstra("nm0000288","nm0001401") 
            oppgave2.nyDijkstra("nm0031483","nm0931324")   """
        
             
             
             
        Hjelpefunksjon()
    stringTotal = (f"{timeit.timeit(arbeid, number=1):.5f}s total")
    print(stringTotal, "For oppgave 1, 2 og 3 (2 og 3 fem ganger)")