import chromadb

client = chromadb.Client()

def store_embeddings_in_chromadb(embeddings, metadata):
    # Criar uma coleção no ChromaDB
    collection = client.create_collection("privacy_policy")
    
    # Adicionar embeddings e metadados
    collection.add(embeddings, metadata)
    print("Embeddings adicionados ao ChromaDB.")

def retrieve_from_chromadb(query):
    # Recuperar informações baseadas no embedding da consulta
    collection = client.get_collection("privacy_policy")
    
    # Pesquisar a resposta mais relevante no ChromaDB
    results = collection.query(query)
    return results
