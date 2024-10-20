import os
import sys
import site

def find_mediapipe_path():
    # Get the site-packages directory
    site_packages = site.getsitepackages()
    
    # Look for the MediaPipe package in the site-packages directories
    for path in site_packages:
        mediapipe_dir = os.path.join(path, 'mediapipe')
        if os.path.isdir(mediapipe_dir):
            return mediapipe_dir
    return None

def generate_spec_file(mediapipe_path):
    # Prepare the data files to include
    data_files = []
    
    # Hand landmark files
    hand_landmark_dir = os.path.join(mediapipe_path, "modules", "hand_landmark")
    data_files.append((hand_landmark_dir, "mediapipe/modules/hand_landmark"))
    
    # Palm detection model file
    palm_detection_file = os.path.join(mediapipe_path, "modules", "palm_detection", "palm_detection_full.tflite")
    data_files.append((palm_detection_file, "mediapipe/modules/palm_detection"))

    # Random Forest model file (add your model path here)
    model_file = os.path.join(os.getcwd(), "rfmodel01234.joblib")  # Adjust the path as necessary
    data_files.append((model_file, "rfmodel01234.joblib"))

    # Create the spec file content
    spec_content = f"""# -*- mode: python -*-
block_cipher = None

a = Analysis(
    ['implementModel.py'],
    pathex=[],
    binaries=[],
    datas={data_files},
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
"""

    # Write the spec file
    with open("implementModel.spec", "w") as spec_file:
        spec_file.write(spec_content)
    
    print("Spec file created successfully!")

def main():
    mediapipe_path = find_mediapipe_path()
    if mediapipe_path:
        print(f"Found MediaPipe at: {mediapipe_path}")
        generate_spec_file(mediapipe_path)
    else:
        print("MediaPipe package not found. Please ensure it is installed.")

if __name__ == "__main__":
    main()
