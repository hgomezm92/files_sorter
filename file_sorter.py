import os, shutil

PATH = '/home/aituk/Documentos/Prueba'

CONFIG: dict[str, list[str]] = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
}

def read_files_list(path: str) -> dict[str, str]:
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

def get_category(extension: str, config: dict[str, list[str]] = CONFIG) -> str:
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

def create_folders(files: dict[str, str], path: str, config: dict[str, list[str]] = CONFIG) -> None:
    """
    Create needed directories to sort files taking an extension list from a
    dictionary

    Args:
        files: A dictionary with names as keys and extensions with dot as values
        path: Path where directories will be created
        config: A dictionary with categories and extensions that belong to it
    """
    extensions: set[str] = set(files.values())
    
    categories: set[str] = {get_category(extension, config) for extension in extensions} # set comprehension
    
    for category in categories:
        os.makedirs(os.path.join(path, category), exist_ok=True)

def move_files(files: dict[str, str], path: str, config: dict[str, list[str]] = CONFIG) -> None:
    """
    Move files to directories by extension

    Args:
        files: A dictionary with names as keys and extensions with dot as values
        path: Original path of files
        config: A dictionary with categories and extensions that belong to it
    """
    print('Moving files...')

    for name, ext in files.items():
        category: str = get_category(ext, config)
        if os.path.exists(os.path.join(path, category, name)):
            print(f'\tSkipped {name} - already exists in {category}')
            continue
        print(f'\tMoved {name} to {category}')
        shutil.move(os.path.join(path, name), os.path.join(path, category, name))

def main(path: str = PATH):
    print(f'Organizing files in {path}...')
    files = read_files_list(PATH)

    print('Creating folders...')
    create_folders(files, PATH, CONFIG)

    move_files(files, PATH, CONFIG)

    print(f'Done! Organized {len(files)} files.')

if __name__ == '__main__':
    main()