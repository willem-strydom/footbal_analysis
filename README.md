# SP23 Assignments

This repository contains template code for the assignments in the course. It will additionally serve as an _upstream repository_ to source potential updates and corrections for the assignments.

Assuming you've set up your repo according to the instructions below, run the following to fetch and merge the latest updates and corrections from the upstream repository to make sure your code is up-to-date:

```
git fetch upstream
```

> Note: `git fetch` only retrieves the latest changes from the upstream repo and saves them locally, it does not incorporate them into your active code -- `git merge` will do this in a later step.

If you want to review a log of the commits you'll be incorporating into your code, run:

```
git log upstream/hw1 ^hw1
```

> The caret `^` _excludes_ commits from the `hw1` branch, leaving only the commits that are unique to the `upstream/hw1` branch.

If you'd like to see the lines of code that where changed in a commit, run:

```
git show <first 6 digits of commit hash>
```

> It's annoying that there's not a particularly convenient way to reference a specific commit besides the first 6 digits of the hash, but at least 6 digits is within the range of [working memory](https://en.wikipedia.org/wiki/Working_memory).

If you're happy with the changes, merge them into your code:

```bash
git merge upstream/hw1
```

1. Open a shell terminal

   - A _Unix_ shell is **highly recommended**.
     - On MacOS: Your default terminal is a Unix shell.
     - On Windows:
       - You can use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) for a fully-featured Linux environment and terminal application, straight from your Windows desktop. You can choose any 'distro' you like, but Ubuntu is standard. I suggest two ways to interface with the WSL shell:
         - [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) is a new, modern terminal application that can launch WSL, PowerShell, Git Bash, or any other shell you have installed. Configure the settings to launch Ubuntu/WSL by default.
         - [VS Code](https://code.visualstudio.com/) provides an integrated terminal that can also use any shell installed on your system. Follow VS Code's [WSL setup instructions](https://code.visualstudio.com/docs/remote/wsl) to configure it to use WSL by default. Launch VS Code from the Windows Terminal with the command `code`.
       - If you absolutely must work in a true Windows environment, (for example, if you rely heavily on a Windows-only program such as GitHub Desktop or Power BI), you have two main options:
         - [Git Bash](https://gitforwindows.org/) _emulates_ a Unix shell, although you still may run into trouble with some commands and packages that expect you to be using a Unix shell.
         - [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.3) is a robust all-in-one command line shell and scripting language. Its syntax is quite different from Unix shells, but more and more tools are including Powershell compatibility.
     - If you're interested in customizing your shell to be a little more fun and powerful, check out [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh/wiki). With this program, built for `zsh` (z-shell), you can:
       - Customize your terminal prompt with a theme! Various themes have different colors, fonts, layouts, and icons. They also display different bits of information such as the git branch, git status, current working directory, etc. I like the default theme and the [powerlevel10k](theme).
       - Configure shortcut abbrevations for commands called _aliases_. `git add` becomes `ga`, `git commit -m` becomes `gcmsg`, etc. You can install plugins for [Poetry](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/poetry), [Pipenv](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/pipenv), [PosgreSQL](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/postgres), [Docker](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/docker), and [more](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins).
     - For a comprehensive tutorial-style introduction to using the command line, check out [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial).

2. Install and configure Git

   1. Install the latest version of [Git](https://git-scm.com/downloads) if you don't have it. The latest version is 2.39.1 at the time of this writing. Check your version with `git --version`.
   2. Configure [Git Credentials Manager (GCM)] to manage your git credentials for GitHub and other services.
      - [MacOS](https://github.com/GitCredentialManager/git-credential-manager/blob/release/docs/install.md#macos)
      - [Windows Subsystem for Linux (WSL)](https://github.com/GitCredentialManager/git-credential-manager/blob/release/docs/wsl.md)

3. Install and configure Python

   1. Install [Pyenv](https://github.com/pyenv/pyenv#installation) to manage your Python installations.
   2. Use Pyenv to install the latest version of Python and set it as the global default on your machine. At the time of this writing, the latest stable release is Python 3.11.1. The install might take a few minutes.

   ```bash
   pyenv install 3.11.1
   pyenv global 3.11.1
   ```

   If you find yourself needing an older version of Python in your project, (for example, Python 3.10 is the latest compatible version of Python for the package `pandas-profiling`), from your project's root directory, install and configure the version, e.g.:

   ```bash
   pyenv install 3.10.9
   pyenv local 3.10.9
   ```

   This creates a `.python-version` file in the project root directory that tells Pyenv and Poetry the version to use for the project.

4. Install and configure a _package_ and _virtual environment_ manager.
   These tools, such as Poetry, Pipenv, and Conda, ensure that your project's package dependencies are installed and run in a _virtual environment_. A _virtual environment_ is essentially a directory on your system that contains _executables_ for the Python installation and package installations. These tools provide an interface to maintaining these executables in such a way that you can seamlessly switch between executing code in different Python projects on your machine despite the fact that the projects have completely different sets of dependencies, which also contain their own nested hierarchy of dependencies. Without these tools, you would need to manually install, remove, upgrade, or downgrade packages to try and match the dependency requirements. This operation becomes more and more complex as the number of dependencies grows; the network of shared dependencies grows, and the likelihood of finding a conflict grows. Instead, these tools automatically update a configuration file to reflect any changes you make to your dependency requirements.

   Importantly, these tools help us share code by specifying the nature of your project's dependencies in a parseable configuration file. Anyone who wishes to execute your code can similarly use the tool to install the dependencies in a virtual environment on their own machine.

Here are the three most popular tools for package and virtual environment management:

- **Suggested**: [Poetry](https://python-poetry.org/docs/) sits at the cutting edge of the Python ecosystem. It uses a simple but powerful [command-line interface (CLI)](https://python-poetry.org/docs/cli/). A configuration file `pyproject.toml` is generated and maintained by Poetry, in part motivated by a [broader proposal](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata) to make `pyproject.toml` the final source of truth for all Python-related configuration metadata. `pyproject.toml` lists package dependencies, package-specific settings, and other project metadata such as the license, contributors, and version number.

  - [Install Poetry](https://python-poetry.org/docs/#installation).
  - Generate your initial `pyproject.toml` file.

    In your root directory, generate your `pyproject.toml` with the command `poetry init` and answer the questions in the interactive prompt. You should choose a name for your package that maps to the primary package or module that you want to expose in your API.

  - Install the dependencies from `pyproject.toml` in a virtual environment with `poetry install`. `poetry install` does a few things:
    1.  First it _resolves_ your dependencies, finding the newest version of each package that is compatible with all other dependencies and the versions specified in `pyproject.toml`.
    2.  Then it creates a `poetry.lock` file that stores a record of these resolved version numbers and the corresponding metadata.
    3.  It creates a virtual environment using your specified Python version if the virtual environment does not already exist.
    4.  Finally, installs all dependencies in the virtual environment.
  - Activate your virtual environment with `poetry shell`. Notice the `(\<package name\>-pyX.X)` prefix that appears in your terminal prompt. This indicates the active virtual environment. You can deactivate the virtual environment and close the shell with the command `exit` or simply deactivate with `deactivate`.
  - If you need to change the Python version assigned to your virtual environment, run `poetry env use <python version>`.

- [Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
  Pipenv implements many of the same dependency/environment management features as Poetry, but the CLI is compatible with the widely-known `pip install` command and the dependencies are specified in the widely-used `requirements.txt` file and format.
- `Conda` works independently from, but is still closely tied to, the Python ecosystem. Conda finds more usage among data scientists because it more gracefully handles dependencies on certain C libraries which are often needed for fast computations. These libraries are often installed directly on the host OS outside of anything Python-related on your machine. Thus, these packages cannot be simply packaged with pip. While packages with these kinds of requirements are becoming more rare, major packages such as [PyTables](https://www.pytables.org/usersguide/installation.html) and [PyMC](https://www.pymc.io/welcome.html) suggest a conda-first installation approach. In summary, Conda is a cross-platform tool that can install C libraries right alongside your project's main Python packages, using its own virtual environment management, its own package repository, its own CLI, etc.

For now I would say these are the minimum dependencies to get you started. More development dependencies may be required depending on the needs of the assignment or project.

Make a post in Discussions if you have any questions or run into any problems setting things up on your own!
