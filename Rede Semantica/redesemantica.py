import requests
from rdflib import Graph, Namespace, RDF, RDFS, URIRef

#config
API_KEY = '5f3d37b7db5f82624c4baeffc563be36' #api do Tmdb, gratis para estudantes / fins academicos
BASE_URL = 'https://api.themoviedb.org/3' 

#criacao do grafo
g = Graph()
ns = Namespace("http://example.org/") #obrigatorio ter um ns

#classes
g.add((ns.Filme, RDF.type, RDFS.Class))
g.add((ns.Genero, RDF.type, RDFS.Class))
g.add((ns.Ator, RDF.type, RDFS.Class))
g.add((ns.Diretor, RDF.type, RDFS.Class))
g.add((ns.Estúdio, RDF.type, RDFS.Class))

#propriedades, todas seram tambem agrupadas no property dentro do grafo
g.add((ns.pertenceAoGenero, RDF.type, RDF.Property))
g.add((ns.pertenceAoGenero, RDFS.domain, ns.Filme))
g.add((ns.pertenceAoGenero, RDFS.range, ns.Genero))

g.add((ns.temAtor, RDF.type, RDF.Property))
g.add((ns.temAtor, RDFS.domain, ns.Filme))
g.add((ns.temAtor, RDFS.range, ns.Ator))

g.add((ns.atuouEm, RDF.type, RDF.Property))
g.add((ns.atuouEm, RDFS.domain, ns.Ator))
g.add((ns.atuouEm, RDFS.range, ns.Filme))

g.add((ns.dirigidoPor, RDF.type, RDF.Property))
g.add((ns.dirigidoPor, RDFS.domain, ns.Filme))
g.add((ns.dirigidoPor, RDFS.range, ns.Diretor))

g.add((ns.produzidoPeloEstudio, RDF.type, RDF.Property))
g.add((ns.produzidoPeloEstudio, RDFS.domain, ns.Filme))
g.add((ns.produzidoPeloEstudio, RDFS.range, ns.Estúdio))

#buscar filmes
def buscar_filmes_populares(pagina=1):
    url = f"{BASE_URL}/movie/popular"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR',
        'page': pagina
    }
    resposta = requests.get(url, params=params)
    return resposta.json()

#buscar as informacoes dos filmes
def buscar_detalhes_filme(filme_id):
    url = f"{BASE_URL}/movie/{filme_id}"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR'
    }
    resposta = requests.get(url, params=params)
    return resposta.json()

#func para elenco
def buscar_elenco_filme(filme_id):
    url = f"{BASE_URL}/movie/{filme_id}/credits"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR'
    }
    resposta = requests.get(url, params=params)
    return resposta.json()

#coleta de dados
filmes = buscar_filmes_populares(pagina=1)['results']

for filme in filmes[:2]:  #quantidade de filmes
    filme_id = filme['id']
    detalhes = buscar_detalhes_filme(filme_id)
    elenco = buscar_elenco_filme(filme_id)

    #instancias do grafo
    filme_uri = URIRef(ns[detalhes['title'].replace(" ", "")])
    g.add((filme_uri, RDF.type, ns.Filme))
    
    #adcionar genero
    for genero in detalhes['genres']:
        genero_uri = URIRef(ns[genero['name'].replace(" ", "")])
        g.add((genero_uri, RDF.type, ns.Genero))
        g.add((filme_uri, ns.pertenceAoGenero, genero_uri))
    
    #adcionar atores
    for membro in elenco['cast'][:1]:  #quantidade de atores, atualmente pegando somente o principal
        ator_uri = URIRef(ns[membro['name'].replace(" ", "")])
        g.add((ator_uri, RDF.type, ns.Ator))
        g.add((filme_uri, ns.temAtor, ator_uri))
        g.add((ator_uri, ns.atuouEm, filme_uri))
    
    #adcionar diretor
    for membro in elenco['crew']:
        if membro['job'] == 'Director':
            diretor_uri = URIRef(ns[membro['name'].replace(" ", "")])
            g.add((diretor_uri, RDF.type, ns.Diretor))
            g.add((filme_uri, ns.dirigidoPor, diretor_uri))
            break

    #adcionar o estudio de producao
    if detalhes.get('production_companies'):
        estúdio = detalhes['production_companies'][0]  #como alguns filmes sao produzidos por mais de um estudio, foi setado para pegar apenas o estudio principal
        estúdio_uri = URIRef(ns[estúdio['name'].replace(" ", "")])
        g.add((estúdio_uri, RDF.type, ns.Estúdio))
        g.add((filme_uri, ns.produzidoPeloEstudio, estúdio_uri))

#salvar a rede
g.serialize(destination="redesemantica.rdf", format="xml")

print("rede salva com sucesso")
