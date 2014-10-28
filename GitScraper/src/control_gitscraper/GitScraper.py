#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 27/10/2014

@author: vagner
'''
import requests
import json
from requests.exceptions import RequestException, ConnectionError, HTTPError,\
    URLRequired, Timeout
from control_gitscraper.GitScaperError import GitScrapeError

class GitScraper(object):
    '''
       Classe que realiza o processo de 
       Scraper de Projetos do GitHub
    '''
    __BASIC_URL = 'https://api.github.com/search/repositories?'
    __ACESS_TOKEN = '29bd7d59b8a227b60e0c8b0aa2e517c2963bd398'

    def __init__(self):
        '''
              Do nothing             
        '''
        
    def __get_dict_links(self,response_header):
        
        '''----------------------------------------------
           Função que recebe um cabeçalho de response
           e retorna um novo dictionary com os links
           da próxima página e a última página da
           consulta proposta    
        ------------------------------------------------'''
        
        #Recupera a string com os dados dos links
        links = response_header['link']
        
        '''*******************************
          Removendo os caracteres:
           - " " Espaço
           - >   Maior
           - <  Menor
        *******************************'''
        links = links.replace(" ", "") 
        links = links.replace("<", "") 
        links = links.replace(">", "") 
        
        #Criando uma lista da string
        list_pages = links.split(",")
        
        #Criando uma nova lista com o primeiro 
        #item da lista
        next_page =  list_pages[0].split(";")
        
        #Criando uma nova lista com o segundo 
        #item da lista
        last_page =  list_pages[1].split(";")
        
        dict_links = dict(next=next_page[0],last=last_page[0])
        
        return dict_links
     
    def run_query(self, language='java', sort='forks', order='des'):
        '''
            Retorna uma lista de Projestos no formato JSON
            com base na language, sort e order informado       
        
        '''
        list_proj_recuperados = [] # A lista de projetos a ser retornado
        '''-----------------------------------------------------------------
        Criando a URL DE CONSULTA
        -------------------------------------------------------------------'''
        url = self.__BASIC_URL+ 'access_token=' + self.__ACESS_TOKEN + '&'
        url = url + 'q=language:'   + language + '&'
        url = url + 'sort='         + sort + '&'
        url = url + 'order='        + order
        
        while True:
            try:
                response = requests.get(url)
            except RequestException as e:
                raise GitScrapeError('There was an ambiguous exception that occurred while handling your request.Vide erro: {0}'.format(e))
            except ConnectionError as e:
                raise GitScrapeError('Ocorreu um erro de conexão. Detalhes: {0}'.format(e))
            except HTTPError as e:
                raise GitScrapeError('Ocorreu um erro de HTTP. Detalhes: {0}'.format(e))
            except URLRequired as e:
                raise GitScrapeError('A URL informada {0} não é válida. Detalhes: {1}'.format(url,e))
            except Timeout as e:
                raise GitScrapeError('Timeout da conexão. Detalhes: {0}'.format(e))
            
            '''----------------------------------------
                    Verificando se a conexao ocorreu
                    corretamente.
            ------------------------------------'''
            if response.status_code == 200:
                json_data = response.json()
                
                if json_data["total_count"] > 0:
                    
                    for p in  json_data["items"]:
                        raw_json = json.dumps(p, indent=1)
                        
                        list_proj_recuperados.append(raw_json)
                        
                dict_links = self.__get_dict_links(response.headers)
                next_page = dict_links['next']
                last_page = dict_links['last']
                if next_page == last_page:
                    break
                else:
                    url = next_page
            else:
                return list_proj_recuperados
        #Saindo do While
        return list_proj_recuperados