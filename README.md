# Apresentacao_Scrapy

Repositório criado para hospedar o programa criado em Python 3.8 e Scrapy para apresentação.

## Funcionamento

Um robô que acessa 3 páginas diferentes do domínio: mercadolivre.com.br, utiliza um UserAgent para acessar os dados dos produtos hospedados nas páginas. Em cada página são coletados os seguintes dados: 
  Nome do Produto;
  Preço do Produto;
  Frete é Grátis; e
  Avaliações do Produto, caso disponível.

## Rodando o programa
Baixe o repositório para o seu computador, no Terminal.. vá para o diretório e digite o seguinte comando para executar o script:
  scrapy crawl MercadoLivre
  
Recomenda-se que extraia o resultado usando o seguinte comando no terminal:
  scrapy crawl MercadoLivre -o result.csv
Ou
  scrapy crawl MercadoLivre -o result.json

Aguarde alguns segundos e um arquivo de resultado será gerado.
