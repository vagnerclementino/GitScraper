#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 28/10/2014

@author: vagner
'''
from control_gitscraper.GitScaperError import GitScrapeError
from datetime import datetime

class Commit(object):
    '''
    Representa o commit de um projeto
    '''


    def __init__(self, project_code=None, raw_json_data=None):
        '''
        Constructor
        '''
        self.__commit_parents = []
        try:
            self.__project_code = project_code
        except ValueError as e:
            raise GitScrapeError('Atributo __project_code: Erro na conversão de valores. Detalhes: {0}'.format(e))
        
        try:
            self.__commit_json_data = raw_json_data
        except ValueError as e:
            raise GitScrapeError('Atributo ____commit_json_data: Erro na conversão de valores. Detalhes: {0}'.format(e))
        
        try:
            self.__sha = str(raw_json_data['sha'])
        except ValueError as e:
            raise GitScrapeError('Atributo __sha: Erro na conversão de valores. Detalhes: {0}'.format(e))        
        
        try:
            self.__commit_author = str(raw_json_data['commit']['author']['name'])
            
        except ValueError as e:
            raise GitScrapeError('Atributo commit_author: Erro na conversão de valores. Detalhes: {0}'.format(e))
         
        try:
            self.__commit_author_email = str(raw_json_data['commit']['author']['email'])
        except Exception as e:
            raise GitScrapeError('Atributo __commit_author_login: Erro na conversão de valores. Detalhes: {0}'.format(e))
                 
        try:
            self.__commit_date = datetime.strptime(raw_json_data['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError as e:
            raise GitScrapeError('Atributo __commit_author_id: Erro na conversão de valores. Detalhes: {0}'.format(e))
        
        
        try:
            self.__committer_name = str(raw_json_data['commit']['committer']['name'])
        except ValueError as e:
            raise GitScrapeError('Atributo __committer_name: Erro na conversão de valores. Detalhes: {0}'.format(e))
         
         
        try:
            self.__committer_email = str(raw_json_data['commit']['committer']['email'])
        except ValueError as e:
            raise GitScrapeError('Atributo __committer_email: Erro na conversão de valores. Detalhes: {0}'.format(e))        
         
        try:
            self.__committer_date = datetime.strptime(raw_json_data['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError as e:
            raise GitScrapeError('Atributo __committer_date: Erro na conversão de valores. Detalhes: {0}'.format(e))
        
        
        try:
            self.__message = unicode(raw_json_data['commit']['message'])
        except ValueError as e:
            raise GitScrapeError('Atributo __message: Erro na conversão de valores. Detalhes: {0}'.format(e))
        
        
        for p in raw_json_data['parents']:
            try:
                self.__commit_parents.append(p['sha'])
            
            except ValueError as e:
                raise GitScrapeError('Atributo __commit_parents: Erro na conversão de valores. Detalhes: {0}'.format(e))
        
    def get_message(self):
        
        return self.__message
        
    def show_parents(self): 
        
        index = 1
        
        for p in self.__commit_parents:
            print 'Parent {0}: {1} '.format(index,p)   
            
        
