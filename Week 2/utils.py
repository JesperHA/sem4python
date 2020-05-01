import os

path = "../dat4sem2020spring-python-master"

def filereader():

    filenames = open("filenames.txt", "a")

    entries = os.scandir("../dat4sem2020spring-python-master")
    for entry in entries:
        filenames.write(entry.name + "\n")
    print("Write to file succesful!")


    
def sub_file_reader():

    filenames2 = open("filenames2.txt", "w")

    for dir_name, subdir, files in os.walk(path):
        for name in files:

            filenames2.write(os.path.join(path, name) + "\n")
            #print(os.path.join(path, name))
        print("Write subdir names to file succesful!")

def filereader_reader():

    entries = os.scandir("../randomdir")
    for entry in entries:
        
        file = open("../randomdir/" + entry.name)
        print(file.readline())


    
def find_email():
    entries = os.scandir(r"..\randomdir")
    
    for entry in entries:
        
        file = open("../randomdir/" + entry.name)
        list_of_lines = file.readlines()

        for line in list_of_lines:

            if "@" in line:
                print(line)


def write_from_md():
    headlines = open("headlines.txt", "w")

    for dir_name, subdir, files in os.walk(path):
        for name in files:
            if name.endswith(".md"):
                filepath = path + "/" + name
                file = open(filepath)           
                list_of_lines = file.readlines()
                print("Printing headlines from file: ", filepath)
                for line in list_of_lines:

                    if line.startswith("#"):
                        headlines.write(line)





