# Dockerfile para LangChain, Llama3 e ChromaDB
FROM python:3.10-slim

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar os arquivos da aplicação
COPY . /app

# Instalar as bibliotecas necessárias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
