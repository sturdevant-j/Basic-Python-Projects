import os


def start():
    directoryPath = "/Users/rene/Projects/basic_python_projects/drill_1"
    for file in os.listdir(directoryPath):
        if file.endswith('txt'):
            filePath = os.path.join(directoryPath,file)
            lastModified = os.path.getmtime(filePath)
            print(file,lastModified)





if __name__ == "__main__":
    start()
