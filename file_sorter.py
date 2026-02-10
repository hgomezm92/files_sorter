import os

PATH = "/home/aituk/Documentos/Prueba"

config = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}

def read_files_list(path):
    files = os.listdir(path)
    names = {}

    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            name = os.path.splitext(file)
            names[file] = name[1]

    return names

def get_file_category(extension):
    for category, extensions in config.items():
        if extension.lower() in extensions:
            return category

    return "Others"