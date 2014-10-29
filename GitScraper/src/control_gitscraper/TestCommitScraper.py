#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 28/10/2014

@author: vagner
'''

import requests
import json
from requests.exceptions import RequestException, ConnectionError, HTTPError,\
    URLRequired, Timeout
from control_gitscraper.GitScaperError import GitScrapeError
from control_gitscraper.Commit import Commit


if __name__ == '__main__':
    url_base = "https://api.github.com/repos/junit-team/junit/commits?access_token=29bd7d59b8a227b60e0c8b0aa2e517c2963bd398&per_page=100&page="
    
    list_proj_recuperados = []
    page = 20
    
    while True:
            url = url_base + str(page)
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
                print 'Recuperando dados de {0}'.format(url)
                json_data = response.json()
                
                if len (json_data) > 0:
                    for p in  json_data:
                        raw_json = json.dumps(p, indent=1)
                        list_proj_recuperados.append(raw_json)
                else:
                    break
                
                page +=1          
                
            else:
                break
    #Saindo do While
    for c in list_proj_recuperados:
        try:
            
            commit = Commit(25,json.loads(c))
            commit.show_parents()
        except GitScrapeError as gerror:
            pass    
       
    