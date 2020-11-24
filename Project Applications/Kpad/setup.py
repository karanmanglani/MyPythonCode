import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python38-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python38-32\tcl\tk8.6'

executables = [cx_Freeze.Executable('main.py',base=base , icon='icon.ico')]

cx_Freeze.setup(
    name = 'Kpad Text Editor',
    options = {"build_exe":{"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll','Icons']}},
    version = "1.00",
    description = 'A great text editor developed by me',
    executables = executables
)