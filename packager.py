import os
import zipfile
import argparse

def zip_project(output_filename):
  with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in ['LICENSE', 'README.md']:
      if os.path.isfile(file):
        zipf.write(file)
    for root, dirs, files in os.walk('src'):
      for file in files:
        file_path = os.path.join(root, file)
        zipf.write(file_path, os.path.relpath(file_path, 'src'))

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = "Create a zip archive of the project")
  parser.add_argument('--output', default = "§eSlim§0 §eFire§0.zip", help = "Output zip file name")
  args = parser.parse_args()
  zip_project(args.output)
