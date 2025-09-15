import os
from pathlib import Path

current_dir = os.getcwd()
print(current_dir)

# OR
current_dir2 = Path.cwd()
print(current_dir2)

os.mkdir("sample_folder1")     # gives error if exists
os.makedirs("sample_path/to/folder")   # gives error if exactly same exists
                                # makedirs creates intermediate folders
                                # if intermediet folder already exists - no error
# OR
Path("sample_folder2").mkdir() 
Path("sample_path/to/folder").mkdir(parents=True) # if parents is False, intermediate folders will not be created

