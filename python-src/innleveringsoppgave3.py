from graph import Graph
import timeit 

EXPECTEDVALUES = (5068918,119205)

if __name__ == "__main__":

    
    ans = input("Fast or safe? (f/s)").lower()

    def total() -> None:
        oppgave2 = Graph(fast= ans == "f")  

        def Hjelpefunksjon():
            
            input("Oppgave 1: \nTrykk enter!:")
            print()
            floatBygg =  timeit.timeit(bygg, number=1)
            floatTest = timeit.timeit(test, number=1)
            print(f"\n{floatBygg:.5f}s to build graph")
            print(f"{floatTest:.5f}s to validate graph\n")
            
            
            input("Oppgave 2\nTrykk enter!:")
            floatSearch = timeit.timeit(searchUnweighted, number=1)
            print(f"{floatSearch:.5f}s to search shortest path x5\n")
            
            input("Oppgave 3\nTrykk enter!:")
            floatSearchWeighted = timeit.timeit(searchWeighted, number=1)
            print(f"{floatSearchWeighted:.5f}s to search easiest path x5\n")
    
            input("Oppgave 4\nTrykk enter!:")
            floatKomponent = timeit.timeit(findComponents, number=1)
            print("="*45)
            print(f"{floatKomponent:.5f}s to find components\n")

            print("="*56)
            print(f"{(floatBygg+floatTest+floatSearch+floatSearchWeighted+ floatKomponent):.5f} s for å prossesere oppgave 1-4")

        def bygg():  
            """ Oppgave 1 """  
            oppgave2.lesOgLag("../data/movies.tsv", "../data/actors.tsv")
        
        def test():
            """ Oppgave 1 """
            verdier = oppgave2.hentVerdier()
            print(f"Nodes: {verdier[1]} \nEdges: {verdier[0]}")
            assert verdier == EXPECTEDVALUES
      
        def sjekkTest(graf:Graph, verdier:tuple) -> bool:
            """ More accurate extension of test, doublecheck the validity of test """
            return graf.kontrollerVerdier() == EXPECTEDVALUES

        def searchUnweighted():
            """ Oppgave 2 """
            oppgave2.BFSfull("nm2255973","nm0000460")  
            oppgave2.BFSfull("nm0424060","nm0000243")  
            oppgave2.BFSfull("nm4689420","nm0000365")  
            oppgave2.BFSfull("nm0000288","nm0001401")  
            oppgave2.BFSfull("nm0031483","nm0931324")  

        def searchWeighted(): 
            """ Oppgave 3 """
            oppgave2.nyDijkstra("nm2255973","nm0000460")   
            oppgave2.nyDijkstra("nm0424060","nm0000243")  
            oppgave2.nyDijkstra("nm4689420","nm0000365")  
            oppgave2.nyDijkstra("nm0000288","nm0001401") 
            oppgave2.nyDijkstra("nm0031483","nm0931324")  
             
        def findComponents():
            oppgave2.findComponents()

        Hjelpefunksjon()

    stringTotal = (f"Men {timeit.timeit(total, number=1):.5f}s tok det totalt med litt OStime og din input")
    print(stringTotal)
    print("="*56)