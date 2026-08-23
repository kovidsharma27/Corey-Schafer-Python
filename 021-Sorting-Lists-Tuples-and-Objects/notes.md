# Video 21 — Sorting Lists, Tuples, and Objects

## Status

✅ Completed

## What I Learned

- Learned the difference between `sorted()` and `.sort()`.
- Learned that `sorted()` returns a new sorted list without modifying the original.
- Learned that `.sort()` modifies the original list and returns `None`.
- Learned how to sort in descending order using `reverse=True`.
- Learned how to sort tuples using `sorted()`.
- Learned that `sorted()` always returns a list.
- Learned how `sorted()` works with dictionaries.
- Learned how to use `key` to customize sorting.
- Learned how to use `abs` as a sorting key.
- Learned how to sort objects using their attributes.
- Learned how to use a normal function, `lambda`, and `attrgetter` as sorting keys.

## What I Practiced

- Sorted lists in ascending and descending order.
- Compared `sorted()` with `.sort()`.
- Sorted tuples and dictionary keys.
- Sorted values using their absolute values.
- Created `Employee` objects and sorted them by name, age, and salary.
- Used `lambda` and `operator.attrgetter` for custom sorting.

## Verification

I reviewed the examples from the video and understood how to sort lists, tuples, dictionaries, and objects using different sorting methods and keys.

## Notes

`sorted()` returns a new sorted list:

    s_li = sorted(li)

`.sort()` modifies the original list:

    li.sort()

Descending order:

    sorted(li, reverse=True)

    li.sort(reverse=True)

`sorted()` can sort a tuple, but the result is a list:

    s_tup = sorted(tup)

When sorting a dictionary directly, `sorted()` sorts its keys:

    sorted(di)

The `key` argument specifies how values should be compared:

    sorted(li, key=abs)

Objects can be sorted using one of their attributes:

    sorted(employee, key=e_sort)

Using `lambda`:

    sorted(employee, key=lambda e: e.name)

Using `attrgetter`:

    from operator import attrgetter

    sorted(employee, key=attrgetter('age'))

`reverse=True` can also be combined with a custom key:

    sorted(employee, key=lambda e: e.salary, reverse=True)

## Key Takeaway

`sorted()` creates a new sorted list, while `.sort()` changes the original list. The `key` argument allows custom sorting rules, making it possible to sort complex data such as objects by their attributes.
