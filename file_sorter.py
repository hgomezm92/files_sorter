import os

PATH = '/home/aituk/Documentos/Prueba'

config: dict[str, list[str]] = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
}

def read_files_list(path: str):
    """
    Read directory content and returns a dictionary with file names and 
    extensions skipping directories

    Args:
        path: Path to the directory to be sorted
    
    Returns:
        Dictionary with file names (file.xyz) as keys and extensions (.xyz) as
        values
    """
    filenames: list[str] = os.listdir(path)
    files: dict[str, str] = {}

    for filename in filenames:
        if os.path.isfile(os.path.join(path, filename)):
            _, ext = os.path.splitext(filename) # Unpack tuple (or list). _ for skipping the value
            files[filename] = ext

    return files

def get_category(extension: str, config: dict[str, list[str]]):
    """
    Get category name for a given extension (.xyz) from the config dictionary
    
    Args:
        extension: A string with the extension
        config: A dictionary with categories and extensions that belong to it
    
    Returns:
        A string with the extension's category
    """
    for category, extensions in config.items():
        if extension.lower() in extensions:
            return category

    return 'Others'

def create_folders(names: dict[str, str], path: str, config: dict[str, list[str]]):
    """
    Create needed directories to sort files taking an extension list from a
    dictionary

    Args:
        names: A dictionary with names as keys and extensions with dot as values
        path: Path where directories will be created
        config: A dictionary with categories and extensions that belong to it
    """
    extensions: set[str] = set(names.values())
    
    categories: set[str] = {get_category(extension, config) for extension in extensions} # set comprehension
    
    for category in categories:
        os.makedirs(os.path.join(path, category), exist_ok=True)