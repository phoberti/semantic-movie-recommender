# Semantic Movie Recommender

Este projeto implementa uma base de conhecimento para recomendação de filmes utilizando Redes Semânticas e RDF (Resource Description Framework).

Desenvolvido como parte da disciplina de Representação do Conhecimento no curso de Ciência da Computação da Universidade Estadual do Oeste do Paraná (UNIOESTE).

---

## 1. Visão Geral do Projeto

O objetivo do projeto é modelar um grafo semântico que represente as relações entre:

* Filmes
* Gêneros
* Atores
* Diretores
* Estúdios

Utilizando tripletas RDF (sujeito–predicado–objeto), o sistema constrói uma base estruturada de conhecimento capaz de sustentar recomendações de filmes de forma mais inteligente e explicável.

---

## 2. Representação do Conhecimento

O formalismo adotado foi a Rede Semântica, implementada com:

* RDF (Resource Description Framework)
* RDFS (RDF Schema)
* Python com a biblioteca RDFlib

Cada entidade é representada como uma URI, e as relações são modeladas como propriedades RDF.

Exemplo de tripletas:

```
Deadpool_Wolverine  pertenceAoGenero  Acao
Ryan_Reynolds       atuouEm           Deadpool_Wolverine
```

---

## 3. Tecnologias Utilizadas

* Python 3
* RDFlib
* Requests
* API do TMDb (The Movie Database)
* RDF/XML
* Virtualenv (Linux Ubuntu)
* Visual Studio Code

---

## 4. Fonte dos Dados

Os dados dos filmes são obtidos através da API do TMDb:

[https://www.themoviedb.org/](https://www.themoviedb.org/)

O sistema coleta:

* Filmes populares
* Gêneros
* Elenco
* Diretores
* Estúdios de produção

---

## 5. Funcionamento do Sistema

1. Consulta filmes populares na API do TMDb
2. Obtém detalhes e informações de elenco
3. Cria um grafo RDF
4. Define classes e propriedades:

   * Filme
   * Genero
   * Ator
   * Diretor
   * Estudio
5. Insere tripletas RDF no grafo
6. Exporta o grafo no formato RDF/XML

---

## 6. Como Executar

### 1. Clonar o repositório

```
git clone https://github.com/phoberti/semantic-movie-recommender.git
cd semantic-movie-recommender
```

### 2. Criar ambiente virtual

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```
pip install rdflib requests
```

### 4. Configurar chave da API

No arquivo `redesemantica.py`, defina sua chave:

```
API_KEY = "sua_api_key_aqui"
```

### 5. Executar o script

```
python3 redesemantica.py
```

Após a execução, será gerado um arquivo RDF/XML contendo o grafo semântico.

---

## 7. Visualização do Grafo

O arquivo RDF gerado pode ser visualizado utilizando:

* RDF Grapher
  [https://www.ldf.fi/service/rdf-grapher](https://www.ldf.fi/service/rdf-grapher)

* WebProtégé
  [https://webprotege.stanford.edu/](https://webprotege.stanford.edu/)

---

## 8. Possíveis Melhorias Futuras

* Implementação de consultas SPARQL
* Inclusão de regras de inferência
* Modelagem de preferências do usuário
* Integração com avaliações e críticas
* Expansão do grafo para maior volume de dados

---

## 9. Referências Acadêmicas

* ADOMAVICIUS, G.; TUZHILIN, A. Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, 2005.
* HENDLER, J.; LASSILA, O. The Semantic Web. Scientific American, 2001.
* W3C. RDF – Resource Description Framework.

---

## 10. Autores

Pedro Henrique de Oliveira Berti


Luiz Eduardo Garzon de Oliveira

UNIOESTE – 2024
