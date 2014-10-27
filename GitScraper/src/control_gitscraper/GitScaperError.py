#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 26/10/2014

@author: Vagner
'''

import logging

class GitScrapeError(Exception):
    '''
    Classe para gerenciar a exibição de erro para o usuário
    Atributos:
       mensagem: a mensagem a se exibida ao usuário 
    '''


    def __init__(self, mensagem):
        self.__mensagem = mensagem
        logging.error("ERROR: {0}".format(self.__mensagem))
        
    def show_error(self):
        print(self.__mensagem)
        