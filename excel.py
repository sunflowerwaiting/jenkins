import git
from openpyxl import Workbook,load_workbook
import os
from git import Repo

firmware = ['AIDSP','SMCU','LMCU','CMCU','VDMCU','VDSP','VEMCU']
tools = ['demo','profiler','common','smi','logger','debugger']
linux = ['pcie']
sdk = ['libva']
AI_Compiler = ['runtime']

all_Projects = {
    'linux':linux,
    'sdk':sdk,
    'ai-compiler-group':AI_Compiler,
    'tools':tools,
    'firmware':firmware,

}
work_path = 'D:\GIT\software\\'
work_exname = 'SW_version_release.xlsx'


def buildExcell(project,path,exname):
    wb = Workbook()
    path1 = path + exname
    for val in project:
        val1 = project[val]
        for sheet in val1:
            wb.create_sheet(sheet)
            #wb.save('path1')
    #wb.remove('sheet')

    print(path1)
    wb.save('path1')

buildExcell(all_Projects,work_path,work_exname)
