# Video 20 — Comprehensions

## Status

✅ Completed

## What I Learned

- Learned that comprehensions provide a concise way to create collections.
- Learned about **list comprehensions**.
- Learned how to use conditions inside list comprehensions.
- Learned how list comprehensions compare with `for` loops, `map()`, and `filter()`.
- Learned about **dictionary comprehensions**.
- Learned how to add conditions to dictionary comprehensions.
- Learned about **set comprehensions**.
- Learned how `zip()` combines values from multiple iterables into tuples.
- Learned that `zip()` stops when the shortest iterable is exhausted.

## What I Practiced

- Created lists using list comprehensions.
- Used expressions such as `n * n` inside list comprehensions.
- Used conditions to select specific values.
- Used nested list comprehensions.
- Created dictionaries using dictionary comprehensions.
- Used conditions inside dictionary comprehensions.
- Created sets using set comprehensions.
- Used `zip()` to combine names and heroes.

## Verification

I reviewed the examples from the video in vs code and understood how list, dictionary, and set comprehensions work.

## Notes

List comprehension syntax:

    [expression for item in iterable]

With a condition:

    [expression for item in iterable if condition]

Example:

    [n * n for n in nums]

    [n for n in nums if n % 2 == 0]

Nested comprehensions can replace certain nested `for` loops:

    [(letter, num) for letter in "abcd" for num in range(4)]

`map()` applies a function to each item and produces transformed values.

`filter()` keeps only the items that satisfy a condition.

`zip()` combines corresponding values from iterables into tuples.

Dictionary comprehension syntax:

    {key: value for item in iterable}

With a condition:

    {key: value for item in iterable if condition}

Set comprehension syntax:

    {expression for item in iterable}

Sets automatically remove duplicate values.

## Key Takeaway

Comprehensions provide a concise and readable way to create lists, dictionaries, and sets. They are especially useful when transforming or filtering values and can often replace simple `for` loops.
