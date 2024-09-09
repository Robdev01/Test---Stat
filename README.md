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
