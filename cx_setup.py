from cx_Freeze import setup, Executable
import os,sys
 
# Dependencies are automatically detected, but it might need
# setup file for cx_freeze to build Windows Executable
# create executable using command `python cx_setup.py build`
script_dir  = os.path.dirname(os.path.realpath(__file__))

is_bundle = getattr(sys, 'frozen', False)
is_local = not is_bundle and os.path.exists(os.path.join(script_dir, "setup-release.py"))
is_android = 'ANDROID_DATA' in os.environ

if is_bundle or is_local or is_android:
    import imp
    imp.load_module('electrum_xvg', *imp.find_module('lib'))

from electrum_xvg.version import ELECTRUM_VERSION
buildOptions = dict(packages = ["idna","shutil","ltc_scrypt","argparse","dns","gui","dbhash","dumbdbm"], excludes = [], include_files=["lib"])
 
base = 'Win32GUI' if sys.platform=='win32' else None
 
executables = [
    Executable('electrum-xvg', base=base, icon = "./icons/electrum.ico")
]
 
setup(
    name='Electrum XVG',
    version=ELECTRUM_VERSION,
    description = 'Electrum Wallet for Verge (XVG)',
    options = dict(build_exe = buildOptions),
    executables = executables,    
)
