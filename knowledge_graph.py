from rdflib import Graph, URIRef

g = Graph()

g.add((URIRef("Goa"), URIRef("type"), URIRef("Beach")))
g.add((URIRef("Goa"), URIRef("hasFood"), URIRef("Seafood")))

for s,p,o in g:
    print(s, p, o)
