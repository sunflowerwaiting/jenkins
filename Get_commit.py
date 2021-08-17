from git import Repo
import json

################ get git commit ###################

def get_commit(path):
    repo = Repo(path)
    '''
    ####################used json to format log massage#####################
    
    commit_log = repo.git.log('--pretty={"author":"%an","Commit Num":"%h","release date":"%cd","release note": "%s" }', max_count=50, date='format:%Y-%m-%d %H:%M')
     print(1)
    log_list = commit_log.split("\n")
    print(type(log_list))
    real_log_list = [eval(item) for item in log_list]
    '''
    #####not use json ######################

    commit_log = repo.git.log('--pretty=%an%n%h%n%cd%n%s%n', max_count=50,date = 'format:%Y-%m-%d %H:%M')
    log_list = commit_log.split('\n\n')
    real_log_list = []
    for log in log_list:

        log1 = log.split('\n')
        real_log_list.append(log1)

    print(real_log_list)
    return real_log_list