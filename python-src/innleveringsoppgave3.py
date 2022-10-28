from graph import Graph
import timeit 
import dis
EXPECTEDVALUES = (5068918,119205)

def sjekk(graf:Graph, verdier:tuple) -> bool:
    return graf.hentVerdier() == EXPECTEDVALUES

if __name__ == "__main__":
    def arbeid() -> None:
        oppgave2 = Graph()
        
        def bygg():
            print("Oppgave 2\n")
            oppgave2.les("../data/movies.tsv", "../data/actors.tsv")
            oppgave2.lagGraf()
        stringBygg = f"{timeit.timeit(bygg, number=1):.5f} to build graph"

        def test():
            verdier = oppgave2.hentVerdier()
            print(f"\nNodes: {verdier[1]} \nEdges: {verdier[0]}")
        stringTest = f"{timeit.timeit(test, number=1):.5f} to validate graph"

        def search():
            oppgave2.BFSfull("nm0031483","nm0931324")
        stringSoek = f"{timeit.timeit(search, number=1):.5f} to search through graph"
        
        print(stringBygg + "\n" + stringTest + "\n" + stringSoek + "\n")
    
    print(f"{timeit.timeit(arbeid, number=1):.5f} total")
    