# Video 26 — Python Tutorial: Automate Parsing and Renaming of Multiple Files

## Status
✅ Completed

## What I Learned
- Learned how to automate renaming of multiple files using Python.
- Learned how to parse filenames into separate parts using string methods.
- Learned the value of building a script incrementally, step by step.
- Learned how to pad numbers with zeros for correct sorting order.

## What I Practiced
- Changed directory and listed files using `os.chdir()` and `os.listdir()`.
- Split filename and extension using `os.path.splitext()`.
- Split filename parts using `str.split('-')`.
- Cleaned up whitespace using `.strip()`.
- Removed unwanted characters using slicing (`[1:]`).
- Padded numbers using `.zfill()`.
- Formatted new filenames using `str.format()`.
- Renamed files using `os.rename()`.

## Main Concepts

### Problem
Filenames started with titles instead of numbers, causing incorrect sort order. Manually renaming hundreds of files would be too time-consuming — automate it instead.

### Script-Building Approach
Build solutions step by step:
1. Change directory and confirm current path.
2. Loop through files and print to confirm detection.
3. Gradually parse and transform filenames, testing each step before moving to the next.
4. Only rename files once the new filename format is confirmed correct.

## Important Commands / Examples

### File Listing
- `os.chdir(path)` → Change to target directory.
- `os.getcwd()` → Confirm current directory.
- `os.listdir()` → List all files in current directory.

### Parsing Filenames
- `os.path.splitext(f)` → Splits into `(name, extension)`.
- `f_name.split('-')` → Splits name into parts by delimiter.
 - Assumes a fixed number of hyphens; use `split('-', maxsplit=n)` for messier names.
- `.strip()` → Removes leading/trailing whitespace.
- `f_num[1:]` → Slices off unwanted leading character (e.g. `#`).
- `.zfill(2)` → Pads number with zeros (e.g. `4` → `04`) for correct sort order.

### Renaming
- `'{}-{}{}'.format(num, title, ext)` → Builds new filename string.
- `os.rename(old_name, new_name)` → Renames the file.

## Practical Example
```python
import os

os.chdir("path/to/files")

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = f'{f_num}-{f_title}{f_ext}'
    os.rename(f, new_name)
```
This loops through every file, extracts the number and title, zero-pads the number, and renames each file so they sort correctly.

## Verification
I followed the examples from the video and practiced automated file renaming.

- `print(os.getcwd)` (without parentheses) prints the function object, not the path — must call it as `os.getcwd()`.
- `.split('-')` will raise `ValueError: too many values to unpack` if a filename has more or fewer hyphens than expected.
- Zero-padding numbers (`.zfill()`) is essential — without it, `1` and `10` sort next to each other instead of `1` and `2`.

## Notes
- `os.chdir()` → Change directory.
- `os.listdir()` → List files.
- `os.path.splitext()` → Split name and extension.
- `str.split()` → Split string by delimiter.
- `str.strip()` → Remove extra whitespace.
- `str.zfill()` → Zero-pad a number string.
- `str.format()` → Build formatted string.
- `os.rename()` → Rename a file.

## Key Takeaway
Combining `os` and string methods lets Python automate tedious, repetitive file-renaming tasks — building the script incrementally (test each step before the next) keeps the process safe and error-free.
