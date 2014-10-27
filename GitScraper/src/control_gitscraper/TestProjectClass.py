#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 26/10/2014

@author: vagner
'''

import json
import psycopg2
from control_gitscraper.Project import Project
from control_gitscraper.GitScaperError import GitScrapeError
from datetime import datetime


if __name__ == '__main__':

    SQL_QUERY = '''SELECT rpd.id_raw_projects_data
                   ,      rpd.json_data
                   FROM   public.raw_projects_data  rpd;
                 '''
    
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
                               private,
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
    
    project_list = []
    
    conn = psycopg2.connect("dbname=mes user=mes password=mes2014")
    
    cur = conn.cursor()
    cur_2 = conn.cursor()
    
    cur.execute(SQL_QUERY)
    
    for a_record in cur:
        id_raw_projects_data = a_record[0]
        json_data = json.loads(a_record[1])
        try:
            print id_raw_projects_data
            project = Project(json_data)            
            project_list.append(project)
            cur_2.execute(SQL_INSERT, (id_raw_projects_data,
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
        except GitScrapeError as gse:
            cur.close()
            cur_2.rollback()
            cur_2.close()
            conn.rollback()
            exit(3)
    print ('Total de Projetos: %d' % len(project_list))        
    for p in project_list:
        print p.get_project_name()        
            
    cur.close()
    cur_2.close()
    conn.commit()
    conn.close()
    print ('Everything is gonna be alright!')