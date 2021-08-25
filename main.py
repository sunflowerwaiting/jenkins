import ComTagInsert
from openpyxl import load_workbook

linux = ['pcie']
sdk = ['libva']
AI_Compiler = ['runtime']
firmware = ['AIDSP', 'SMCU', 'LMCU', 'CMCU', 'VDMCU', 'VDSP', 'VEMCU']
tools = ['demo', 'profiler', 'common', 'smi', 'logger', 'debugger']
all_Projects = {
    'firmware': firmware,
    'linux': linux,
    'sdk': sdk,
    'ai-compiler-group': AI_Compiler,
    'tools': tools,
}

work_path = 'D:\\GIT\\software\\'
work_path2 = 'D:\\GIT\\'
'''
work_path = '/home/tag/workspace/'
work_path2 = '/home/tag/'
'''
work_exname = 'SW_version_release.xlsx'
output_xls_path = work_path2 + work_exname

if __name__ == "__main__":
    log_list = ComTagInsert.get_commit('D:\\GIT\\jenkins', "repo_name")
    #   step 1 clone repo
    ComTagInsert.clone_gitlib(all_Projects, work_path)
    # ComTagInsert.fetch_gitlib(all_Projects, work_path)
    #   step 2 new work excel
    ComTagInsert.init_excel(all_Projects, output_xls_path)
    #   step 3 get commit
    wb = load_workbook(output_xls_path)
    for category_name in all_Projects:
        repo_names = all_Projects[category_name]
        for repo_name in repo_names:
            repo_path = work_path + repo_name
            log_list = ComTagInsert.get_commit(repo_path, repo_name)
            #   steps 4 insert commit into excel
            #print(log_list)
            # ComTagInsert.add_commit_log(log_list, wb, category_name)
    wb.save(output_xls_path)
