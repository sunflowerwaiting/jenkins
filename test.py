import os
import shutil
from git import Repo, repo
work_path = 'D:\\GIT\\jenkins\\'
#work_path = '/home/tag/workspace/'



def pull_gitlib(filepath):

    dirfile = os.path.abspath(filepath)
    repo = Repo(dirfile)
    g = repo.git
    g.push()

pull_gitlib(work_path)