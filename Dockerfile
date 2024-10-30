# Usa a imagem oficial do Python 3
FROM python:3.10

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para dentro do contêiner
COPY . /app

# Instala as dependências (caso tenha um requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Comando para manter o contêiner ativo
CMD ["python3"]
