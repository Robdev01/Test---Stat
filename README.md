# Navegar para o diretório do projeto
mkdir meu_projeto_langchain
cd meu_projeto_langchain

# Criar diretório e arquivos
mkdir app
mkdir docs

# Criar o arquivo requirements.txt
cat <<EOL > requirements.txt
langchain
llama-cpp-python
chromadb
PyPDF2
pdfminer.six
EOL

# Criar o Dockerfile
cat <<EOL > Dockerfile
# Dockerfile para LangChain, Llama3 e ChromaDB
FROM python:3.10-slim

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y \\
    gcc \\
    libgomp1 \\
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar os arquivos da aplicação
COPY . /app

# Instalar as dependências listadas no requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
EOL

# Criar o arquivo docker-compose.yml
cat <<EOL > docker-compose.yml
version: '3'
services:
  langchain_service:
    build: .
    container_name: langchain_container
    ports:
      - "8000:8000"
    volumes:
      - .:/app
      - ./docs:/app/docs
    depends_on:
      - chromadb_service

  chromadb_service:
    image: chromadb:latest
    container_name: chromadb_container
    ports:
      - "9000:9000"
EOL

# Criar o arquivo pdf_processor.py
cat <<EOL > app/pdf_processor.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
EOL

# Criar o arquivo pipeline.py
cat <<EOL > app/pipeline.py
from langchain.chains import TransformChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import LlamaEmbedding

def create_pipeline():
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    llama_embedding = LlamaEmbedding(model="Llama3")
    pipeline = TransformChain(steps=[
        ("Split Text", text_splitter),
        ("Generate Embeddings", llama_embedding)
    ])
    return pipeline
EOL

# Criar o arquivo chromadb_integration.py
cat <<EOL > app/chromadb_integration.py
from chromadb import Client

def store_embeddings_in_chromadb(embeddings, metadata):
    client = Client()  # Ajuste conforme necessário
    collection = client.create_collection(name="my_collection")
    collection.add(embeddings=embeddings, metadata=metadata)

def retrieve_from_chromadb(query):
    client = Client()  # Ajuste conforme necessário
    collection = client.get_collection(name="my_collection")
    result = collection.query(query)
    return result
EOL

# Criar o arquivo main.py
cat <<EOL > app/main.py
from pdf_processor import extract_text_from_pdf
from pipeline import create_pipeline
from chromadb_integration import store_embeddings_in_chromadb, retrieve_from_chromadb

def main():
    pdf_path = "/app/docs/politica_de_privacidade.pdf"
    text = extract_text_from_pdf(pdf_path)
    print("Texto extraído do PDF.")

    pipeline = create_pipeline()
    embeddings, metadata = pipeline.run(text)
    print("Embeddings gerados.")

    store_embeddings_in_chromadb(embeddings, metadata)
    print("Embeddings armazenados no ChromaDB.")

    query = "Qual é a política de privacidade sobre dados pessoais?"
    result = retrieve_from_chromadb(query)
    print(f"Resposta para a consulta: {result}")

if __name__ == "__main__":
    main()
EOL

# Criar o diretório e adicionar o PDF de exemplo
echo "Este é um exemplo de PDF." > docs/politica_de_privacidade.pdf

# Criar o arquivo README.md
cat <<EOL > README.md
# Projeto LangChain, Llama3 e ChromaDB

Este projeto configura um pipeline para processar textos extraídos de PDFs, gerar embeddings usando Llama3 e armazenar esses embeddings no ChromaDB. O projeto é containerizado usando Docker e Docker Compose para facilitar a configuração e execução do ambiente.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

\`\`\`
meu_projeto_langchain/
├── app/
│   ├── main.py
│   ├── pipeline.py
│   ├── pdf_processor.py
│   ├── chromadb_integration.py
├── docs/
│   └── politica_de_privacidade.pdf
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
\`\`\`

## Dependências

Certifique-se de que você tem as seguintes ferramentas instaladas:
- Docker
- Docker Compose

As dependências do Python são listadas em \`requirements.txt\`:

\`\`\`
langchain
llama-cpp-python
chromadb
PyPDF2
pdfminer.six
\`\`\`

## Configuração e Execução

### Passo 1: Instalar Docker e Docker Compose

Se ainda não tiver o Docker e o Docker Compose instalados, você pode encontrá-los e instalá-los aqui:

- [Instalação do Docker](https://docs.docker.com/get-docker/)
- [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

### Passo 2: Clonar o Repositório

Clone este repositório para o seu ambiente local:

\`\`\`
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
\`\`\`

### Passo 3: Construir e Iniciar os Contêineres

Construa e inicie os contêineres usando Docker Compose:

\`\`\`
docker-compose up --build
\`\`\`

### Passo 4: Estrutura dos Arquivos

- **\`app/main.py\`**: Orquestra o fluxo de processamento, desde a extração do texto do PDF até a consulta ao ChromaDB.
- **\`app/pdf_processor.py\`**: Contém a função para extrair texto de arquivos PDF.
- **\`app/pipeline.py\`**: Configura o pipeline para processar texto e gerar embeddings.
- **\`app/chromadb_integration.py\`**: Gerencia o armazenamento e recuperação de embeddings no ChromaDB.
- **\`docs/politica_de_privacidade.pdf\`**: Exemplo de arquivo PDF para processamento. Substitua pelo seu arquivo PDF.

## Configuração do Docker

- **\`Dockerfile\`**: Define a imagem Docker para o projeto.
- **\`docker-compose.yml\`**: Configura os serviços Docker e volumes.

## Consultas e Problemas

Se você encontrar algum problema ou tiver dúvidas, sinta-se à vontade para abrir uma [issue](https://github.com/seu-usuario/seu-repositorio/issues) no GitHub.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor, faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
EOL
