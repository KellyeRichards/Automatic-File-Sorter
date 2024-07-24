import os, shutil

path = r"/Users/kellye/Documents/"

file_name = os.listdir(path)

folder_names = ['pdf files', 'img files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))

for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "img files/" + file):
        shutil.move(path + file, path + "img files/" + file)
    elif ".docx" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)

