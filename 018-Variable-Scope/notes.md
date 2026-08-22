# Video 18 — Python Tutorial: Variable Scope - Understanding the LEGB rule and global/nonlocal statements

## Status

✅ Completed

## What I Learned

- Learned about variable scope in Python.
- Learned the LEGB rule: Local → Enclosing → Global → Built-in.
- Learned about local, enclosing, global, and built-in scopes.
- Learned how `global` allows a function to modify a global variable.
- Learned how `nonlocal` allows an inner function to modify a variable from its enclosing function.
- Learned that function parameters are local variables.
- Learned that nested functions use enclosing scope.
- Learned that built-in names can be overridden, but this should generally be avoided.

## What I Practiced

- Practiced identifying local and global variables.
- Practiced understanding nested functions and enclosing scope.
- Practiced using `global` and `nonlocal`.
- Practiced understanding how Python searches for variables using LEGB.

## Verification

I reviewed the examples in vs code from the video and understood how Python resolves variable names using the LEGB rule.

## Notes

The **LEGB rule** determines where Python searches for a variable:

**Local → Enclosing → Global → Built-in**

- **Local** → variables inside the current function.
- **Enclosing** → variables in an outer function when using nested functions.
- **Global** → variables defined at the module level.
- **Built-in** → Python's built-in names and functions.

Function parameters are also local variables.

The `global` keyword tells Python that a variable inside a function refers to a global variable.

The `nonlocal` keyword tells Python that a variable inside an inner function belongs to its enclosing function.

Built-in names such as `min()` can technically be overridden, but this should generally be avoided because it can prevent the original built-in function from being used.

## Key Takeaway

Python follows the **LEGB rule** when searching for variables:

**Local → Enclosing → Global → Built-in**

Understanding scope, `global`, and `nonlocal` is important when working with variables inside functions and nested functions.
