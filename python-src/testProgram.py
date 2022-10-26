from graph import Graph

EXPECTEDVALUES = (5068918,119205)

def sjekk(graf:Graph):
    return graf.hentVerdier()[0] == EXPECTEDVALUES

graf = Graph()
print(sjekk(graf))