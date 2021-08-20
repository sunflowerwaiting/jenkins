from git import Repo
import git
import re
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Font, colors, Alignment, NamedStyle, Border, Side, Color
from openpyxl.styles import Font  # 导入字体模块

from openpyxl.styles import PatternFill

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
def pull_gitlib(ls, path):
    for val in ls:
        val1 = ls[val]
        for sheet in val1:
            git_path = 'git@192.168.16.6:' + val + '/' + sheet + '.git'
            git.Git(path).clone(git_path)
            print('pull  ' + val + '\\' + sheet + '  pass')


############### new a excel #####################
def init_excel(project, output_filepath):
    wb = Workbook()
    # ws = wb.active
    '''
    #this is to create  by every store
    for key in project:
        repoName = project[key]
        for sheetName in repoName:
            wb.create_sheet(sheetName)
            ws1 = wb[sheetName]
            #insert sheet title
            title = ['a','Version Num', 'Commit NUM', 'release date', 'release note (bug fix,new feature)']
            ws1.append(title)
           
            tab = Table(displayName="Table1", ref="A1:E5")

            # Add a default style with striped rows and banded columns
            style = TableStyleInfo(name='TableStyleMedium5', showFirstColumn=True,
                                   showLastColumn=True, showRowStripes=False, showColumnStripes=True)
            tab.tableStyleInfo = style
            ws1.add_table(tab)
            
            wb.save('D:\\GIT\\software\\SW_version_release.xlsx')
'''
    #   this is to create by future
    for sheetName in project:
        wb.create_sheet(sheetName)
        title = ['Function', 'Version Num', 'Commit NUM', 'release date', 'release note (bug fix,new feature)']
        ws1 = wb[sheetName]
        ws1.append(title)

    del wb['Sheet']
    '''
    tab = Table(displayName="Table1", ref="A1:E1000")

    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(name='TableStyleMedium5', showFirstColumn=True,
                           showLastColumn=True, showRowStripes=False, showColumnStripes=True)
    tab.tableStyleInfo = style
    ws.add_table(tab)
    '''
    # wb.save('D:\\GIT\\software\\SW_version_release.xlsx')
    wb.save(output_filepath)


############## get commit message #############
def get_commit(path, repoName):
    repo = Repo(path)

    # git log --tags --simplify-by-decoration --pretty=format:%D%n%h%n%cd%n%s%n
    commit_log = repo.git.log('--tags',
                              '--simplify-by-decoration',
                              '--pretty=format:%D%n%h%n%cd%n%s%n',
                              date='format:%Y-%m-%d %H:%M')

    log_list = commit_log.split('\n\n')
    real_log_list = []
    for log in log_list:
        log1 = log.split('\n')
        log1[0] = get_tag(log1[0])
        if log1[0]:
            log1.insert(0, repoName)
            real_log_list.append(log1)
    return real_log_list


regx = re.compile(".*tag:\\s*([\\w\\.-]+)\\b.*")


# ############# use re to  match tag ##############
def get_tag(describe):
    tags = []
    m = regx.search(describe)
    while m:
        tags.append(m.group(1))
        m = regx.search(describe, m.end(1))
    return ", ".join(tags) if len(tags) else None
    # print(describe, m.group(1))


############### insert commit to excel #############
def add_commit_log(commits, wb, val):
    ws1 = wb[val]
    # high of row 1
    ws1.row_dimensions[1].height = 20
    ws1.font = 'Times New Roma'
    ws1.column_dimensions['B'].width = 16
    ws1.column_dimensions['D'].width = 17.89
    ws1.column_dimensions['E'].width = 104

    for commit in commits:
        '''
        new_commit = []
        for key in commit:
            new_commit.append(key[value])
        '''

        ws1.append(commit)


def GetExcelInfo(exname):
    wb = load_workbook(exname)
    ws1 = wb.sheetnames
