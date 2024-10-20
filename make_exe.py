import subprocess
import os
import shutil

def build_executable(spec_file, model_file):
    # Check if the spec file exists
    if not os.path.exists(spec_file):
        print(f"Spec file '{spec_file}' does not exist.")
        return

    try:
        # Run PyInstaller with the specified spec file
        subprocess.run(['pyinstaller', spec_file], check=True)
        print(f"Executable created successfully from '{spec_file}'.")

        # Move the model file to the executable directory
        dist_dir = 'dist/implementModel'  # Adjust this if your executable has a different name
        if os.path.exists(dist_dir):
            shutil.copy(model_file, dist_dir)
            print(f"Model file '{model_file}' copied to '{dist_dir}'.")
        else:
            print(f"Executable directory '{dist_dir}' does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the executable: {e}")

if __name__ == "__main__":
    spec_filename = 'implementModel.spec'  # Adjust this if your spec file has a different name
    model_filename = 'rfmodel01234.joblib'  # Adjust to your model filename
    build_executable(spec_filename, model_filename)
