# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItensMercadoLivre(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nome_produto = scrapy.Field()
    preco_produto = scrapy.Field()
    frete_gratis = scrapy.Field()
    avaliacoes_produto = scrapy.Field()

