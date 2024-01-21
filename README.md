# Official-Jokes-Test-Framework

## Overview

This is a basic framework developed using [pytest-bdd](https://github.com/pytest-dev/pytest-bdd). The purpose of this project is to verify that when users of the Official Jokes API want jokes of a specific type they get it! 

## Prerequisites

### Install Pyenv and Python

Before you can install pyenv on macOS you will need the XCode command line tools, which are installed via the following command:

```bash
xcode-select --install
```
pyenv builds Python from source, which means you’ll need build dependencies to actually use pyenv. I highly recommend using the package manager Homebrew to install those dependencies. if you need instructions on how to install homebrew you can find it [here](https://brew.sh):

```bash
brew install openssl readline sqlite3 xz zlib
```

Go ahead and install pyenv using homebrew by running the following: 

```bash
brew update
brew install pyenv
```
And after the installation has finished successfully, enter the following to add the pyenv to your $PATH and start pyenv when a new terminal window is opened (if you are not using zsh as a shell, you have to change ~/.zshrc accordingly):

```bash
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
```
Now that you have pyenv installed, installing Python is the next step. You have many versions of Python to choose from. If you want to see all the versions, you can do the following:

```bash
pyenv install --l
```
Once you find the version you want, you can install it with a single command, I recommend a python version > 3.7.x:

```bash
pyenv install [PYTHON_VERSION]
```

Now, after you installed a python version you can set a default Python version that is active when you open a new terminal, you use the global command:

```bash
pyenv global [PYTHON_VERSION]
```

### Create and Activate Virtual Environments
At this point you should have pyenv installed. Now you will need install pyenv-virtualenv to create and manage virtual environments. To install pyenv-virtualenv using homebrew run the following:

```bash
brew install pyenv-virtualenv
```
Next you will need to add pyenv-virtualenv initializer to shell startup script. (if you are not using zsh as a shell, you have to change ~/.zshrc accordingly):

```bash
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```

Now you can create virtual environments that use the same version of Python, but have their own set of pip installed packages by running the following from the root directory of the project:

```bash
pyenv virtualenv <python-version> <name>
```
- Example
    ```bash
    pyenv virtualenv 3.12.0 myproject
    ```
Now that you’ve created your virtual environment, using it is the next step. You can activate your environment by running the following from the root directory of the project:

```bash
pyenv local myproject
```

The preceding step should create a .python-version file in your current working directory and because you ran eval "$(pyenv virtualenv-init -)" in your environment, the environment will automatically be activated.

You can verify this by running the following:

```bash
pyenv which python
```

## Installation
- From the project root directory install the following packages
    - `pip install pytest`
    - `pip install pytest-bdd`
    - `pip install requests`

## Running Tests
To run all tests from the root directory, run `pytest`.
All the standard
[pytest command line options](https://docs.pytest.org/en/latest/usage.html)
work.
Use [command line options](http://behave.readthedocs.io/en/latest/behave.html)
for filtering and other controls.
Options may also be put inside the `pytest.ini`
[configuration file](https://docs.pytest.org/en/latest/reference.html#configuration-options).
Below are some common options:

```bash
# run all tests
pytest

# filter tests by test module
pytest tests/test_programming.py

# filter tests by tags
pytest -k "programming"
pytest -k "random"
pytest -k "tenJokes"
```