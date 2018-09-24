# -*- mode: python -*-

block_cipher = None


a = Analysis(['cpuprogress.py'],
             pathex=['C:\\Users\\gurubhat\\Desktop\\GB_Projects\\Easy-Mon'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='cpuprogress',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
