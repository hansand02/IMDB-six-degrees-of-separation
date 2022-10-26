from graph import Graph

EXPECTEDVALUES = (5068918,119205)

def sjekk(graf:Graph):
    return graf.hentVerdier() == EXPECTEDVALUES

if __name__ == "__main__":
    oppgave2 = Graph()
    oppgave2.les("../data/movies.tsv", "../data/actors.tsv")
    oppgave2.lagGraf()
    print(oppgave2.hentVerdier())
    print(sjekk(oppgave2), "oppgaven er løst")
