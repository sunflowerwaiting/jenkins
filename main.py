import Get_commit
import InsertExcl


arg1 = Get_commit.get_commit('D:\GIT\jenkins')
InsertExcl.insertExcel(arg1,'jenkins')

arg2=Get_commit.get_commit('D:\GIT\PythonLearn')
InsertExcl.insertExcel(arg2,'PythonLearn')