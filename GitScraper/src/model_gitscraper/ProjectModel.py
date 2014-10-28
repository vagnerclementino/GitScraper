#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 27/10/2014

@author: vagner
'''
from model_gitscraper.ConnectionManager import ConnectionManager
import psycopg2
from datetime import datetime
from control_gitscraper.GitScaperError import GitScrapeError

class ProjectModel(object):
    '''
    Visa persistir os dados de um Projeto no banco de dados
    '''
    __DB_NAME =  'mes'
    __USER    =  'mes'
    __PASSWORD = 'mes2014'

    def __init__(self):
        '''
        Constructor
        '''
        self.__conn_manager = ConnectionManager(dbname = self.__DB_NAME, user = self.__USER, password = self.__PASSWORD)
        
    def __insert_raw_project_data(self, a_cur, a_json_data):
        SQL_INSERT = '''
                       INSERT INTO raw_projects_data(id_raw_projects_data,json_data, data_de_atualizacao)
                       VALUES(%s, %s, %s);
                    '''
        
        SQL_GET_SQ = ''' SELECT nextval('raw_projects_data_id_raw_projects_data_seq') '''
        
        
        try:
            a_cur.execute(SQL_GET_SQ) 
            
            a_register = a_cur.fetchone()
            
            sq_next_value = a_register[0]
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao obter o next valeu da sequence raw_projects_data_id_raw_projects_data_seq do banco: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror)) 
        
        try:
            a_cur.execute(SQL_INSERT, (sq_next_value,a_json_data, datetime.now()))
            
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao inserir na tabela raw_project_data: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))     
        
        return sq_next_value 
    
    def __insert_projects(self, a_cur,id_raw_projects_data, project):
        
        SQL_INSERT = '''INSERT INTO public.projects
                               (id_projects,
                               id_raw_projects_data,
                               git_project_cod,
                               project_name,
                               description,
                               project_lang,
                               create_data,
                               project_owner,
                               project_url,
                               clone_url,
                               commits_url,
                               git_url,
                               api_url,
                               stargazers_count,
                               forks_count,
                               watchers_count,
                               project_size,
                               last_update,
                               is_public,
                               default_branch,
                               data_de_atualizacao
                               )
                    VALUES    (nextval('projects_id_projects_seq'),
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                                );'''
        try:
            a_cur.execute(SQL_INSERT, (id_raw_projects_data,
                                       project.get_git_project_cod(),
                                       project.get_project_name(),
                                       project.get_description(),
                                       project.get_project_lang(),
                                       project.get_create_data(),
                                       project.get_project_owner(),
                                       project.get_project_url(),
                                       project.get_clone_url(),
                                       project.get_commits_url(),
                                       project.get_git_url(),
                                       project.get_api_url(),
                                       project.get_stargazers(),
                                       project.get_forks(),
                                       project.get_watchers(),
                                       project.get_project_size(),
                                       project.get_last_update(),
                                       project.is_public(),
                                       project.get_default_branche(),
                                       datetime.now()                                       
                                       ))
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao inserir na tabela project: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))     
            
        
        
    
    def persite_project(self, a_project):
        
        try:
            self.__conn_manager.connect_db()
            
            cur = self.__conn_manager.get_cursor()
            
            id_raw_project_data = self.__insert_raw_project_data(cur, a_project.get_project_json_data())
            
            self.__insert_projects(cur, id_raw_project_data, a_project)
            
            self.__conn_manager.commit_transation()       
            
        except GitScrapeError as e:
            raise e
            
        
        
        
        
        
            
        
