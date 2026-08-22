# Video 19 — Slicing Lists and Strings

## Status

✅ Completed

## What I Learned

- Learned how to access individual list elements using indexes.
- Learned that Python supports positive and negative indexes.
- Learned list slicing using `list[start:end:step]`.
- Learned that the `end` index is not included in the result.
- Learned how to omit `start` or `end` when slicing.
- Learned how to use a negative `step` to slice backwards.
- Learned that `[::-1]` reverses a list or string.
- Learned that the same slicing syntax can be used with strings.

## What I Practiced

- Accessed list elements using positive and negative indexes.
- Sliced lists using different start and end positions.
- Used positive and negative step values.
- Reversed a list using `[::-1]`.
- Sliced a string using indexes and slices.

## Verification

I reviewed the examples from the video in vs code and understood how indexing and slicing work with lists and strings.

## Notes

List slicing uses:

    list[start:end:step]

The `end` index is excluded.

Examples:

    my_list[0:5]
    my_list[1:]
    my_list[:-1]
    my_list[:]

A positive `step` moves forward:

    my_list[2:-1:2]

A negative `step` moves backwards:

    my_list[-1:2:-1]
    my_list[::-1]

`[::-1]` is commonly used to reverse a sequence.

Slicing also works with strings.

Example:

    sample_url = "http://coreyms.com"

    sample_url[7:]
    sample_url[-4:]
    sample_url[7:-4]
    sample_url[::-1]

## Key Takeaway

Python slicing uses `start:end:step` and works with sequences such as lists and strings. The `end` index is excluded, and a negative step can be used to move backwards or reverse a sequence.
