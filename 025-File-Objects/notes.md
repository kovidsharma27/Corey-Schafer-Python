# Video 25 — Python Tutorial: File Objects - Reading and Writing to Files

## Status
✅ Completed

## What I Learned
- Learned how to open, read, and write files using file objects.
- Learned the difference between `open()`/`close()` and context managers.
- Learned different ways to read file contents.
- Learned how to track and control file position using `tell()` and `seek()`.
- Learned how to write and append to files.
- Learned how to work with binary files like images.

## What I Practiced
- Opened files using `open()` and closed them manually with `.close()`.
- Used a context manager (`with`) to auto-close files.
- Read file contents using `.read()`, `.readlines()`, and `.readline()`.
- Iterated over a file line by line using a `for` loop.
- Read files in chunks using `.read(size)` combined with a `while` loop.
- Tracked file position using `.tell()` and moved position using `.seek()`.
- Wrote to files using `'w'` mode and appended using `'a'` mode.
- Copied a text file and an image file using read/write modes.

## Main Concepts

### File Modes
- `'r'` → Read (default).
- `'w'` → Write (overwrites existing content, creates file if not present).
- `'a'` → Append (writes at the end, creates file if not present).
- `'r+'` → Read and write.
- `'rb'` / `'wb'` → Binary read/write (used for non-text files like images).

### Context Manager
`with open(path, mode) as f:` automatically closes the file after the block ends — safer than manually calling `.close()`.

### File Position
- `.tell()` → Returns current cursor position (in bytes).
- `.seek(pos)` → Moves cursor to a specific position.

## Important Commands / Examples

### Opening Files
- `open('file.txt', 'r')` → Opens file object.
- `f.name` → File name.
- `f.mode` → Mode file was opened in.
- `f.close()` → Manually closes file.
- `f.closed` → Checks if file is closed (`True`/`False`).

### Reading
- `f.read()` → Reads entire file as a string.
- `f.readlines()` → Reads file as a list of lines.
- `f.readline()` → Reads one line at a time.
- `for line in f:` → Iterates file line by line (memory-efficient for large files).
- `f.read(n)` → Reads `n` characters/bytes at a time.

### Writing
- `f.write('text')` → Writes text to file.
- Multiple `.write()` calls append content sequentially within the same open block.

### Position Control
- `f.tell()` → Current position (bytes).
- `f.seek(0)` → Reset position to start of file.

### Binary Files
- Use `'rb'`/`'wb'` instead of `'r'`/`'w'` for non-text files (e.g., images) to avoid `UnicodeDecodeError`.

## Practical Example
```python
# Copy a text file using chunks
with open('source.txt', 'r') as rf:
    with open('copy.txt', 'w') as wf:
        chunk_size = 100
        chunk = rf.read(chunk_size)
        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(chunk_size)
```
This reads `source.txt` in fixed-size chunks and writes each chunk to `copy.txt`, avoiding loading the entire file into memory at once.

## Verification
I followed the examples from the video and practiced reading/writing text and binary files.

- Reading a closed file raises `ValueError: I/O operation on closed file.`
- Writing in `'r'` mode raises `io.UnsupportedOperation: not writable`.
- `'w'` mode overwrites existing files — use `'a'` mode to preserve existing content.
- Opening image files in text mode (`'r'`/`'w'`) causes `UnicodeDecodeError` — must use `'rb'`/`'wb'`.
- `f.tell()` returns byte position, which can differ from character count for multi-byte (non-ASCII) text.

## Notes
- `open()` → Opens a file object.
- `with open() as f:` → Context manager; auto-closes file.
- `f.read()` → Read entire file.
- `f.readlines()` → Read as list of lines.
- `f.readline()` → Read one line at a time.
- `f.write()` → Write to file.
- `f.tell()` → Get current position.
- `f.seek()` → Move to a position.
- `'rb'` / `'wb'` → Binary mode for non-text files.

## Key Takeaway
File objects let Python read and write both text and binary files efficiently — using context managers, chunked reading, and the right mode (`r`/`w`/`a`/`rb`/`wb`) keeps file handling safe and memory-friendly.
