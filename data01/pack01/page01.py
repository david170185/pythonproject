# import pack02.mysqldb
from pack02 import mysqldb

print('welcome')
# 실행 : ctrl+shift+f10

mysqldb.create()
mysqldb.read()
mysqldb.update()
mysqldb.delete()

from tkinter import *
window = Tk()
window.mainloop()