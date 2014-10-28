#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 18/10/2014

@author: Vagner Clementino
'''
from control_gitscraper.GitScraper import GitScraper
import json
from control_gitscraper.Project import Project
from control_gitscraper.GitScaperError import GitScrapeError
from model_gitscraper.ProjectModel import ProjectModel

if __name__ == '__main__':
    
    try:
        scraper = GitScraper()
            
        json_data_list = scraper.run_query(language='java', sort='forks', order='desc')
    
        print 'Total de projetos recuperados: {0}'.format(len(json_data_list))
        
        project = Project(json.loads(json_data_list[0]))
        
        projectModel = ProjectModel()
        
        projectModel.persite_project(project)
        
        print(project.get_project_name())
        
    except GitScrapeError as e:
        e.show_error()    
    
    print('Everythig ins gonna be alright!')
    

    
