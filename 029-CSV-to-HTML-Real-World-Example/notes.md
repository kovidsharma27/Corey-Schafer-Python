# Video 29 — Python Tutorial: Real World Examples - Parsing Names From a CSV to an Html List

## Status
✅ Completed

## What I Learned
- Learned how to apply the `csv` module to a real-world data processing task.
- Learned how to filter specific rows based on a condition while looping.
- Learned how to build an HTML string dynamically from CSV data using f-strings.

## What I Practiced
- Read a real-world patron CSV file using `csv.DictReader()`.
- Skipped a non-data description row using `next()`.
- Used `break` to stop collecting data once a specific marker row was reached.
- Built an HTML unordered list (`<ul><li>`) dynamically from filtered names.

## Main Concepts

### Real-World Use Case
A patron CSV file contains contributors who opted in ("1 + Reward" tier) and those who didn't ("No Reward" tier). Only opted-in patrons' names should appear in the final HTML contributors list.

### Filtering with `break`
Looping through `DictReader` rows and using `if condition: break` stops processing as soon as a specific marker row (`'No Reward'`) is reached — everything after it is excluded.

### Building HTML as a String
HTML output can be built incrementally using string concatenation (`+=`) and f-strings, turning raw CSV data into a ready-to-use HTML snippet.

## Important Commands / Examples
- `csv.DictReader(data_file)` → Read CSV rows as dictionaries.
- `next(csv_data)` → Skip a specific row (e.g., a description row).
- `if line['Field'] == 'value': break` → Stop the loop when a marker row is found.
- `html_output += f'\n\t<li>{name}</li>'` → Append formatted HTML per item.

## Practical Example
```python
import csv

names = []
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    next(csv_data)  # skip description row

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html = f'<p>There are currently {len(names)} public contributors. Thank You!</p>\n<ul>'
for name in names:
    html += f'\n\t<li>{name}</li>'
html += '\n</ul>'
```
This filters only opted-in patrons and builds a clean HTML list ready to paste into a webpage.

## Output

**Raw HTML generated:**
```html
<p>There are currently 30 public contributors. Thank You!</p>
<ul>
	<li>John Doe</li>
	<li>Dave Smith</li>
	<li>Mary Jacobs</li>
	...
	<li>Jane Stuart</li>
	<li>Maggie Jefferson</li>
</ul>
```

**How this renders on a website:**

> There are currently 30 public contributors. Thank You!
>
> - John Doe
> - Dave Smith
> - Mary Jacobs
> - ...
> - Jane Stuart
> - Maggie Jefferson

## Verification
I followed the example from the video and practiced applying `csv` + string/HTML building to a real dataset.

- `next()` must be used carefully — it skips exactly one row, so it must match the actual structure of the file (here, a one-line reward description).
- The `break` condition depends on exact string matching (`'No Reward'`) — if the CSV formatting changes, this logic could silently stop early or not at all.

## Notes
- `csv.DictReader()` → Read CSV rows as dictionaries.
- `next()` → Skip a row in an iterator.
- `break` → Exit a loop early based on a condition.
- `+=` with f-strings → Build formatted output (HTML) incrementally.

## Key Takeaway
Combining the `csv` module with simple string building lets you transform raw spreadsheet data into ready-to-use HTML — a practical technique for real-world data-to-web workflows.
