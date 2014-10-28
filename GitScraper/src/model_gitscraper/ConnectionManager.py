#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 27/10/2014

@author: vagner
'''
import psycopg2
from control_gitscraper.GitScaperError import GitScrapeError

class ConnectionManager(object):
    '''
    Classe que gerencia a conexão com o banco de dado
    '''


    def __init__(self, dbname = None, user = None, password= None):
        '''
        Constructor
        '''
        self.__dbname = dbname
        self.__user   = user
        self.__password = password
        self.__dbconn = None
        try:
            self.__dbconn = psycopg2.connect(database = self.__dbname, user=self.__user, password=self.__password)
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao conectar o banco de dados: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        
    def connect_db(self):
        
        if self.__dbconn == None:
            try:
                self.__dbconn = psycopg2.connect(database = self.__dbname, user=self.__user, password=self.__password)
                
            except psycopg2.Error as e:
                raise GitScrapeError("Erro ao conectar o banco de dados: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        
        
        
    
    def close_connection(self):
        try:
            self.__dbconn.close()
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao fechar a conexão com o banco de dados: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        
    def commit_transation(self):
        try:
            self.__dbconn.commit()
            
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao realizar o commit da transição: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        
    def rollback_transation(self):
        try:
            self.__dbconn.rollback()
             
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao realizar o rollback da transição: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror)) 
        
    def get_cursor(self):
        try:
            return_cursor = self.__dbconn.cursor()
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao obter um cursor do banco: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        return return_cursor
    
    def close_cursor(self, a_cursor):
        try:
            a_cursor.close()
        except psycopg2.Error as e:
            raise GitScrapeError("Erro ao fechar um cursor do banco: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))   
            
                  
            