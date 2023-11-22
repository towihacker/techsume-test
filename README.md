# Techsume
Techsume's official GITHUB!

# Required Installations

## Python3

### MacOS

Downloading Python3 needs Homebrew

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

Now insert Homebrew directory on your PATH environment variable to start using it

`export PATH="/usr/local/opt/python/libexec/bin:$PATH"`

If you have OS X 10.12 (Sierra) or older

`export PATH=/usr/local/bin:/usr/local/sbin:$PATH`

Now install Python3

`brew install python`

Then check if Python3 is working on your system

`python3 --version`

## Python3-PIP

Download PIP from their website using curl command

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

Now install downloaded packages from PIP

`python3 get-pip.py`

Then check if PIP is working

`pip --version`

## Flask

Install flask and its required modules

`pip3 install flask flask_login flask_bcrypt flask_wtf wtforms email_validator`

# git basics: https://www.atlassian.com/git

Do this before changing something or pushing your changes

`git pull`

To check the status if you have changed something

`git status`

To add all changed files to a commit

`git add .`

To make a commit - yourmessage can be anything straightforward to what you did

`git commit -m "yourmessage"`

To make a push to the Github repository (updating files in Github)

`git push`

If it is asking you to login

`git config --global user.name "your-github-username"`

`git config --global user.email "your-github-email"`
