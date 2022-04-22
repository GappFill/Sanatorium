import os
import getpass
def createfolder ():
    try:
        USER_NAME = getpass.getuser()
        g=r"C:\Users\%s\desktop\Отчёты" % USER_NAME
        os.mkdir(g)
        return g
    except: return g