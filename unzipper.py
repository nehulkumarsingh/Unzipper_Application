
import sys
import zipfile
import os
import subprocess


status, output = subprocess.getstatusoutput('clear')
if status != 0:
    os.system('cls')
    
print("\n\n\n"*3)

if len(sys.argv) >= 2:
    if len(sys.argv) == 3:
        outpath = sys.argv[2]
        if not os.path.isdir(outpath):
            outpath = ''
    else:
        outpath = ''
    path = sys.argv[1]
    if os.path.isfile(path):
        zfile = zipfile.ZipFile(path)
        zfile.extractall(outpath)
        print(f"\n\nFiles Extracted Successfully at {outpath}")
        print("Thanks for using our program")
        sys.exit(0)
    else:
        print("!!Error!!Invalid File Path!!!Please check your path carefully")
        sys.exit(2)
else:
    print("!!Error!! Please Provide File Path")
    print("!!Usage: unzipper.py zip_file_path output_folder_path")
    sys.exit(2)
        
