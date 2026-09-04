# Video 28 — Python Tutorial: CSV Module - How to Read, Parse and Write CSV Files

## Status
✅ Completed

## What I Learned
- Learned what CSV files are and how delimiters separate fields.
- Learned how to read and parse CSV files using the `csv` module.
- Learned how to write CSV files with custom delimiters.
- Learned how `DictReader`/`DictWriter` make working with fields easier than index-based access.
- Learned how to selectively write only specific fields to a new CSV file.

## What I Practiced
- Read CSV files using `csv.reader()`.
- Skipped the header row using `next()`.
- Wrote CSV files using `csv.writer()` with custom delimiters.
- Used `newline=''` to prevent extra blank lines when writing.
- Read/wrote CSV files using `csv.DictReader()` and `csv.DictWriter()`.
- Removed unwanted fields before writing using `del`.

## Main Concepts

### CSV Files
Plain text files storing data separated by a delimiter (usually a comma, but can be `-`, `\t`, etc.). Not meant for readability — meant for storing/transporting large amounts of structured data.

### `csv.reader()` vs `csv.DictReader()`
- `csv.reader()` → Returns each row as a **list**; access fields by index.
- `csv.DictReader()` → Returns each row as a **dictionary**; access fields by name (easier, especially for files with many fields).

### `newline=''` Gotcha
When writing CSV files, always pass `newline=''` to `open()`. Without it, Python's automatic newline translation (`\n` → `\r\n` on Windows) combines with `csv.writer`'s own line terminator, creating extra blank lines between rows.

## Important Commands / Examples

### Reading
- `csv.reader(csv_file)` → Returns rows as lists.
- `next(csv_reader)` → Advances the iterator by one row (commonly used to skip the header).
- `csv.reader(csv_file, delimiter='\t')` → Read a file using a custom delimiter.

### Writing
- `csv.writer(new_file, delimiter='-')` → Create a writer with a custom delimiter.
- `csv_writer.writerow(line)` → Write one row.
- `open('file.csv', 'w', newline='')` → Prevents extra blank lines when writing.

### Dictionary Reader/Writer
- `csv.DictReader(csv_file)` → Each row as `{field_name: value}`.
- `csv.DictWriter(new_file, fieldnames=[...], delimiter='\t')` → Create a dict-based writer.
- `csv_writer.writeheader()` → Writes the field names as the header row.
- `del line['field']` → Remove a field from a row dict before writing (when `fieldnames` excludes it).

## Practical Example
```python
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('names_only.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
```
This reads a CSV with names and emails, then writes a new CSV containing only the first and last names, dropping the email field.

## Verification
I followed the examples from the video and practiced reading, writing, and reformatting CSV files.

- Reading a `\t`-delimited file without specifying `delimiter='\t'` lumps all fields into one string — the delimiter must match on both read and write.
- `csv.writer` automatically quotes fields that contain the delimiter itself (e.g., `"Smith-Robinson"` when delimiter is `-`).
- `DictWriter.writerow()` raises an error if the row dict has extra keys not listed in `fieldnames` — remove them with `del` first.

## Notes
- `csv.reader()` → Read rows as lists.
- `csv.writer()` → Write rows from lists.
- `csv.DictReader()` → Read rows as dictionaries.
- `csv.DictWriter()` → Write rows from dictionaries.
- `next()` → Skip the header row.
- `newline=''` → Prevents extra blank lines when writing.
- `writeheader()` → Writes field names as the first row.

## Key Takeaway
The `csv` module makes it simple to read, parse, and write structured data files — `DictReader`/`DictWriter` are especially useful for readability and selectively working with named fields instead of numeric indexes.
