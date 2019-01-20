# Computer Setup

## Install Python

1. [Download Python](https://www.python.org/downloads/)
1. Follow the installation, and use all of the defaults

## Install GIT

1. [Download Git](https://git-scm.com/downloads)
1. Once Git is installed

### Configure Git

1. Set user name
    ```bash
    git config --global user.name "Your Name"
    ```
1. Set email address
    ```bash
    git config --global user.email "your_email@example.com"
    ```
1. To check the configuration  
    ```bash
    git config --edit --global
    ```

## Install Visual Studio Code

1. [Download VS Code](https://code.visualstudio.com/)

## Create GitHub account

1. Create account with your email address
1. Verify account
1. Create SSH keys
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
1. [Add the SSH key to your GitHub account.](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
1. Use the SSH connection string to connect

## Go through GitHub Tutorial

1. [GitHub Guide](https://guides.github.com/activities/hello-world/)
