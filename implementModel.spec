# -*- mode: python -*-
block_cipher = None

a = Analysis(
    ['implementModel.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\gauth\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\mediapipe\\modules\\hand_landmark', 'mediapipe/modules/hand_landmark'), ('C:\\Users\\gauth\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\mediapipe\\modules\\palm_detection\\palm_detection_full.tflite', 'mediapipe/modules/palm_detection'), ('C:\\Users\\gauth\\Downloads\\MV\\rfmodel01234.joblib', 'rfmodel01234.joblib')],
    hiddenimports=[
        'sklearn',
        'sklearn.ensemble',
        'sklearn.ensemble._forest',
        'sklearn.tree',
        'sklearn.base',
        'sklearn.utils',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='implementModel',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='implementModel')
