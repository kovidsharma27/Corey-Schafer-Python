# Video 27 — Python Tutorial: Generate Random Numbers and Data using the random module

## Status
✅ Completed

## What I Learned
- Learned how to generate random numbers using the `random` module.
- Learned how to pick random values from a list, with and without duplicates.
- Learned how to shuffle a list randomly.
- Learned how to weight random choices to make some values more/less likely.
- Learned that `random` should not be used for security/cryptography purposes.

## What I Practiced
- Generated random floats using `random.random()` and `random.uniform()`.
- Generated random integers using `random.randint()`.
- Picked a single random value using `random.choice()`.
- Picked multiple random values (with possible duplicates) using `random.choices()`.
- Weighted random choices using the `weights` parameter.
- Shuffled a list in place using `random.shuffle()`.
- Picked multiple unique random values using `random.sample()`.
- Built a fake data generator using random names, addresses, phone numbers, and emails.

## Main Concepts

### Security Note
`random` module is **not cryptographically secure** — use the `secrets` module instead for anything security-related.

### Randomness Behavior
- A stored variable (e.g. `value = random.random()`) stays fixed for the rest of that run — printing it again gives the same result.
- Calling the function fresh each time (`random.random()` directly) gives a new value every call, even within the same run.

### `choices()` vs `sample()`
- `choices()` → Multiple random values, **duplicates possible**.
- `sample()` → Multiple random values, **guaranteed unique**.

## Important Commands / Examples

### Random Numbers
- `random.random()` → Random float between 0 (inclusive) and 1 (exclusive).
- `random.uniform(a, b)` → Random float between `a` (inclusive) and `b` (exclusive).
- `random.randint(a, b)` → Random integer, both `a` and `b` inclusive.

### Random Selection
- `random.choice(list)` → One random value from a list.
- `random.choices(list, k=n)` → `n` random values, duplicates allowed.
- `random.choices(list, weights=[...], k=n)` → Weighted random selection.
- `random.sample(list, k=n)` → `n` random **unique** values.

### Shuffling
- `random.shuffle(list)` → Shuffles list **in place** (no new variable/return value).

## Practical Example
```python
import random

colors = ['Red', 'Black', 'Green']

# Weighted random choice — Green is much less likely
result = random.choices(colors, weights=[18, 18, 2], k=1)
print(result)

# Unique random sample from a deck of cards
deck = list(range(1, 53))
hand = random.sample(deck, k=5)
print(hand)
```
This picks a weighted random color and deals 5 unique random cards from a simulated deck.

## Verification
I followed the examples from the video and practiced random number/data generation.

- `random.shuffle()` modifies the original list directly; it does not return a new list.
- `random.choices()` can return duplicate values — use `random.sample()` when uniqueness is required.
- A variable storing a random value stays constant until reassigned; only a fresh function call or a new script run produces a different value.

## Notes
- `random.random()` → Random float (0–1).
- `random.uniform()` → Random float (custom range).
- `random.randint()` → Random integer (inclusive range).
- `random.choice()` → One random value.
- `random.choices()` → Multiple random values (duplicates possible).
- `random.sample()` → Multiple unique random values.
- `random.shuffle()` → Shuffle list in place.
- `secrets` → Use instead of `random` for security-related randomness.

## Key Takeaway
The `random` module provides simple, flexible tools for generating random numbers and selections — useful for games, simulations, and test data, but never for security-sensitive operations.
