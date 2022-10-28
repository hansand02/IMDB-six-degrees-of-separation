from graph import Graph
import timeit 
EXPECTEDVALUES = (5068918,119205)

def sjekk(graf:Graph, verdier:tuple) -> bool:
    return graf.hentVerdier() == EXPECTEDVALUES

if __name__ == "__main__":
    def arbeid() -> None:
        print("Oppgave 1")
        oppgave2 = Graph()
        oppgave2.les("../data/marvel_movies.tsv", "../data/marvel_actors.tsv")
        oppgave2.lagGraf()
        verdier = oppgave2.hentVerdier()
        print(f"{sjekk(oppgave2, verdier)}, grafen er bygget riktig :=D \nNodes: {verdier[1]} \nEdges: {verdier[0]}")
        oppgave2.BFSfull("nm0000375", "nm0339460")
    print(f"{timeit.timeit(arbeid, number=1):.5f} sekunder for å bygge grafen")