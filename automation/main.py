import zipfile
import os
from pathlib import Path


def file_compress(inp_file_names, out_zip_file):

  # Select the compression mode ZIP_DEFLATED for compression
  # or zipfile.ZIP_STORED to just store the file
  compression = zipfile.ZIP_DEFLATED
  # create the zip file first parameter path/name, second mode
  zf = zipfile.ZipFile(out_zip_file, mode="w")

  try:
    for file_to_write in inp_file_names:
        # Add file to the zip file
        # first parameter file to zip, second filename in zip
      zf.write(file_to_write, file_to_write, compress_type=compression)

  except FileNotFoundError as e:
    print(f'Exception occurred during zip process - {e}')
  finally:
      # Don't forget to close the file!
    zf.close()
    print(f'Saved zip file to - {out_zip_file}')


print("""Hello! Pick any one task to automate:
  [1] Show Folder Structure
  [2] Compress current folder as zip
  [3] Rename files
""")
opt = int(input("Choose [1] - [3]: "))

if opt == 1:
  print("")
  folder = input("Enter your folder path (Enter . for current folder): ")
  path = str(Path(folder).resolve())
  print("Current Folder: ", path)
  print("")
  print("Folder Structure:")
  for dirpath, dirnames, filenames in os.walk(path):
    directory_level = dirpath.replace(path, "")
    directory_level = directory_level.count(os.sep)
    print(f"{'   ' * directory_level}{os.path.basename(dirpath)}/")

    for f in filenames:
      print(f"{'   ' * (directory_level + 1)}\u2514{f}")
elif opt == 2:
  _, _, filenames = next(os.walk(os.curdir))
  file_compress(filenames, "compressed.zip")
elif opt == 3:
  print("")
  print("Rename File")
  file = input("    Enter the path of the file to rename: ")
  name = input("    Enter the new name of the file: ")
  p = Path(file)
  n = Path(p.parent, f"{name}{p.suffix}")
  p.rename(n)
  print(f"Renamed {p} to {n}")
else:
  print("")
  print("Sorry, please try again later.")
