# SP23 Assignments

This repository contains template code for the assignments in the course. It will additionally serve as an _upstream repository_ to source potential updates and corrections for the assignments.

Generally, each assignment will operate off of its own _branch_ while the _main_ branch will include the base template for an operational environment.

## Choosing an environment

Before cloning this repo, decide what kind of development environment you'd like to work from. Generally, you have three options:

### 1. A cloud-based "Dev Container" setup in GitHub Codespaces (Default IDE: VS Code, compatible with PyCharm)
   
   *Choose this option if you have a fast and stable internet connection and like the idea of a 1-click setup (including Poetry installation!)*

   #### Basic Steps

   1. Click "Create a Codespace on main" from the big green "Code" button at the top of the repo.
   
   That's pretty much it. Wait for the environment to build and for your startup commands to execute until you are greeted with a terminal prompt.

### 2. A local Dev Container-based setup (Default IDE: VS Code, compatible with PyCharm)
   
   *Choose this if you want much of the convenience of a 1-click setup while working from a local copy of your code. Working this way might requires installing a few basic dependencies and may at times require you to acquire some passing knowledge of how Docker containers work, but this method should still be pretty painless. Please create a discussion or issue if you are running into errors and stay tuned for more details on containers.*

   #### Basic Steps

   1. Install Docker Desktop
   2. Install VS Code
   3. Install the Dev Container extension for VS Code. the Clone the repo. 
   4. Open the repo in VS Code
   5. Click the "Reopen in Container" button that pops up.
      - If you miss the window of opportunity for the button, find the "Dev Containers: Reopen in Container" option from the command palette.

### 3. A completely local setup with manually installed development dependencies.
   
   *Choose this option if you want/require fine-grained control of your environment and are comfortable with installing and configuring development dependencies on your own or would like to challenge yourself to do so. This option will require you to install and configure one or more of the following dependencies at various points in the course:*

   - A recent version of Python (I prefer to use [pyenv](https://github.com/pyenv/pyenv) to manage my Python installations).
   - The [poetry](https://python-poetry.org/) package manager.
   - The [pre-commit](https://pre-commit.com/) framework for managing git hooks.
   - The [black](https://github.com/psf/black) code formatter.
   - The [ruff](https://github.com/charliermarsh/ruff) linter.
   - A PostgreSQL database

   Post in Discussions if you have any questions or run into any problems on your own.

## Cloning the repo and setting up your submission repo.

Once your development environment is properly set up, follow these instructions, modified from [this Stack Overflow thread](https://stackoverflow.com/a/30352360/1526293), carefully. 

1. Create a private repo named as your WUSTL username in the `wustl-data` GitHub Organization.
   - Don't add a README or .gitignore just yet.
2. Run:
```shell
# clone the template repo
git clone --bare https://github.com/wustl-data/sp23-assignments 

# move your *current directory* to the cloned repo's folder
cd sp23-assignments

# push a version of the repo to your private repo
git push --mirror https://github.com/wustl-data/<your wustl username>

# go back to your original working directory
cd .. 

# delete your local version of the template repo
rm -rf 

# clone the repo locally again from your private repo
git clone https://github.com/wustl-data/<your wustl username> 

# Change your current directory to your local copy of the repo, now in a different folder
cd <your wustl username>

# Add the template repo as an remote repo named 'upstream'
git remote add upstream https://github.com/wustl-data/sp23-assignments
```



You should name your repository with your WUSTL ID, and you should create your private repository within the `wustl-data` organization. Do not add a README or .gitignore from the GitHub UI.

A high-level overview of the mechanics of the above operations can be deduced from [this tutorial](https://devopscube.com/set-git-upstream-respository-branch/).
