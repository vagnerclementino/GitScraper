'''
Created on 18/10/2014

@author: Vagner Clementino
'''
import requests
from lxml import html

if __name__ == '__main__':
    #url = 'https://github.com/search?l=Java&q=language%3AJava&ref=advsearch&type=Repositories&utf8=%E2%9C%93&p='
    url = 'https://api.github.com/search/repositories?q=language:java&sort=stars&order=desc&page=2'
    offset = 1
    total_recuperado = 0
    linha = 1
    list_proj_recuperados = []
    #price
    url_nova = url + str(offset)    
    while total_recuperado < 200:
        
    # print(url_nova)
        page = requests.get(url_nova)
        #print(page)
        #print(page.status_code)
        print(page.json())
        tree = html.fromstring(page.text)
        #print (tree)
        price = tree.xpath('//*[@id="container"]/div[2]/div[2]/ul/li[%d]/h3/a/@href' % (linha))
        #price = tree.xpath('//*[@id="container"]/div[2]/div[2]/ul/li[%d]/div[1]/text()' % (linha))
        
        #for p in price:
        if len(price) > 0 :
            list_proj_recuperados.append(str(price[0]).strip(' '))
            print('%d - %s' % (total_recuperado + 1, str(price[0]).strip(' ')))       
            total_recuperado += 1
            linha += 1
        if linha == 10 :
            offset += 1
            linha = 1
            url_nova = url + str(offset)
            print('---------------------PAGINACAO---------------------------------')
    print('Total de projestos recuperados: %d' % len(list_proj_recuperados))
    for p in list_proj_recuperados:
        print p
    print('Everything is gonna be alright!')    
                        
       
                 
        
