# Video 15 — Anaconda - Installation and Using Conda

## Status

✅ Completed

## What I Learned

* **Anaconda** is a Python distribution mainly useful for data science.
* It includes:

  * Python
  * Conda
  * Many pre-installed packages
  * Tools such as Jupyter Notebook
* **Conda** is a package manager and environment manager.
* **pip** mainly installs Python packages.
* Conda can also manage dependencies and different Python versions.
* Conda environments keep projects isolated from each other.
* Different environments can have different Python versions and packages.
* I can use a Conda environment as the Python interpreter for a project in VS Code.
* I do not need Anaconda just to learn normal Python.

## Main Concepts

### Anaconda

Anaconda provides Python together with many commonly used data-science packages.

It is useful for people working with tools such as:

* NumPy
* SciPy
* Matplotlib
* Jupyter

It is optional. Regular Python + pip is also fine for normal Python development.

### Anaconda vs Miniconda

**Anaconda**

* Full distribution.
* Many packages are installed by default.
* Uses more disk space.

**Miniconda**

* Smaller installation.
* Provides the basic Conda setup.
* Packages can be installed as needed.

### pip vs Conda

`pip` is mainly a Python package installer.

```text
pip install package_name
```

Conda can install packages and manage other dependencies as well:

```text
conda install package_name
```

Both can be used with Python environments.

### Conda Environment

A Conda environment is an isolated workspace containing its own Python and packages.

Example:

```text
project_a
├── Python
├── Flask
└── SQLAlchemy
```

Another project can have different versions without affecting `project_a`.

### Python Version

If I don't specify a Python version:

```text
conda create --name my_app flask sqlalchemy
```

Conda resolves a suitable/compatible Python version based on the dependencies and available packages.

If I specify one:

```text
conda create --name my_app python=3.12 flask sqlalchemy
```

Conda tries to create the environment using Python 3.12.

My normal Windows Python installation is separate from the Python inside a Conda environment.

## Important Commands / Examples

### Show Conda help

```text
conda --help
```

Shows available Conda commands and their usage.

### Show installed packages

```text
conda list
```

Shows packages managed by Conda in the current environment.

```text
pip list
```

Shows Python packages visible to pip in the current environment.

### Create an environment

```text
conda create --name my_app flask sqlalchemy
```

Creates an environment named `my_app` and installs Flask and SQLAlchemy.

`--name` can also be written as:

```text
-n
```

Example:

```text
conda create -n my_app flask sqlalchemy
```

### Create an environment with a specific Python version

```text
conda create --name my_app python=3.12 flask sqlalchemy
```

Creates the environment with Python 3.12.

Corey demonstrated Python 2.7 in this old tutorial, but Python 2.7 is obsolete and should not be installed today.

### Activate an environment

Modern Conda:

```text
conda activate my_app
```

This makes `my_app` the active environment.

The terminal may show:

```text
(my_app) C:\Users\MyName>
```

### Deactivate an environment

```text
conda deactivate
```

Leaves the currently active Conda environment.

### List environments

```text
conda env list
```

Shows all Conda environments.

An `*` indicates the currently active environment.

### Remove an environment

To delete the entire environment:

```text
conda remove --name my_app --all
```

`--all` removes the environment and everything installed inside it.

### Start Python

```text
python
```

Starts the Python interpreter belonging to the currently active environment.

To leave Python:

```text
exit()
```

### Find Python on Windows

Corey's macOS/Linux command:

```text
which python
```

Windows equivalent:

```text
where python
```

This shows where Windows is finding `python.exe`.

## Practical Example

Suppose I have a Flask project.

I can create a separate environment:

```text
conda create --name my_flask_project python=3.12 flask sqlalchemy
```

Then activate it:

```text
conda activate my_flask_project
```

Now this project can use:

```text
Python 3.12
Flask
SQLAlchemy
```

without changing my normal Windows Python installation.

In VS Code, I can select the `my_flask_project` Conda environment as the project's Python interpreter.

The basic workflow is:

```text
Create environment
       ↓
Activate environment
       ↓
Open project in VS Code
       ↓
Select Conda environment as Python interpreter
       ↓
Write and run Python code
```

## Verification

* Corey verified Anaconda by starting Python and importing packages such as NumPy and Matplotlib.
* `pip list` and `conda list` can be used to inspect installed packages.
* `where python` is the Windows equivalent of Corey's `which python`.
* Corey's video uses older Conda commands such as `activate` and `source activate`; modern Conda uses `conda activate`.
* The Python 2.7 example is only useful for understanding that Conda can manage different Python versions. Python 2.7 is obsolete today.
* On Windows, Anaconda Prompt is a convenient place to use Conda.

## Notes

* I don't need Anaconda just because I am learning Python.
* Anaconda is especially useful for data-science workflows.
* A Conda environment is separate from my normal Windows Python installation.
* Activating an environment changes which Python and packages my terminal uses.
* `conda create` creates an environment.
* `conda activate` enters an environment.
* `conda deactivate` leaves an environment.
* `conda env list` shows environments.
* `conda remove --name NAME --all` deletes an environment.
* `pip list` and `conda list` show packages for the current environment.
* VS Code can use a Conda environment as the Python interpreter for a project.
* I should not randomly change my Windows PATH or install old Python versions just to reproduce an old tutorial.

## Key Takeaway

**Anaconda provides Python, packages, Conda, and useful data-science tools. Conda's biggest advantage is creating isolated environments where each project can have its own Python version, packages, and dependencies.**
