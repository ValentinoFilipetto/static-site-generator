import os
import shutil


# Recursively copies file and directories from
# source_dir to destination_dir.
def copy_files(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
        os.makedirs(destination_dir)
    else:
        os.makedirs(destination_dir)

    for item in os.listdir(source_dir):
        if os.path.isfile(source_dir + f"/{item}"):
            shutil.copy(source_dir + f"/{item}", destination_dir)
        else:
            copy_files(source_dir + f"/{item}", destination_dir + f"/{item}")
