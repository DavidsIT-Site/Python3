import os
import shutil
py = 0
md = 0
c = 0
for root, dirs, files in os.walk("A:\\DF\\"):
    for file in files:
        if file.endswith(".py"):
             py += 1
             print("{} {} ".format(py, os.path.join(root, file)))
             print("{}         {} ".format(root, file))


             shutil.copy(os.path.join(root, file), "{}_py{}.txt".format( os.path.join(root, file), py))
        elif file.endswith(".md"):
            md += 1
            print("{} {} ".format(py, os.path.join(root, file)))
            print("{}         {} ".format(root, file))

            shutil.copy(os.path.join(root, file), "{}_md{}.txt".format(os.path.join(root, file), md))
        elif file.endswith(".c"):
            c += 1
            print("{} {} ".format(py, os.path.join(root, file)))
            print("{}         {} ".format(root, file))

            shutil.copy(os.path.join(root, file), "{}_md{}.txt".format(os.path.join(root, file), c))