from git import Repo
import git
import re
from openpyxl import Workbook,load_workbook
import os

'''
import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
logging.debug('debug 信息')
logging.info('info 信息')
logging.warning('warning 信息')
logging.error('error 信息')
logging.critical('critial 信息')
'''
############## clone repository #############
def pull_gitlib(list,path):
    for val in list:
        val1 = list[val]
        for sheet in val1:
            git_path = 'git@192.168.16.6:'+val+'/'+sheet+'.git'
            git.Git(path).clone(git_path)
            print('pull  '+ val + '\\' + sheet +'  pass')

############### new a excel #####################
def buildExcell(project,path,exname):
    wb = Workbook()
    for key in project:
        repoName = project[key]
        for sheetName in repoName:
            wb.create_sheet(sheetName)
    #wb.remove('sheet')
            #path1 = path + exname
            wb.save('D:\\GIT\\software\\SW_version_release.xlsx')

############## get commit message #############
def get_commit(path,sheet):
    repo = Repo(path)

    '''
    ####################used json to format log massage#####################    
    commit_log = repo.git.log('--pretty={"author":"%an","Commit Num":"%h","release date":"%cd","release note": "%s" }',
                              max_count=50, date='format:%Y-%m-%d %H:%M')
    log_list = commit_log.split("\n")
    print(type(log_list))
    real_log_list = [eval(item) for item in log_list]
    
    '''

    # git log --simplify-by-decoration --pretty=format:%D%n%h%n%cd%n%s%n
    commit_log = repo.git.log('--simplify-by-decoration',
                              '--pretty=format:%D%n%h%n%cd%n%s%n',
                              date='format:%Y-%m-%d %H:%M')

    log_list = commit_log.split('\n\n')
    real_log_list = []
    for log in log_list:
        log1 = log.split('\n')
        log1[0] = get_tag(log1[0])
        real_log_list.append(log1)
    return real_log_list


regx = re.compile(".*tag:\\s+([\\w\\.]+).*")


# ############# use re to  match tag ##############
def get_tag(describe):
    tags = []
    m = regx.search(describe)
    while m:
        tags.append(m.group(1))
        m = regx.search(describe, m.end(1))
    return ", ".join(tags) if len(tags) else describe
    # print(describe, m.group(1))
    # return m.group(1) if m else describe



############### insert commit to excel #############
def add_commit_log(args, store, exname):
    wb = load_workbook(exname)
    ws1 = wb[store]
    for commit in args:
        '''
        new_commit = []
        for key in commit:
            new_commit.append(key[value])
        '''
        ws1.append(commit)
    # wb.save('D:\\GIT\\software\\SW_version_release.xlsx')
    wb.save(exname)


def GetExcelInfo(exname):
    wb = load_workbook(exname)
    ws1 = wb.sheetnames
