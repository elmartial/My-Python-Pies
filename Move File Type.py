#if you want to find & move different type of files then:
#rename def move_(file type)_files & f.endswith('file type')
import os
import shutil

def move_mid_files(src, dst):
    os.makedirs(dst, exist_ok=True)
    for root, _, files in os.walk(src):
        [shutil.move(os.path.join(root, f), dst) for f in files if f.endswith('.mid')]

# Example usage
move_mid_files(r"path_to_source_folder", r"path_to_destination_folder")
