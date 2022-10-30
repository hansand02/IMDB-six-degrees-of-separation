from graph import Graph
import timeit 
import dis
EXPECTEDVALUES = (5068918,119205)


if __name__ == "__main__":

    #To make a boolean for graph validity
    #A double check to the already implemented "test()"
    def sjekk(graf:Graph, verdier:tuple) -> bool:
        return graf.kontrollerVerdier() == EXPECTEDVALUES

    def arbeid() -> None:
        oppgave2 = Graph()
        
        def bygg():
            print("Oppgave 2\n")
            oppgave2.les("../data/movies.tsv", "../data/actors.tsv")
            oppgave2.lagGraf()
        stringBygg = f"{timeit.timeit(bygg, number=1):.5f}s to build graph"

        def test():
            verdier = oppgave2.hentVerdier()
            print(f"Nodes: {verdier[1]} \nEdges: {verdier[0]}")
            assert verdier == EXPECTEDVALUES
        stringTest = f"{timeit.timeit(test, number=1):.5f}s to validate graph"
        
        def search():
            oppgave2.BFSfull("nm0749263","nm0000375")
        stringSoek = f"{timeit.timeit(search, number=1):.5f}s to search through graph"
        
        print(stringBygg + "\n" + stringTest + "\n" + stringSoek + "\n")
    
    print(f"{timeit.timeit(arbeid, number=1):.5f}s total")
    