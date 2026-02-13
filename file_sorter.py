import os, shutil, sys

PATH = ''

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

def get_unique_name(filename: str, dest_path: str) -> str:
    """
    Get unique names for duplicate files adding (number)

    Args:
        filename: Duplicated file's name
        dest_path: Destination path for duplicated files
    
    Returns:
        A unique new name for the file
    """
    name, ext = os.path.splitext(filename)
    i: int = 1
    new_name: str = filename
    
    while os.path.exists(os.path.join(dest_path, new_name)):
        new_name = f'{name}({i}){ext}'
        i += 1
    
    return new_name 

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
        os.makedirs(os.path.join(path, category), exist_ok = True) # exist_ok = True does not raise exception for already existing directories

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
        new_name: str = name
        if os.path.exists(os.path.join(path, category, name)):
            new_name = get_unique_name(name, os.path.join(path, category))

        print(f'\tMoved {new_name} to {category}')
        shutil.move(os.path.join(path, name), os.path.join(path, category, new_name))

def main(path: str = PATH):
    try:
        validate_path(path)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        sys.exit(str(e))


    print(f'Organizing files in {path}...')
    files = read_files_list(path)

    print('Creating folders...')
    create_folders(files, path, CONFIG)

    move_files(files, path, CONFIG)

    print(f'Done! Organized {len(files)} files.')


def validate_path(path: str) -> None:
    """
    Validate that path exists, is a directory, and has read/write permissions
    
    Args:
        path: Path to validate
        
    Raises:
        FileNotFoundError: If path doesn't exist
        NotADirectoryError: If path is not a directory
        PermissionError: If missing read or write permissions
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f'Path does not exist: {path}')
    
    if not os.path.isdir(path):
        raise NotADirectoryError(f'Path is not a directory: {path}')
    
    if not os.access(path, os.R_OK):
        raise PermissionError(f'No read permission for: {path}')
    
    if not os.access(path, os.W_OK):
        raise PermissionError(f'No write permission for: {path}')


if __name__ == '__main__':
    main()