# Version 0.1 — early development

This is an early v0.1, still in development and a learning project. The
language and UX are intentionally informal — it's not polished yet. For
now the configuration is hardcoded: edit the `PATH` and `CONFIG` variables
directly in `file_sorter.py` to change behaviour.

This is a small Python utility that organizes files in a target
directory into categorized subfolders based on their file extensions. It uses only
the Python standard library and is intended as a simple, configurable
tool to keep downloads or project folders tidy.

**Status:** Minimal, single-file tool — in development (learning project).

**Contents**
- `file_sorter.py`: main script that scans a directory and moves files into
	categorized folders.
- `requirements.txt`: notes that no external dependencies are required.

**Features**
- Categorizes files by extension using a configurable `CONFIG` mapping.
- Creates missing category folders automatically.
- Skips files that already exist in the destination category.

**Requirements**
- Python 3.9+ (the project uses type hints like `dict[str, ...]`).
- No third-party packages.

Installation
------------
Clone the repository and (optionally) create a virtual environment:

```bash
git clone https://github.com/<your-username>/files_sorter.git
cd files_sorter
python -m venv .venv
source .venv/bin/activate
```

Usage
-----
Run the script directly. By default it sorts the path defined in the
`PATH` variable inside `file_sorter.py`. To sort a different directory,
call `main()` with a path or run the module after editing `PATH`.

```bash
python file_sorter.py
# or edit file_sorter.py to change PATH and then run
```

Configuration
-------------
Edit the `CONFIG` dictionary in `file_sorter.py` to change categories or
add/remove extensions. `get_category()` falls back to `Others` for unknown
extensions.

Notes
-----
- The script moves files (uses `shutil.move`). Back up important files if
	you're unsure.
- Filenames that already exist in the destination folder are skipped.

License
-------
See the `LICENSE` file in the repository.

Author
------
Created by the repository owner.