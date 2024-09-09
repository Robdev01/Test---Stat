from pdf_processor import extract_text_from_pdf
from pipeline import create_pipeline
from chromadb_integration import store_embeddings_in_chromadb, retrieve_from_chromadb

def main():
    # Caminho para o PDF
    pdf_path = "Politica_de_Privacidade.pdf"
    
    # Extrair texto do PDF
    text = extract_text_from_pdf(pdf_path)
    print("Texto extraído do PDF.")
    
    # Criar pipeline para processar o texto
    pipeline = create_pipeline()
    
    # Gerar embeddings do texto
    embeddings, metadata = pipeline.run(text)
    print("Embeddings gerados.")
    
    # Armazenar embeddings no ChromaDB
    store_embeddings_in_chromadb(embeddings, metadata)
    print("Embeddings armazenados no ChromaDB.")
    
    # Exemplo de consulta ao ChromaDB
    query = "Qual é a política de privacidade sobre dados pessoais?"
    result = retrieve_from_chromadb(query)
    print(f"Resposta para a consulta: {result}")

if __name__ == "__main__":
    main()
