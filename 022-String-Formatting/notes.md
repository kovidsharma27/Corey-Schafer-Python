# Video 22 — String Formatting

## Status

✅ Completed

## What I Learned

- Learned why string concatenation with `+` can be difficult to read and maintain.
- Learned how to use `.format()` for cleaner string formatting.
- Learned that `{}` are replacement fields/placeholders.
- Learned that positional indexes in `.format()` start at `0`.
- Learned how to use numbered replacement fields such as `{0}` and `{1}`.
- Learned how to reuse the same value with a replacement field.
- Learned how to access dictionary values inside replacement fields.
- Learned how to format lists using `.format()`.
- Learned how to access object attributes using `.format()`.
- Learned how to use keyword arguments with `.format()`.
- Learned how `**dictionary` unpacks dictionary values as keyword arguments.
- Learned how to format numbers with leading zeros.
- Learned how to control decimal places using `.2f` and `.3f`.
- Learned how to add thousands separators using `:,`.
- Learned how to format `datetime` objects.
- Learned common datetime formatting codes such as `%B`, `%d`, `%Y`, `%A`, and `%j`.

## What I Practiced

- Replaced string concatenation with `.format()`.
- Used positional and keyword arguments with `.format()`.
- Accessed dictionary and list values through replacement fields.
- Formatted object attributes.
- Formatted numbers with different widths and decimal places.
- Added thousands separators to numbers.
- Formatted dates using `datetime` and `.format()`.

## Verification

I reviewed the examples from the video in vs code and understood how `.format()` can be used to format strings, dictionaries, lists, numbers, objects, and dates.

## Notes

Basic formatting:

    sentence = "My name is {} and I am {} years old.".format("Jenn", 23)

Positional arguments:

    sentence = "My name is {0} and I am {1} years old.".format("Jenn", 23)

Dictionary values:

    sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)

Keyword arguments:

    sentence = "My name is {name} and I am {age} years old.".format(name="Jenn", age=23)

Dictionary unpacking:

    sentence = "My name is {name} and I am {age} years old.".format(**person)

Number formatting:

    "{:02}".format(5)
    "{:03}".format(5)
    "{:.2f}".format(3.14159265)
    "{:,}".format(1000000)

Examples:

    05
    005
    3.14
    1,000,000

Date formatting:

    "{:%B %d, %Y}".format(my_date)

Common datetime codes:

- `%B` → Full month name
- `%d` → Day of the month
- `%Y` → Four-digit year
- `%A` → Full weekday name
- `%j` → Day of the year

## Key Takeaway

The `.format()` method provides a cleaner and more powerful way to create formatted strings. It can work with dictionaries, lists, objects, numbers, and dates, while giving control over how values are displayed.
