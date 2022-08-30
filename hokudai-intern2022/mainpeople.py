import glob
import shutil

files = glob.glob("./newanalyse/*")
for file in files:
    print(file)
    print(sum([1 for _ in open(file)]))

    if  sum([1 for _ in open(file)]) >= 20:
        new_path = shutil.move(file, './mainpeople_newanalyse/')

        print(new_path)
        # temp/dir2/file.txt
