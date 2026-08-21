# Video 17 — Jupyter Notebook Tutorial: Introduction, Setup and Walkthrough

## Status

✅ Completed

## What I Learned

* Learned what Jupyter Notebook is and why it is useful.
* Learned how to start Jupyter Notebook using `jupyter notebook`.
* Learned that running Jupyter starts a notebook server.
* Learned that the notebook server can be accessed through the browser using localhost, commonly port `8888`.
* Learned that the terminal running the Jupyter server needs to remain open while using the notebook server.
* Learned that the Jupyter dashboard displays files and folders from the directory where the server was started.
* Learned how to create a new Jupyter Notebook.
* Learned that a Jupyter Notebook uses a kernel to execute code.
* Learned that the kernel determines which programming language/environment is being used.
* Learned about Command Mode and Edit Mode.
* Learned that `Esc` switches to Command Mode.
* Learned that `Enter` switches to Edit Mode.
* Learned how to execute code cells.
* Learned that `Ctrl + Enter` executes the current cell and stays on that cell.
* Learned that `Shift + Enter` executes the current cell and moves to the next cell.
* Learned that `Alt + Enter` executes the current cell and inserts a new cell below.
* Learned that Jupyter cells behave like an interactive Python prompt.
* Learned that the output of an expression can be displayed without using `print()`.
* Learned that the `In` and `Out` numbers show the order in which cells were executed.
* Learned that Jupyter cells do not have to be executed from top to bottom.
* Learned that variables can keep values from previous cell executions depending on execution order.
* Learned that `Run All` can execute all cells from top to bottom.
* Learned that cells above or below the current cell can also be executed.
* Learned how to add Markdown cells to a notebook.
* Learned that Markdown is translated into HTML when the Markdown cell is executed.
* Learned how Markdown can be used for headings, lists, bold text, italic text, and documentation.
* Learned that `!` can be used to execute shell/bash commands from a notebook.
* Learned what Jupyter Magic Commands are.
* Learned that `%` represents a Line Magic and `%%` represents a Cell Magic.
* Learned how to use `%lsmagic` to display available Magic Commands.
* Learned how to use `%pwd` to display the current working directory.
* Learned how to use `%ls` to list files and folders.
* Learned that `%timeit` can be used to measure Python code execution time.
* Learned about `%matplotlib inline` for displaying Matplotlib plots directly inside a notebook.
* Learned that Matplotlib is useful for creating charts and visualizations.
* Learned that Matplotlib is free and open-source.
* Learned that Pandas DataFrames can be displayed directly inside Jupyter in a readable table format.
* Learned about using NumPy together with Pandas for creating data.
* Learned about `%%html` for rendering HTML directly inside a notebook.
* Learned that HTML can be used to display or embed content such as an iframe.
* Learned that Jupyter notebooks can be exported into different formats.
* Learned how to download a notebook as HTML.
* Learned that an HTML export contains the notebook's code and output but is not an editable Jupyter Notebook.
* Learned that Jupyter Notebook files normally use the `.ipynb` extension.
* Learned that `.ipynb` files are structured as JSON files.
* Learned about using multiple kernels for different Python versions/environments.
* Learned that Conda environments can be used as Jupyter kernels.
* Learned how existing Jupyter notebooks can be downloaded and opened locally.
* Learned that existing notebooks can be useful for learning by inspecting their Markdown, code, formulas, and visualizations.

## What I Practiced

* Starting a Jupyter Notebook server from the terminal.
* Opening the Jupyter dashboard in the browser.
* Creating a new notebook and selecting a kernel.
* Switching between Command Mode and Edit Mode.
* Running individual cells using keyboard shortcuts.
* Understanding cell execution order using the `In` and `Out` numbers.
* Running all cells from top to bottom.
* Adding and executing Markdown cells.
* Running shell commands from inside a notebook using `!`.
* Using `%lsmagic` to explore Magic Commands.
* Using `%pwd` and `%ls`.
* Using `%timeit` to measure Python code execution.
* Using `%matplotlib inline` to display Matplotlib charts.
* Displaying Pandas DataFrames inside a notebook.
* Rendering HTML using `%%html`.
* Exporting a notebook as HTML.
* Understanding the `.ipynb` file format.
* Understanding the relationship between kernels, Python environments, and notebooks.
* Opening and experimenting with an existing Jupyter Notebook.

# Jupyter Notebook Notes

## What is Jupyter Notebook?

Jupyter Notebook is an interactive environment where we can write and execute Python code **cell by cell**.

It allows us to keep:

- Python code
- Code output
- Markdown explanations
- Charts and visualizations
- DataFrames
- Mathematical formulas

all inside one notebook.

---

## Main Uses

- Write and execute Python code interactively.
- See output directly below code cells.
- Add explanations using Markdown.
- Display charts and visualizations.
- Display Pandas DataFrames in a readable format.
- Run shell/bash commands.
- Use Jupyter Magic Commands.
- Export notebooks to different formats.
- Use different Python environments as different kernels.
- Download and reuse existing notebooks.

---

## Starting Jupyter Notebook

Run this in the terminal:

    jupyter notebook

Typical flow:

    Terminal
       ↓
    jupyter notebook
       ↓
    Jupyter Notebook Server
       ↓
    Browser → localhost:8888

Keep the terminal running because it is running the Jupyter server.

---

## Notebook Cells

A Jupyter Notebook is made up of cells.

The two important cell types are:

- **Code Cell** → Used to write and execute Python code.
- **Markdown Cell** → Used to write explanations, headings, notes, formulas, etc.

Example Python code:

    name = "Python"
    print(name)

---

## Markdown

Markdown allows us to write readable documentation inside the notebook.

Common Markdown syntax:

    # Heading 1
    ## Heading 2
    ### Heading 3

    **Bold text**

    *Italic text*

    - Item 1
    - Item 2
    - Item 3

    `inline code`

Markdown is useful for explaining what our code is doing.

---

## Running Shell / Bash Commands

Normally, a code cell is interpreted as Python.

If we put `!` before a command, Jupyter runs it as a shell/bash command.

Example:

    !pip list

This gives output similar to running `pip list` directly in the terminal.

Other examples:

    !ls
    !ls -la
    !pwd

So:

    Python code → normal Python execution

    !command → shell/bash command

---

## Jupyter Magic Commands

Jupyter provides special commands called **Magic Commands**.

They start with `%` or `%%`.

### Line Magic

A single `%` means the command works on that line.

Example:

    %pwd

### Cell Magic

Two `%%` signs mean the entire cell is treated as the command's input.

Example:

    %%html

    <h1>Hello</h1>

### List Available Magic Commands

Use:

    %lsmagic

This shows the available:

- Line Magics
- Cell Magics

---

## Useful Magic Commands

### `%pwd`

Shows the current working directory.

    %pwd

### `%ls`

Lists files and folders in the current directory.

    %ls

You can also pass normal options:

    %ls -la

### `%timeit`

Measures how long Python code takes to execute.

Example:

    %timeit [n*n for n in range(1000)]

This is useful when comparing the performance of different pieces of code.

### `%%html`

Allows HTML to be rendered directly inside the notebook.

Example:

    %%html

    <h1>Hello Jupyter</h1>
    <p>This is HTML.</p>

Jupyter can also use HTML to embed things such as an iframe.

### Other Magic Commands

Jupyter also provides magic commands for:

- JavaScript
- Bash
- HTML
- LaTeX
- Timing code
- Running scripts
- Other notebook functionality

Use `%lsmagic` to see the available commands.

---

## Matplotlib

**Matplotlib** is a Python library used to create charts and visualizations.

It is especially useful in Jupyter because charts can be displayed directly inside the notebook.

### Enable Inline Plots

Use:

    %matplotlib inline

Then Matplotlib plots can be displayed directly below the code cell.

Example:

    import numpy as np
    import matplotlib.pyplot as plt

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()

### Why Use Matplotlib in Jupyter?

Normally, we might run a Python script and then view the chart separately.

Jupyter allows us to:

    Write code
        ↓
    Run cell
        ↓
    See chart immediately

This makes it very useful for exploring data and code in real time.

---

## Pandas and NumPy Output

Jupyter can display Pandas DataFrames directly in a readable table.

Example:

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randn(10, 5))

    df.head()

`df.head()` displays the first few rows of the DataFrame.

This is useful for quickly inspecting data inside the notebook.

---

## HTML in Jupyter

The `%%html` cell magic allows HTML to be rendered directly in a notebook.

Example:

    %%html

    <h2>My Notebook</h2>
    <p>This is HTML content.</p>

It can also be used to embed content such as YouTube videos using an HTML iframe.

---

## Exporting Notebooks

Jupyter notebooks can be exported into different formats.

From the Jupyter interface:

    File
       ↓
    Download As
       ↓
    Choose format

For example, we can download a notebook as:

- Python file
- HTML
- Other supported formats

### Export as HTML

HTML is useful when we want to:

- Share the notebook.
- Put it on a blog.
- View the notebook without Jupyter.

The HTML version keeps the code and output in a readable format, but it is not the same as an editable Jupyter Notebook.

---

## Notebook Files

Jupyter notebooks normally use the:

    .ipynb

extension.

Example:

    Testing Jupyter.ipynb

A `.ipynb` file is essentially a **JSON file** containing the notebook information.

It stores things such as:

- Code cells
- Markdown cells
- Outputs
- Metadata
- Kernel information

Normally, we edit `.ipynb` files through Jupyter rather than manually editing the JSON.

---

## Multiple Kernels

A **kernel** is the environment that actually executes the code in a Jupyter Notebook.

Different Python environments can be used as different kernels.

For example:

    Python 3 Kernel
    Python 2 Kernel

A notebook can be connected to a specific kernel.

Basic idea:

    Notebook
       ↓
    Kernel
       ↓
    Python Environment
       ↓
    Execute Python Code

This allows different notebooks to use different Python versions or environments.

---

## Conda Environments and Kernels

With Anaconda/Conda, different environments can be used with Jupyter.

To see Conda environments:

    conda env list

For example:

    python27
    root

The tutorial's example showed a Python 2.7 Conda environment being available as a Jupyter kernel.

The important idea is:

    Conda Environment
           ↓
        Jupyter
           ↓
         Kernel
           ↓
    Notebook uses that environment

If Jupyter is installed/configured in an environment, that environment can be available for use as a kernel.

---

## Downloading Existing Notebooks

Jupyter notebooks can be downloaded from online collections and opened locally.

Existing notebooks may contain:

- Explanations
- Python code
- Mathematical formulas
- Charts
- Visualizations

Typical workflow:

    Download .ipynb notebook
            ↓
    Put it in your Jupyter directory
            ↓
    Reload Jupyter Dashboard
            ↓
    Open the notebook
            ↓
    Inspect / edit / run cells

This is useful for learning because we can see how other people created their notebooks.

For example, if a notebook contains a mathematical formula or visualization, we can click the cell, enter edit mode, and see the code used to create it.

---

## Notebook as an Interactive Document

A Jupyter Notebook combines documentation and executable code.

Instead of having:

    Python script
    + separate notes
    + separate charts
    + separate data output

we can keep everything together:

    Jupyter Notebook
    ├── Markdown explanations
    ├── Python code
    ├── Output
    ├── Charts
    ├── DataFrames
    └── Formulas

This is one of the main reasons Jupyter is popular for data exploration and research.

---

## Important Commands to Remember

| Command | Purpose |
|---|---|
| `jupyter notebook` | Start Jupyter Notebook |
| `!pip list` | Run a shell command |
| `!ls` | List files using shell |
| `!pwd` | Show directory using shell |
| `%pwd` | Show current working directory |
| `%ls` | List files/folders |
| `%lsmagic` | List available Magic Commands |
| `%timeit` | Measure code execution time |
| `%matplotlib inline` | Display Matplotlib plots inside notebook |
| `%%html` | Render HTML in a cell |

---

## Quick Mental Model

    Jupyter Notebook
    │
    ├── Code Cells
    │     └── Execute Python
    │
    ├── Markdown Cells
    │     └── Notes / Documentation
    │
    ├── Shell Commands
    │     └── !command
    │
    ├── Magic Commands
    │     ├── %line_magic
    │     └── %%cell_magic
    │
    ├── Visualization
    │     └── Matplotlib
    │
    ├── Data
    │     └── Pandas / NumPy
    │
    ├── Kernel
    │     └── Python Environment
    │
    └── Export
          ├── Python
          └── HTML

---

## Key Takeaways

- Jupyter Notebook lets us execute Python **interactively, cell by cell**.
- Use **Code cells** for Python code.
- Use **Markdown cells** for explanations and documentation.
- Use `!` to run shell/bash commands.
- Use `%` for **Line Magic** commands.
- Use `%%` for **Cell Magic** commands.
- `%lsmagic` shows available Magic Commands.
- `%pwd` shows the current working directory.
- `%ls` lists files and folders.
- `%timeit` measures code execution time.
- `%matplotlib inline` displays Matplotlib plots directly inside the notebook.
- Pandas DataFrames can be displayed directly in a readable format.
- `%%html` allows HTML to be rendered inside a notebook.
- `.ipynb` is the standard Jupyter Notebook file extension.
- `.ipynb` files contain notebook information in JSON format.
- Different Python environments can be used through different kernels.
- Notebooks can be exported to formats such as Python and HTML.
- Existing `.ipynb` notebooks can be downloaded and opened locally.
- Jupyter is useful for **data exploration, visualization, experimentation, and research**.
