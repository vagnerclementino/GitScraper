#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 18/10/2014

@author: Vagner Clementino
'''
import requests
import json
import psycopg2


def get_dict_links(response_header):
    
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

def insert_raw_projects_data(a_cur, a_json_data):
    SQL_QUERY = '''INSERT INTO raw_projects_data(id_raw_projects_data,json_data)
                   VALUES(nextval('raw_projects_data_id_raw_projects_data_seq'), %s);
                '''
    a_cur.execute(SQL_QUERY,(a_json_data,))    
    

if __name__ == '__main__':
    url = 'https://api.github.com/search/repositories?'         #basic URL
    ACESS_TOKEN ='29bd7d59b8a227b60e0c8b0aa2e517c2963bd398'     #TOKEN DE ACESSO
    LANGUAGE = 'java'                                           #Linguam dos projetos
    SORT = 'forks'                                              #Critério de ordenação
    ORDER = 'desc'                                              #Tipo de ordenação dos dados    
    '''-----------------------------------------------------------------
        Criando a URL DE CONSULTA
    -------------------------------------------------------------------'''
    url = url + 'access_token=' + ACESS_TOKEN + '&'
    url = url + 'q=language:'   + LANGUAGE + '&'
    url = url + 'sort='         + SORT + '&'
    url = url + 'order='        + ORDER
    print url
    list_proj_recuperados = []
    index = 1
    #output_file = open('../outs/projects_data.json','w')
    
    
    #Criando conexão com o banco de dados
    conn = psycopg2.connect("dbname=mes user=mes password=mes2014")
    
    cur = conn.cursor()
    
    
    while True:         
        
        response = requests.get(url)    
    
        '''------------------------------------
        Verificando se a conexao ocorreu
        corretamente.
        ------------------------------------'''
        if response.status_code == 200 :   
   
            
            json_data = response.json()
            for p in  json_data["items"]:
                raw_json = json.dumps(p, indent=1)
                list_proj_recuperados.append(raw_json)
                #Escrevendo os dados em um arquivo
                #json.dump(raw_json , output_file)
                #Inserindo os dados no banco 
                insert_raw_projects_data(cur, raw_json)           
           
            dict_links = get_dict_links(response.headers)
            
            next_page = dict_links['next']
            last_page = dict_links['last']
            
            
            if next_page == last_page:                
                break
            else:
                url = next_page
        else:
            break
    for project in list_proj_recuperados:
        
        project_data = json.loads(project)
        
       
        print ("%d -  %s - %s" % (index , project_data['full_name'] , project_data['html_url']))
        print '*****************************************************'
        index += 1
    print('Total de projetos recuperados: %d' % len(list_proj_recuperados))
    print('Everythig ins gonna be alright!')
    
    conn.commit()
    cur.close()
    conn.close()
    
