# Video 14 — Python Tutorial for Beginners 14: Virtual Environments

## Status

✅ Completed

## What I Learned

* Learned what a **virtual environment** is and why it is useful.
* Learned how virtual environments isolate packages and their versions for different projects.
* Learned how to create, activate, deactivate, and delete a virtual environment.
* Learned how to check which Python and `pip` are being used.
* Learned how to install packages inside a virtual environment.
* Learned how to save dependencies in `requirements.txt`.
* Learned how to recreate an environment's packages using `requirements.txt`.
* Learned that virtual environments should contain dependencies, not project source code.
* Learned that modern Python provides the built-in `venv` module.

---

# Why Use Virtual Environments?

Different projects may require different versions of the same package.

Without virtual environments:

```text
Global Python
├── Project A → Django 4
└── Project B → Django 5
```

The package versions can conflict.

With virtual environments:

```text
Project A → Environment → Django 4
Project B → Environment → Django 5
```

Each project has its own isolated dependencies.

---

# Creating a Virtual Environment

Corey's tutorial uses:

```bash
pip install virtualenv
virtualenv project1_env
```

* `virtualenv` → creates a virtual environment.
* `project1_env` → name of the environment.

For modern Python projects, the built-in `venv` can be used instead:

```powershell
python -m venv .venv
```

---

# Activating the Environment

### macOS/Linux

```bash
source project1_env/bin/activate
```

### Windows PowerShell

```powershell
project1_env\Scripts\Activate.ps1
```

### Windows CMD

```cmd
project1_env\Scripts\activate.bat
```

After activation, the terminal normally shows:

```text
(project1_env)
```

This indicates that the environment is active.

---

# Checking the Active Environment

macOS/Linux:

```bash
which python
which pip
```

Windows:

```powershell
where python
where pip
```

These commands show which Python and `pip` executables are being used.

If the environment is active, the paths should point inside the virtual environment.

---

# Installing Packages

```bash
pip install numpy
pip install pytz
pip install psutil
```

Packages installed while the environment is active are installed **inside that environment**.

Check them with:

```bash
pip list
```

---

# `requirements.txt`

Save installed packages and their versions:

```bash
pip freeze --local > requirements.txt
```

Example:

```text
numpy==...
psutil==...
pytz==...
```

`requirements.txt` records the packages required by the project.

To install them into another environment:

```bash
pip install -r requirements.txt
```

This is useful when sharing a project or recreating its environment.

---

# Deactivating

```bash
deactivate
```

Stops using the active virtual environment.

The environment is **not deleted**.

---

# Deleting an Environment

macOS/Linux:

```bash
rm -rf project1_env/
```

Windows PowerShell:

```powershell
Remove-Item -Recurse -Force project1_env
```

The environment can be deleted because it can be recreated from the project requirements.

---

# Using a Specific Python Version

Corey demonstrates:

```bash
virtualenv -p /usr/bin/python2.6 py26_env
```

`-p` specifies the Python interpreter to use.

This demonstrates that a virtual environment can use a specific Python version.

**Modern note:** Python 2.6 is obsolete and should not be used for current projects.

---

# Important Concept

A virtual environment is for:

```text
Dependencies
Packages
Python environment
Package versions
```

It is **not** for storing your actual project files.

Good structure:

```text
my_project/
├── .venv/
├── main.py
├── requirements.txt
└── .gitignore
```

The project files stay outside `.venv`.

---

# VS Code Example

For a modern Windows project:

```powershell
mkdir calculator
cd calculator
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Then select `.venv` using:

```text
Ctrl + Shift + P
→ Python: Select Interpreter
→ Select .venv
```

Create:

```text
calculator.py
```

Example:

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
```

If the project needs a package:

```powershell
pip install requests
```

Save the dependencies:

```powershell
pip freeze > requirements.txt
```

---

# GitHub

Do **not** commit `.venv` to GitHub.

Add this to `.gitignore`:

```gitignore
.venv/
```

Commit:

```text
calculator.py
requirements.txt
.gitignore
```

When someone clones the project, they can recreate the environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---
## Verification

I followed the commands demonstrated in Video 14 and understood how to create, activate, use, deactivate, and delete a virtual environment.

I also identified the Windows PowerShell equivalents for the macOS/Linux commands used in the tutorial.

## Notes

Virtual environments isolate a project's Python packages and their versions from the global Python environment.

`requirements.txt` can be used to record and recreate a project's dependencies.

The virtual environment itself should not contain the project's source code and generally should not be committed to GitHub.

For modern Python projects, I can use Python's built-in `venv`:

```powershell
python -m venv .venv
```

On Windows PowerShell, it can be activated with:

```powershell
.venv\Scripts\Activate.ps1
```

The main workflow is:

```text
Create → Activate → Install packages → Work → Save requirements → Deactivate
```


Keep `.venv` out of GitHub and use `requirements.txt` to record the project's dependencies.

# Key Takeaway

A virtual environment gives each Python project an **isolated environment for its dependencies**.

The basic workflow is:

```text
Create environment
        ↓
Activate
        ↓
Install packages
        ↓
Work on project
        ↓
pip freeze > requirements.txt
        ↓
Deactivate
```

For modern Windows projects, a common approach is:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
