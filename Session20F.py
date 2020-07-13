import os

print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getppid()) # Process Id in which this program is getting executed

print("Current Working Directory:", os.getcwd())

path_to_directory = "/Users/ishantkumar/Downloads"
path_to_file = "/Users/ishantkumar/Downloads/key.json"

print("Downloads Directory Exists?", os.path.isdir(path_to_directory))
print("key.json File Exists?", os.path.isfile(path_to_file))

files = os.walk(path_to_directory)
all_files = list(files)

for file in all_files:
    print(file)

# explore -> mkdir (make a directory) and rmdir (remove directory) | PS: use rmdir very carefully


# Assignment: Using os.walk, walk in some directory and pull below information
#                            show Documents and count of documents (.pdf, .doc, .docx, .txt)
#                            show images and count of images (.jpg, .png, .jpeg)
#                            show audio/video and count of audio/video (.mp3, .mp4 etc..)