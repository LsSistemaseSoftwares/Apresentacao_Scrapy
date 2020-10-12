import scrapy
from ..items import ItensMercadoLivre

class PostsSpider(scrapy.Spider):
    name = "MercadoLivre"

    start_urls = [
        'https://celulares.mercadolivre.com.br/#menu=categories',
        'https://games.mercadolivre.com.br/video-games/#menu=categories',
        'https://esportes.mercadolivre.com.br/futebol-equipamento-e-treinamento-bolas/#menu=categories'
    ]

    def parse(self, response):
        itens = ItensMercadoLivre()

        for produto in response.css('.andes-card--padding-default'):
            nome_produto = produto.css('.ui-search-item__title::text').extract()
            preço_produto = produto.css('.ui-search-price__second-line .price-tag-fraction').css('::text').extract()
            frete_grátis = produto.css('.ui-search-item__shipping--free::text').extract()
            avaliações_produto = produto.css('.ui-search-reviews__amount::text').extract()

            itens['nome_produto'] = nome_produto
            itens['preco_produto'] = preço_produto
            itens['frete_gratis'] = frete_grátis
            itens['avaliacoes_produto'] = avaliações_produto

            yield itens
