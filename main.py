import ComTagInsert
from openpyxl import load_workbook


linux = ['pcie']
sdk = ['libva']
AI_Compiler = ['runtime']
firmware = ['AIDSP','SMCU','LMCU','CMCU','VDMCU','VDSP','VEMCU']
tools = ['demo','profiler','common','smi','logger','debugger']
all_Projects = {
    'linux':linux,
    'sdk':sdk,
    'ai-compiler-group':AI_Compiler,
    'tools':tools,
    'firmware':firmware,
}

work_path = 'D:\\GIT\\software\\'
work_exname = 'SW_version_release.xlsx'

if __name__ == "__main__":
    '''
    wb = load_workbook(r"d:\SW_version_release.xlsx")
    wb1 = wb.sheetnames
    print(wb1)
    '''
    #step 1 git fatch
    #ComTagInsert.pull_gitlib(all_Projects,work_path)

    #step 2 new work excel
    ComTagInsert.buildExcell(all_Projects,work_path,work_exname)

    #step 3 get commit
    for val in all_Projects:
        val1 = all_Projects[val]
        for repoName in val1:
            path = work_path + repoName
            log_list = ComTagInsert.get_commit(path, repoName)
            # steps 4 insert commit into excel
            print(repoName, work_exname)
            store = work_path + work_exname
            ComTagInsert.add_commit_log(log_list, repoName, store)




