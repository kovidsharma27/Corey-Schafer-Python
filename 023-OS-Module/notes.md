# Video 23 — Python Tutorial: OS Module - Use Underlying Operating System Functionality

## Status
✅ Completed

## What I Learned
- Learned that the `os` module lets Python interact with the operating system.
- Learned how to navigate directories and work with files.
- Learned how to create, delete, rename, and inspect files/folders.
- Learned how to access environment variables.
- Learned how to work with file paths using `os.path`.
- Learned how to traverse directory trees using `os.walk()`.

## What I Practiced
- Used `os.getcwd()`, `os.chdir()`, and `os.listdir()`.
- Created and removed directories using `mkdir()`, `makedirs()`, `rmdir()`, and `removedirs()`.
- Deleted files using `os.remove()`.
- Renamed files/folders using `os.rename()`.
- Checked file information using `os.stat()`.
- Accessed file size and timestamps using `st_size`, `st_atime`, `st_mtime`, and `st_ctime`.
- Converted timestamps using `datetime.fromtimestamp()`.
- Used `os.walk()` to traverse directories and subdirectories.
- Accessed environment variables using `os.environ` and `os.environ.get()`.
- Practiced path operations using `os.path`.

## Main Concepts

### `os` Module
`os` is a built-in Python module used to interact with the operating system.

```python
import os
```

### Directories
- `os.getcwd()` → Current working directory.
- `os.chdir(path)` → Change directory.
- `os.listdir(path)` → List files and folders.

### Files & Folders
- `os.mkdir()` / `os.makedirs()` → Create directories.
- `os.rmdir()` / `os.removedirs()` → Remove directories.
- `os.remove()` → Remove a file.
- `os.rename()` → Rename files/folders.
- `os.stat()` → Get file information.

### Paths
`os.path` provides functions for safely working with file paths.

### Environment Variables
`os.environ` provides access to environment variables.

### `os.walk()`
Traverses a directory and its subdirectories, providing the current path, directories, and files.

## Important Commands / Examples

### Directory Operations
- `os.getcwd()` → Gets the current directory.
- `os.chdir(path)` → Changes the current directory.
- `os.listdir(path)` → Lists directory contents.
- `os.mkdir("folder")` → Creates one directory.
- `os.makedirs("outer/inner")` → Creates directories and subdirectories.
- `os.rmdir("folder")` → Removes a directory.
- `os.removedirs("outer/inner")` → Removes intermediate directories when possible.
- `os.remove("file.txt")` → Removes a single file.
- `os.rename("old.py", "new.py")` → Renames a file or folder.

### File Information
`os.stat("file.py")` → Returns file information.

- `st_size` → File size in bytes.
- `st_atime` → Last access time.
- `st_mtime` → Last modification time.
- `st_ctime` → Platform-dependent time information.

`datetime.fromtimestamp(timestamp)` → Converts a timestamp into readable date/time.

### `os.walk()`
`os.walk(path)` → Traverses a directory tree.

Provides:
- `dirpath` → Current directory.
- `dirnames` → Subdirectories.
- `filenames` → Files.

### Environment Variables
- `os.environ` → Access environment variables.
- `os.environ.get("VARIABLE_NAME")` → Get a specific variable.
- Windows commonly uses `USERPROFILE` for the user's home directory.

### Path Operations
- `os.path.join(path, "file.txt")` → Safely combines paths.
- `os.path.basename(path)` → Gets the filename.
- `os.path.dirname(path)` → Gets the directory.
- `os.path.split(path)` → Returns directory and filename.
- `os.path.exists(path)` → Checks whether a path exists.
- `os.path.isdir(path)` → Checks whether a path is a directory.
- `os.path.isfile(path)` → Checks whether a path is a file.
- `os.path.splitext(path)` → Splits the path and extension.

### Deleting Files vs Directories
- `os.remove(path)` → Deletes a **file**. Raises `FileNotFoundError` if it doesn't exist, or `IsADirectoryError` if used on a directory.
- `os.rmdir(path)` → Deletes a **single empty directory**. Raises `OSError` if the directory is not empty.
- `os.removedirs(path)` → Deletes a directory **and** its parent directories, but only as long as each one becomes empty after removal. Stops climbing upward as soon as it hits a non-empty parent.
- None of these can delete a non-empty directory along with its contents. For that, use `shutil.rmtree()` (from the `shutil` module, not `os`).

## Practical Example

```python
import os

path = os.getcwd()

print("Current Directory:", path)

print("Files:", os.listdir(path))

print("Exists:", os.path.exists(path))
```

This gets the current directory, lists its contents, and checks whether the path exists.

## Verification
I followed the examples from the video and practiced the `os` and `os.path` functions.

Some behavior can differ between operating systems:

- Windows commonly uses `USERPROFILE` for the user's home directory.
- `st_ctime` has platform-dependent meaning.
- Path separators differ between Windows and Unix-like systems.
- `os.path.join()` helps handle path separators correctly.
- `os.remove()` and `os.rmdir()` only work on files/directories that already exist and match their expected type.

## Notes
- `os` → Interact with the operating system.
- `os.getcwd()` → Get current directory.
- `os.chdir()` → Change directory.
- `os.listdir()` → List directory contents.
- `os.mkdir()` / `os.makedirs()` → Create directories.
- `os.rmdir()` / `os.removedirs()` → Remove directories.
- `os.remove()` → Remove a file.
- `os.rename()` → Rename files/folders.
- `os.stat()` → Get file information.
- `os.walk()` → Traverse directory trees.
- `os.environ` → Access environment variables.
- `os.path.join()` → Combine paths safely.
- `os.path.basename()` → Get filename.
- `os.path.dirname()` → Get directory.
- `os.path.split()` → Get directory + filename.
- `os.path.exists()` → Check if path exists.
- `os.path.isdir()` → Check for directory.
- `os.path.isfile()` → Check for file.
- `os.path.splitext()` → Separate path and extension.

## Key Takeaway
The `os` module gives Python access to operating-system functionality, especially for working with files, directories, paths, environment variables, and file information.
