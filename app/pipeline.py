from langchain.chains import SimpleChain
from langchain.embeddings import LlamaEmbedding
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_pipeline():
    # Dividir o texto para processamento
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    
    # Gerar embeddings usando o Llama3
    llama_embedding = LlamaEmbedding(model="Llama3")
    
    # Pipeline para pré-processar e gerar embeddings
    pipeline = SimpleChain(steps=[
        ("Split Text", text_splitter),
        ("Generate Embeddings", llama_embedding)
    ])
    
    return pipeline
