# SP23 Assignments

This repository contains template code for the assignments in the course. It will additionally serve as an _upstream repository_ to source potential updates and corrections for the assignments.

Generally, each assignment will operate off of its own _branch_ while the _main_ branch will include the base template for an operational environment.

## Choosing an environment

Before cloning this repo, decide what kind of development environment you'd like to work from. Generally, you have three options:

1. A cloud-based "Dev Container" setup in GitHub Codespaces
   _Choose this option if you have a fast and stable internet connection and like the idea of a 1-click setup_

2. A local Dev Container-based setup
   _Choose this if you want the convenience of 1-click setup while working from a local copy of your code. Working this way might require you to acquire some passing knowledge of how Docker containers work, but should still be relatively painless. Please create a discussion or issue if you are running into errors and stay tuned for more detail._

3. A completely local setup with manually installed development dependencies.
   _Choose this option if you are comfortable with installing and configuring development dependencies on your own. This option will require you to install and configure one or more of the following dependencies at various points in the course:_

   - A recent version of Python (I prefer to use [pyenv](https://github.com/pyenv/pyenv) to manage my Python installations).
   - The [poetry](https://python-poetry.org/) package manager.
   - The [pre-commit](https://pre-commit.com/) framework for managing git hooks.
   - The [black](https://github.com/psf/black) code formatter.
   - The [ruff](https://github.com/charliermarsh/ruff) linter.
   - A PostgreSQL database

### Cloning the repo and setting up your submission repo.

Once your development environment is properly setup, closely follow the instructions at [this Stack Overflow thread](https://stackoverflow.com/a/30352360/1526293).

A high-level overview of the mechanics of the above operations can be deduced from [this tutorial](https://devopscube.com/set-git-upstream-respository-branch/).
