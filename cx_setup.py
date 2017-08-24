from cx_Freeze import setup, Executable
 
# Dependencies are automatically detected, but it might need
# setup file for cx_freeze to build Windows Executable
# create executable using command `python cx_setup.py build`


buildOptions = dict(packages = ["idna","shutil","ltc_scrypt","argparse","dns","gui"], excludes = [], include_files=["lib"])
 
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
 
executables = [
    Executable('electrum-xvg', base=base, icon = "./icons/electrum.ico")
]
 
setup(
    name='Electrum XVG',
    version="2.4",
    description = 'Electrum Wallet for Verge (XVG)',
    options = dict(build_exe = buildOptions),
    executables = executables,    
)
