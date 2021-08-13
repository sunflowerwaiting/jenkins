from git import Repo
import json

################ get git commit ###################

def get_commit(path):
    repo = Repo(path)
    commit_log = repo.git.log('--pretty={"Author":"%an","Commit Num":"%h","release date":"%cd","release note":"%s"}', max_count=50,
                              date='format:%Y-%m-%d %H:%M')

    log_list = commit_log.split("\n")
    real_log_list = [eval(item) for item in log_list]
    return real_log_list