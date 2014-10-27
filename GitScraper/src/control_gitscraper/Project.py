#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 26/10/2014

@author: Vagner Clementino
'''
from datetime import datetime
from control_gitscraper.GitScaperError import GitScrapeError
import json

class Project(object):
    '''
    Representa os dados e comportamento de um projeto do GitHub
    
    ATRIBUTOS:
        * __project_json_data (json) :  Os dados do projeto no formato JSON
        * __git_project_cod   (integer):  Armazena o código do projeto no GitHub
        * __project_name      (string) :  O nome do projeto
        * __description       (string):   A descrição do projeto
        * __project_lang      (string):   A linguagem utilazada no projeto
        * __create_data       (datetime): Data e hora de criação do projeto
        * __project_owner     (string):   Login de usuário no GitHub do criador do projeto
        * __project_url       (string):   A URL do projeto no GitHub
        * __clone_url         (string):   A URL utilizada para reliazar o clone do projeto
        * __commits_url       (string)    A URL com os dados dos commits do projeto
        * __git_url           (string)    A URL para acesso do projeto através do protocolo git
        * __api_url           (string)    A URL para acesso a API do gitHub para o projeto em questão
        * __stargazers_count  (integer)   O total de stargazers do projeto
        * __forks_count       (integer)   O total de forks do projeto
        * __watchers_count    (integer)   O total de watchers do projeto
        * __project_size      (integer)   O tamanho do projeto em KB
        * __last_update       (datetime)  A data de última atualização do projeto
        * __private           (boolean)   Informa se o dados do projeto são publicos
        * __default_branche   (string)    O nome da branche padrão do projeto
    '''


    def __init__(self, a_proj_json_data=None):
        '''
        Recebe os dados do projeto no formato JSON, armazenando-o para
        posterior uso. Os demais atributo são criados com base nos dados recebidos em
        JSON
        '''        
        try:
            self.__project_json_data = a_proj_json_data
        except ValueError as e:
            raise GitScrapeError('Atributo __project_json_data: Erro na conversão de tipo. Vide erro: {0}'.format(e))
        try:
            self.__git_project_cod = int(a_proj_json_data["id"])
        except ValueError as e:
            raise GitScrapeError('Atributo __git_project_cod: Erro na conversão de tipo. Vide erro: {0}'.format(e))
        try:         
            self.__project_name = str(a_proj_json_data["name"])
        except ValueError as e:
            raise GitScrapeError('Atributo __project_name: Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:    
            self.__description = unicode(a_proj_json_data["description"])
        except ValueError as e:
            raise GitScrapeError('Atributo __description: Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:    
            self.__project_lang = str(a_proj_json_data["language"])
        except ValueError as e:
            raise GitScrapeError('Atributo __project_lang: Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:    
            self.__create_data = datetime.strptime(a_proj_json_data["created_at"], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError as e:
            raise GitScrapeError('Atributo __create_data: Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:    
            self.__project_owner = str(a_proj_json_data["owner"]["login"])
        except ValueError as e:
            raise GitScrapeError('Atributo __project_owner : Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:    
            self.__project_url = str(a_proj_json_data["html_url"])
        except ValueError as e:
            raise GitScrapeError('Atributo __project_url: Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:    
            self.__clone_url = str(a_proj_json_data["clone_url"])
        except ValueError as e:
            raise GitScrapeError('Atributo __clone_url: Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:
            # Remove o padrão {/sha} da URL de commits
            self.__commits_url = str(a_proj_json_data["commits_url"]).replace('{/sha}', '')
        except ValueError as e:
            raise GitScrapeError('Atributo __commits_url Erro na conversão de tipo. Vide erro: {0}'.format(e))
        try:     
            self.__git_url = str(a_proj_json_data["git_url"])
        except ValueError as e:
            raise GitScrapeError('Atributo __git_url: Erro na conversão de tipo. Vide erro: {0}'.format(e))
        try:     
            self.__api_url = str(a_proj_json_data["url"])
        except ValueError as e:
            raise GitScrapeError('Atributo __api_url: Erro na conversão de tipo. Vide erro: {0}'.format(e))     
        try:     
            self.__stargazers_count = int(a_proj_json_data["stargazers_count"])
        except ValueError as e:
            raise GitScrapeError('Atributo __stargazers_count: Erro na conversão de tipo. Vide erro: {0}'.format(e))     
        try:     
            self.__forks_count = int(a_proj_json_data["forks"])
        except ValueError as e:
            raise GitScrapeError('Atributo __forks_count: Erro na conversão de tipo. Vide erro: {0}'.format(e))     
        try:     
            self.__watchers_count = int(a_proj_json_data["watchers"])
        except ValueError as e:
            raise GitScrapeError('Atributo self.__watchers_count : Erro na conversão de tipo. Vide erro: {0}'.format(e))     
        try:     
            self.__project_size = int(a_proj_json_data["size"])
        except ValueError as e:
            raise GitScrapeError('Atributo __project_size: Erro na conversão de tipo. Vide erro: {0}'.format(e))     
        try:     
            self.__last_update = datetime.strptime(a_proj_json_data["updated_at"], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError as e:
            raise GitScrapeError('Atributo __last_update: Erro na conversão de tipo. Vide erro: {0}'.format(e))    
        try:      
            self.__private = bool(a_proj_json_data["private"])
        except ValueError as e:
            raise GitScrapeError('Atributo self.__private: Erro na conversão de tipo. Vide erro: {0}'.format(e))     
        try:     
            self.__default_branche = str(a_proj_json_data["default_branch"])
        except ValueError as e:
            raise GitScrapeError('Atributo __default_branche: Erro na conversão de tipo. Vide erro: {0}'.format(e))     
            
        
        
        
    def get_project_json_data(self):
        return(json.dumps(self.__project_json_data,indent=1)) 
    
    def get_git_project_cod(self):
        return(self.__git_project_cod)
    
    def get_project_name(self):
        return(self.__project_name) 
      
    def get_description(self):
        return(self.__description)
    
    def get_project_lang(self):
        return(self.__project_lang)
    
    def get_create_data(self):
        return(self.__create_data)
    
    def get_project_owner(self):
        return (self.__project_owner)
    
    def get_project_url(self):
        return (self.__project_url)
    
    def get_clone_url(self):
        return(self.__clone_url)
    
    def get_commits_url(self):        
        return(self.__commits_url)
    
    def get_git_url(self):
        return (self.__git_url)
    
    def get_api_url(self):
        return (self.__api_url)
    
    def get_stargazers(self):
        return(self.__stargazers_count)
    
    def get_forks(self):
        return(self.__forks_count)
    
    def get_watchers(self):
        return(self.__watchers_count)
    
    def get_project_size(self):
        return(self.__project_size)
    
    def get_last_update(self):
        return(self.__last_update)
    
    
    def is_public(self):        
        return(not(self.__private))
    
    def get_default_branche(self):
        return (self.__default_branche)
    
    
    
    
        
        
   
    def show(self):
        
        '''-----------------------------------------------------------------------------------------
           Exibe os dados de um projeto
        
        ------------------------------------------------------------------------------------------'''        
        print('Dados do projeto: ')
        print('Código: %d' % (self.__git_project_cod))
        print('Nome: %s ' % self.__project_name)
        print('Descrição: %s' % self.__description)
        print('Linguagem: %s' % self.__project_lang)
        print('Data de Criação: %s' % str(self.__create_data))
        print ('Proprietário: %s' % (self.__project_owner))
        print( 'URL do Projeto: %s' % self.__project_url)
        print('Clone URL: %s' % self.__clone_url)
        print('Commit URL: %s' % self.__commits_url)
        print('Git URL: %s' % self.__git_url)
        print('API URL: %s' % self.__api_url)
        print('Total de stargazers: %d' % self.__stargazers_count)
        print('Total de forks: %d' % self.__forks_count)
        print('Tamanho do projeto: %d' % self.__project_size)
        print('Ultima atualização: %s' % str(self.__last_update))
        print ('Private Projeto? %s' % str(self.__private))
        print('Branche Padrão: %s' % self.__default_branche)
