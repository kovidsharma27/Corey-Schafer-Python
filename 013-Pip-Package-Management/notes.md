# Video 13 — Python Tutorial for Beginners 13: pip

## Status

✅ Completed

## What I Learned

* Learned what `pip` is and why it is used in Python.
* Learned that `pip` is a package management tool for installing and managing Python packages.
* Learned that Python packages can be installed from the Python Package Index (PyPI) and other package indexes.
* Learned how to display general help for pip using `pip help`.
* Learned how to display help for a specific pip command using `pip help <command>`.
* Learned how to install a Python package using `pip install <package>`.
* Learned how to list installed Python packages using `pip list`.
* Learned how to uninstall a Python package using `pip uninstall <package>`.
* Learned how to find outdated installed packages using `pip list -o`.
* Learned that `-o` is the short form of `--outdated`.
* Learned that `pip list --outdated` shows installed packages for which newer versions are available.
* Learned that `-U` is the short form of `--upgrade`.
* Learned how to upgrade a package using `pip install -U <package>`.
* Learned that `pip install --upgrade <package>` is the long-form equivalent of `pip install -U <package>`.
* Learned what `pip freeze` does.
* Learned that `pip freeze` displays installed packages in a requirements-file format.
* Learned how package versions can be recorded using the `package==version` format.
* Learned how to redirect command output into a file using `>`.
* Learned how to create a requirements file from installed packages using `pip freeze > requirements.txt`.
* Learned what a `requirements.txt` file is used for.
* Learned how to display the contents of a text file using `cat` on macOS/Linux.
* Learned the Windows alternatives to `cat`, including `Get-Content` in PowerShell and `type` in Command Prompt.
* Learned how to install packages listed inside a requirements file using `pip install -r requirements.txt`.
* Learned that `-r` is the short form of `--requirement`.
* Learned that a requirements file contains packages or package requirements that pip can install.
* Learned what the pipe operator `|` does in a command-line shell.
* Learned that the pipe operator passes the output of one command as input to another command.
* Learned the basic purpose of the Unix commands `grep`, `cut`, and `xargs`.
* Learned that the final package-upgrade command shown in the video combines multiple command-line utilities together.
* Learned that commands used in macOS/Linux terminals are not always directly compatible with Windows Command Prompt or PowerShell.
* Learned that pip commands themselves are generally similar across Windows and macOS/Linux, while shell commands surrounding pip may differ.
* Learned that some commands demonstrated in older Python tutorials may no longer work with modern versions of pip or PyPI.

## What I Practiced

* Understanding the purpose of pip as Python's package manager.
* Understanding how to view pip's general help.
* Understanding how to view help for a specific pip command.
* Understanding how to install a Python package.
* Understanding how to list installed packages.
* Understanding how to uninstall a package.
* Understanding how to identify outdated packages.
* Understanding how to upgrade an installed package.
* Understanding how `pip freeze` represents installed packages.
* Understanding how to save `pip freeze` output into a requirements file.
* Understanding how to install packages from a requirements file.
* Understanding the difference between commands that only display information and commands that modify the Python environment.
* Understanding the difference between macOS/Linux shell commands and Windows shell commands.
* Understanding how pipes and output redirection are used in command-line operations.

## Important pip Commands

### `pip help`

Displays general help information about pip.

### `pip help install`

Displays help specifically for the `install` command.

### `pip install pympler`

Installs the `pympler` package.

* `pip` → Python's package manager
* `install` → tells pip that a package should be installed
* `pympler` → the package to install

Pip can install packages from PyPI and other supported package indexes.

### `pip list`

Lists the packages currently installed in the active Python environment.

### `pip list -o`

Lists installed packages that have newer versions available.

### `pip uninstall pympler`

Removes the `pympler` package from the current Python environment.

### `pip install -U setuptools`

Installs or upgrades `setuptools`.
`setuptools` is a library so we can use this command to update other libraries also.

## `pip freeze`

`pip freeze` outputs installed packages in a format that can be used as a requirements file.

### Important modern pip detail

`pip freeze` reports what is installed. It does not calculate a complete dependency lock or solve the environment from scratch. Modern pip also omits some bootstrap packaging tools by default, depending on the Python version.
`--all` can be used when those packages should also be included.

## `pip freeze > requirements.txt`

This command creates or overwrites a file called `requirements.txt` with the output of `pip freeze`.

## Viewing `requirements.txt`

### For Windows PowerShell

```text
Get-Content requirements.txt
```

### Windows Command Prompt

```text
type requirements.txt
```

Therefore:

| Purpose               | macOS/Linux            | Windows PowerShell             | Windows CMD             |
| --------------------- | ---------------------- | ------------------------------ | ----------------------- |
| Display file contents | `cat requirements.txt` | `Get-Content requirements.txt` | `type requirements.txt` |

This is a **shell difference**, not a pip difference.

---

## `pip install -r requirements.txt`

Installs the requirements listed in `requirements.txt`.

# Command-Line Concepts Used in the Video

The final part of the video goes beyond pip itself and demonstrates how command-line tools can be combined.

## Pipe: `|`

The `|` symbol is called a **pipe**.

It passes the output of one command to another command.
means:

> Run `command1` and send its output to `command2`.

# Final Command Demonstrated by Corey

Corey demonstrates the following Unix/macOS-style command:

```text
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

This command combines several operations.

The overall purpose is:

> Find the packages installed in the current environment, filter the output, extract the package names, and run `pip install -U` for each package.

# Windows Considerations

### Windows PowerShell

PowerShell has its own commands and text-processing features.

For example:

```text
Get-Content requirements.txt
```

can be used to display a file's contents

### Windows Command Prompt

Command Prompt can use:

```text
type requirements.txt
```

to display a file's contents.

The important lesson is:

> `pip` and the shell are two different things.

`pip` is the Python package manager.

PowerShell, Command Prompt, and macOS Terminal are environments/shells in which commands can be executed.

---

# PowerShell vs Command Prompt

Windows has more than one command-line environment.

## Command Prompt (`cmd`)

Command Prompt is the older Windows command-line shell.

Example:

```text
type requirements.txt
```

## PowerShell

PowerShell is a newer and more powerful Windows shell designed for command-line work and automation.

Example:

```text
Get-Content requirements.txt
```

Both can be used to run Python and pip commands.

The difference is mainly in the shell commands and scripting features available around those commands.

### Mostly informational

```text
pip help
pip help install
pip list
pip list -o
pip freeze
cat requirements.txt
```

These primarily display information.

### Commands that change the environment

```text
pip install pympler
pip uninstall pympler
pip install -U setuptools
pip install -r requirements.txt
```

These can install, remove, or modify packages in the Python environment.

The final command:

```text
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

also changes the environment because it upgrades packages.

---

# Important Options Learned

| Option | Long form       | Meaning                                                                     |
| ------ | --------------- | --------------------------------------------------------------------------- |
| `-o`   | `--outdated`    | Show outdated packages                                                      |
| `-U`   | `--upgrade`     | Upgrade a package                                                           |
| `-r`   | `--requirement` | Read requirements from a file                                               |
| `-l`   | `--local`       | In relevant virtual-environment contexts, restrict output to local packages |

## Verification

I followed the commands demonstrated in Video 13 and understood what each command is intended to do.

I did not execute the commands practically because I was currently focusing on understanding the concepts and command-line operations rather than modifying my Python environment.

I also identified the Windows equivalents for the macOS/Linux shell commands used in the video.

---

## Notes

This video introduced `pip`, Python's package management tool, and demonstrated how it can be used to install, uninstall, list, upgrade, and manage Python packages.

I learned that `pip` commands are generally similar across Windows and macOS/Linux, but commands provided by the shell can differ between operating systems.

I also learned that Windows Terminal and PowerShell are not the same thing. Windows Terminal is an application that can host different shells, including PowerShell and Command Prompt.

The video also introduced `requirements.txt`, which can be used to record Python package requirements and later install those requirements using:

```text
pip install -r requirements.txt
```

I learned how output redirection works with `>`:

```text
pip freeze > requirements.txt
```

This sends the output of `pip freeze` into a file instead of displaying it directly in the terminal.

---

## Key Takeaway

I learned that `pip` is Python's package manager and can be used to install, remove, inspect, upgrade, and manage Python packages.

I learned how `pip list` and `pip freeze` can be used to inspect installed packages, how `requirements.txt` can record package requirements, and how `pip install -r requirements.txt` can install those requirements.

I also learned that command-line commands are not always the same across operating systems. The `pip` commands are generally similar on Windows and macOS/Linux, while shell commands can differ.

The most important concept I took from this video is that **pip commands and shell commands are different things**, and understanding the difference is important when following Python tutorials on a different operating system.
