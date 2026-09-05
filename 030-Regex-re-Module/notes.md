# Video 30 — Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)

## Status
✅ Completed

## What I Learned
- Learned what regular expressions are and why they're used for pattern matching.
- Learned metacharacters, character sets, quantifiers, anchors, and groups.
- Learned how to search text and files using the `re` module.
- Learned the difference between `finditer()`, `findall()`, `match()`, and `search()`.
- Learned how to capture and reference groups, including substitution with backreferences.
- Learned how to use flags like `re.IGNORECASE`.

## What I Practiced
- Compiled patterns using `re.compile()`.
- Searched text using `.finditer()`, `.findall()`, `.match()`, and `.search()`.
- Escaped special characters using backslashes.
- Used character classes (`\d`, `\D`, `\w`, `\W`, `\s`, `\S`).
- Used anchors (`\b`, `\B`, `^`, `$`).
- Used character sets (`[]`, `[^]`, ranges like `[a-d]`).
- Used quantifiers (`*`, `+`, `?`, `{n}`, `{n,m}`).
- Used groups (`()`) and alternation (`|`).
- Captured group data using `.group(n)`.
- Performed substitution using `.sub()` with backreferences.
- Searched patterns inside an external file using a context manager.

## Main Concepts

### Raw Strings
`r'pattern'` tells Python not to interpret backslashes specially — essential for regex patterns since they rely heavily on `\`.

### Metacharacters
| Pattern | Matches |
|---|---|
| `.` | Any character except newline |
| `\d` / `\D` | Digit / Not a digit |
| `\w` / `\W` | Word character / Not a word character |
| `\s` / `\S` | Whitespace / Not whitespace |

### Anchors
| Pattern | Matches |
|---|---|
| `\b` / `\B` | Word boundary / Not a word boundary |
| `^` | Beginning of string |
| `$` | End of string |

### Character Sets
- `[abc]` → Matches any one character in the set.
- `[^abc]` → Matches any character NOT in the set.
- `[a-z]` → Matches any character in the range.

### Quantifiers
| Pattern | Matches |
|---|---|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n}` | Exactly n |
| `{n,m}` | Between n and m |

### Groups & Alternation
- `( )` → Groups part of a pattern (can be captured/referenced).
- `\|` → Either/or between alternatives.
- `.group(n)` → Access a specific captured group (`0` = full match).

## Important Commands / Examples

### Compiling & Searching
- `re.compile(r'pattern')` → Creates a reusable pattern object.
- `pattern.finditer(text)` → Returns an iterator of all match objects (with position info).
- `pattern.findall(text)` → Returns matches as a list of strings (or tuples if multiple groups).
- `pattern.match(text)` → Matches only at the **beginning** of the string; returns `None` if not found there.
- `pattern.search(text)` → Matches **anywhere** in the string; returns only the first match.

### Substitution
- `pattern.sub(r'\2\3', text)` → Replaces matches using backreferences to captured groups.

### Flags
- `re.IGNORECASE` or `re.I` → Case-insensitive matching.

## Practical Example
```python
import re

emails = 'CoreyMSchafer@gmail.com, corey.schafer@university.edu'

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.findall(emails)
print(matches)
```
This matches valid email addresses in a block of text, handling dots, hyphens, underscores, and multiple domain extensions.

## Verification
I followed the examples from the video and practiced building/testing regex patterns against sample text and a real file.

- `+` requires at least one character after the match point — excludes single-letter cases like "Mr. T" that `*` would include.
- Alternation (`|`) tries options **in order** — matters when one option is a substring of another (e.g., `Mr` inside `Mrs`).
- `.match()` only checks the start of the string, even if the pattern exists elsewhere — use `.search()` for anywhere-in-string matching.
- `.findall()` returns only captured groups (not full matches) when the pattern contains groups.

## Notes
- `re.compile()` → Create a pattern object.
- `.finditer()` → All matches as match objects (with position).
- `.findall()` → All matches as strings/tuples.
- `.match()` → Match only at start of string.
- `.search()` → First match anywhere in string.
- `.sub()` → Substitute matches using backreferences.
- `.group(n)` → Access a specific captured group.
- `re.IGNORECASE` / `re.I` → Case-insensitive flag.

## Key Takeaway
The `re` module provides powerful, flexible pattern matching for text — combining character classes, quantifiers, anchors, and groups makes it possible to reliably extract structured data like emails, phone numbers, and URLs from raw text.
