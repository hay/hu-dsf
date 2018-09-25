# Data science fundamentals cheatsheet

## Terminal commands
| command | use | example |
| ------- | --- | ------- |
| `ls` | List files in current directory | `ls` |
| | List files as a list | `ls -l` |
| `cd` | Change to directory | `cd Desktop` |
|  | Up one level in directory structure | `cd ..` |
| `mkdir` | Make a directory | `md pythoncode` |
| `pwd` | Print working directory | `pwd` |
| `touch` | Create a new empty file | `touch test.py` |
| `cat` | Print the contents of a file | `cat test.py` |
| `cp` | Copy one or more files | `cp test.py test2.py` |
| `mv` | Rename or move a file | `mv test2.py test3.py` |
| `rm` | Delete a file | `rm test3.py` |
| | Delete a directory | `rm -r pythoncode` |

### Terminal tips
* Try the TAB key to autocomplete your commands
* Use up and down arrow keys for previous / next commands
* Use CTRL-C to stop something

## Git commands
| command | use | example |
| ------- | --- | ------- |
| `git` | Prints most used `git` commands | `git` |
| `git init` | Create a new repository | `git init` |
| `git add` | Add a file to the repository | `git add test.py` |
| | Add all files in directory to repository | `git add .` |
| `git commit` | Commit changes to repository | `git commit -m "Your message here"` |
| `git clone` | Create a working copy of a repository | `git clone git@github.com:hay/hu-dsf.git` |
| `git status` | List changes in your working directory | `git status` |
| `git log` | List what happened in your repository | `git log` |