import os
import shutil

# path = 'testdelete.txt'
# path = 'empty_folder'
path = 'full_folder'

try:
    # os.remove(path)   #only deletes files
    # os.rmdir(path)    #only deletes empty folders/directories
    shutil.rmtree(path)  # deletes folders/directories that contain files
except FileNotFoundError:
    print('We couldn\'t find the file.')
except PermissionError:
    print("You do not have permission to delete that.")
except OSError:
    print("You cannot delete a unempty folder using that function.")
else:
    print(path + " was deleted.")

