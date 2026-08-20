# Video 16 — Managing Multiple Projects, Virtual Environments & Environment Variables

## Status

✅ Completed

## What I Learned

- Each Python project can have its own Conda environment.
- Separate environments prevent dependency conflicts between projects.
- `environment.yaml` can be used to recreate a Conda environment.
- Conda environments are stored separately from project files.
- `activate.d` scripts run when an environment is activated.
- `deactivate.d` scripts run when an environment is deactivated.
- Environment variables can store project-specific configuration.
- Different projects can use the same environment variable name with different values.
- `conda activate` and `conda deactivate` are the modern Conda commands.

## Main Concepts

### 1. Creating a Project

```bash
mkdir my_project
cd my_project
```

- `mkdir` → create a directory.
- `cd` → change directory.

Useful path shortcuts:

```text
.   → current directory
..  → parent directory
~   → home directory
```

Example:

```bash
cd ../coreyms_web/
```

Go up one directory, then enter `coreyms_web`.

### 2. Conda Environments

A Conda environment provides an isolated place for a project's Python version and packages.

Example:

```text
Project A → my_project_env
Project B → coreyms_web
```

This prevents packages and Python versions from different projects from conflicting.

List environments:

```bash
conda env list
```

Activate:

```bash
conda activate my_project_env
```

Deactivate:

```bash
conda deactivate
```

Corey used the older syntax:

```bash
source activate my_project_env
source deactivate
```

On Windows, use:

```powershell
conda activate my_project_env
conda deactivate
```

### 3. environment.yaml

`environment.yaml` is like a recipe/configuration for a Conda environment.

Create an environment from it:

```bash
conda env create -f environment.yaml
```

`-f` means to use the specified file.

The idea:

```text
environment.yaml
       ↓
Conda reads the configuration
       ↓
Environment is created
```

This is useful when sharing or recreating a project environment.

### 4. Environment Location

`conda env list` shows where environments are physically stored.

Example:

```text
my_project_env    C:\Users\You\anaconda3\envs\my_project_env
```

The project might be:

```text
projects/
└── my_project/
```

while the environment is:

```text
anaconda3/
└── envs/
    └── my_project_env/
```

The project folder and Conda environment are related, but they are not the same folder.

### 5. activate.d and deactivate.d

Corey created:

```text
etc/
└── conda/
    ├── activate.d/
    │   └── env_vars.sh
    └── deactivate.d/
        └── env_vars.sh
```

- `activate.d` → scripts that run when the environment is activated.
- `deactivate.d` → scripts that run when the environment is deactivated.

This allows project-specific configuration to be automatically applied and cleaned up.

### 6. Environment Variables

An environment variable stores a value that programs can access through the environment.

Example:

```bash
export DATABASE_URI="project_database"
```

Check the value:

```bash
echo $DATABASE_URI
```

Remove it:

```bash
unset DATABASE_URI
```

The workflow:

```text
conda activate
      ↓
activate.d/env_vars.sh
      ↓
DATABASE_URI is set

conda deactivate
      ↓
deactivate.d/env_vars.sh
      ↓
DATABASE_URI is removed
```

### 7. Multiple Projects

Different projects can have different values for the same variable.

Example:

```text
my_project_env
DATABASE_URI = database_A

coreyms_web
DATABASE_URI = database_B
```

When switching environments, the appropriate project's configuration can be loaded automatically.

## Important Commands / Examples

### Create and enter a project

```bash
mkdir my_project
cd my_project
```

### Create environment from YAML

```bash
conda env create -f environment.yaml
```

### List environments

```bash
conda env list
```

### Activate / deactivate

```bash
conda activate my_project_env
conda deactivate
```

### Open current folder in VS Code

Corey used:

```bash
subl .
```

For VS Code:

```bash
code .
```

`.` means the current directory.

### List files

```bash
ls -la
```

- `ls` → list files/directories
- `-l` → detailed information
- `-a` → include hidden files

PowerShell:

```powershell
Get-ChildItem -Force
```

### Display a file

```bash
cat environment.yaml
```

PowerShell:

```powershell
Get-Content environment.yaml
```

### Create folders

Corey used:

```bash
mkdir -p etc/conda/activate.d
mkdir -p etc/conda/deactivate.d
```

`-p` creates missing parent directories too.

PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path etc\conda\activate.d
New-Item -ItemType Directory -Force -Path etc\conda\deactivate.d
```

### Create files

Corey used:

```bash
touch etc/conda/activate.d/env_vars.sh
touch etc/conda/deactivate.d/env_vars.sh
```

`touch` creates an empty file if it doesn't exist.

PowerShell:

```powershell
New-Item etc\conda\activate.d\env_vars.sh -ItemType File
New-Item etc\conda\deactivate.d\env_vars.sh -ItemType File
```

### Check environment variable

Bash/macOS/Linux:

```bash
echo $DATABASE_URI
```

PowerShell:

```powershell
echo $env:DATABASE_URI
```

CMD:

```cmd
echo %DATABASE_URI%
```

### Start Python

```bash
python
```

This starts Python using the currently active environment.

Leave Python:

```python
exit()
```

`exit()` leaves Python but does not deactivate the Conda environment.

## Practical Example

Suppose I have:

```text
projects/
├── website/
└── data_app/
```

I can create separate environments:

```text
website  → website_env
data_app → data_app_env
```

The website environment could have:

```text
DATABASE_URI = website_database
```

The data app could have:

```text
DATABASE_URI = data_database
```

Activate the website environment:

```bash
conda activate website_env
```

Check:

```bash
echo $DATABASE_URI
```

Output:

```text
website_database
```

Switch environments:

```bash
conda deactivate
conda activate data_app_env
```

Now the variable can be:

```text
data_database
```

This allows each project to keep its own dependencies and configuration.

## Verification

- Practiced creating and navigating project directories.
- Practiced listing Conda environments.
- Understood how `environment.yaml` can recreate an environment.
- Understood the difference between project folders and Conda environment folders.
- Set up `activate.d` and `deactivate.d`.
- Tested environment variables using `echo`.
- Tested activation and deactivation behavior.
- Understood how multiple projects can have separate environments and configuration.
- Learned Windows equivalents for the Bash/macOS/Linux commands used by Corey.

## Notes

```text
conda env list       → show Conda environments
conda activate NAME  → activate an environment
conda deactivate     → deactivate an environment

environment.yaml     → environment configuration/recipe

activate.d           → runs during activation
deactivate.d         → runs during deactivation

export               → set environment variable
unset                → remove environment variable
echo                 → display a value

.                    → current directory
..                   → parent directory
~                    → home directory

code .               → open current folder in VS Code
python               → start Python
exit()               → leave Python
```

## Key Takeaway

> Give each Python project its own environment and configuration. Conda environments isolate Python and packages, while `activate.d` and `deactivate.d` can automatically manage environment variables when switching between projects.
````
