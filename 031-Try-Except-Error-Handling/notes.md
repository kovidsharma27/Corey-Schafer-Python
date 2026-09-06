# Video 31 — Python Tutorial: Using Try/Except Blocks for Error Handling
 
## Status
✅ Completed
 
## What I Learned
- Learned how to handle runtime errors gracefully using try/except blocks.
- Learned the roles of `try`, `except`, `else`, and `finally`.
- Learned why catching specific exceptions is better than catching everything generically.
- Learned how to raise custom exceptions manually.
- Learned Python's exception class hierarchy and why except-block ordering matters.
## What I Practiced
- Caught errors using `try`/`except`.
- Caught specific exceptions (`FileNotFoundError`) vs generic ones (`Exception`).
- Printed the actual error message using `except Exception as e`.
- Used `else` to run code only when no exception occurred.
- Used `finally` to run cleanup code regardless of success/failure.
- Manually raised an exception using `raise`.
- Ordered except blocks from most specific to most general.
## Main Concepts
 
### Try/Except/Else/Finally
- `try` → Runs code that might raise an error.
- `except` → Catches and handles the error if one occurs.
- `else` → (Optional) Runs only if no exception was raised.
- `finally` → (Optional) Always runs, used for cleanup (e.g. closing files).
### Why Be Specific
A generic `except Exception` catches almost everything, which can hide unrelated bugs (e.g. a `NameError` being mistaken for a `FileNotFoundError`). Catching specific exceptions first keeps error handling accurate.
 
### Exception Hierarchy
All exceptions inherit from `BaseException` → most from `Exception`. Catching a parent class also catches all its child exceptions.
 
```
BaseException
├── KeyboardInterrupt
├── SystemExit
└── Exception
     ├── ArithmeticError
     │     ├── ZeroDivisionError
     │     ├── OverflowError
     │     └── FloatingPointError
     ├── LookupError
     │     ├── IndexError
     │     └── KeyError
     ├── OSError
     │     ├── FileNotFoundError
     │     └── PermissionError
     ├── SyntaxError
     │     └── IndentationError
     ├── AttributeError
     ├── NameError
     │     └── UnboundLocalError
     ├── TypeError
     ├── ValueError
     ├── ImportError
     │     └── ModuleNotFoundError
     ├── RuntimeError
     └── StopIteration
```
 
### Ordering Rule
Except blocks must go from **most specific → most general**. A general `except Exception` placed before a specific one will catch everything first, making the specific block unreachable.
 
## Important Commands / Examples
- `try: ... except ExceptionType: ...` → Catch a specific error type.
- `except Exception as e: print(e)` → Print the actual error message.
- `else:` → Runs only if `try` succeeded.
- `finally:` → Always runs (cleanup).
- `raise Exception` → Manually trigger an exception.
## Practical Example
```python
try:
    result = 10 / 0
except ZeroDivisionError:          # Checked first — specific
    print("Caught a division by zero!")
except Exception:                  # Fallback — general
    print("Caught some other error!")
finally:
    print("Done.")
```
This correctly catches the specific `ZeroDivisionError` before falling back to a general exception handler, then always runs the cleanup step.
 
## Verification
I followed the examples from the video and practiced structured error handling.
 
- Catching a general `Exception` first makes any later, more specific `except` block unreachable — always order specific → general.
- `except FileNotFoundError` will **not** catch unrelated errors like `NameError` — the program will still crash unless a broader `except Exception` is also present.
- `finally` runs even if an exception was never caught, or even if the `try` succeeded.
## Notes
- `try` / `except` → Catch and handle errors.
- `else` → Runs only on success.
- `finally` → Always runs (cleanup).
- `raise` → Manually trigger an exception.
- `except Exception as e` → Access the error message.
- Exception ordering → Specific before general.
## Key Takeaway
Try/except/else/finally blocks let Python handle errors predictably and gracefully — catching specific exceptions first (rather than a broad catch-all) keeps error handling accurate and prevents masking unrelated bugs.
