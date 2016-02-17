# -*- mode: python -*-
a = Analysis(['electrum-doged'])

##### include folder in distribution #######
def extra_data(folder):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % folder, files)
    extra_data = []
    for f in files:
        extra_data.append((f, f, 'DATA'))

    return extra_data
###########################################

# Theme data
a.datas += extra_data('data')

# Localization
#a.datas += extra_data('locale')

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='electrum-doged.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='icons\\electrum.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='electrum-doged')
