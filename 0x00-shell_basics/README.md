# 0x00. Shell, basics
***
## This is a README.md for the repository
### 0x00. Shell, basics
```
For Holberton School
Cohort 16.
```
![Alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)
***
### General
* [What Is “The Shell”?](http://linuxcommand.org/lc3_lts0010.php)
* [Navigation](http://linuxcommand.org/lc3_lts0020.php)
* [Looking Around](http://linuxcommand.org/lc3_lts0030.php)
* [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
* [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
* [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)
* [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
* [Keyboard shortcuts for Bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
* [LTS](https://wiki.ubuntu.com/LTS)
* [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)

***
#### man or help
* `cd`
* `ls`
* `pwd` 
* `less`
* `file`
* `ln`
* `cp`
* `mv`
* `rm`
* `mkdir`
* `type`
* `which`
* `help`
* `man`

# Read or watch:

## General

* What does RTFM mean?
* What is a Shebang
## What is the Shell
* What is the shell
* What is the difference between a terminal and a shell
* What is the shell prompt
* How to use the history (the basics)
## Navigation
* What do the commands or built-ins cd, pwd, ls do
* How to navigate the filesystem
* What are the . and .. directories
* What is the working directory, how to print it and how to change it
* What is the root directory
* What is the home directory, and how to go there
* What is the difference between the root directory and the home directory of the user root
* What are the characteristics of hidden files and how to list them
* What does the command cd - do
## What do the commands ls, less, file do
* How do you use options and arguments with commands
* Understand the ls long format and how to display it
* A Guided Tour
* What does the ln command do
* What do you find in the most common/important directories
* What is a symbolic link
* What is a hard link
* What is the difference between a hard link and a symbolic link
## Manipulating Files
* What do the commands cp, mv, rm, mkdir do
* What are wildcards and how do they work
* How to use wildcards
## Working with Commands
* What do type, which, help, man commands do
* What are the different kinds of commands
* What is an alias
* When do you use the command help instead of man
## Reading Man Pages
* How to read a man page
* What are man page sections
* What are the section numbers for User commands, System calls and Library functions
## Keyboard Shortcuts for Bash
* Common shortcuts for Bash
## LTS
* What does LTS mean?
## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 20.04 LTS
* All your scripts should be exactly two lines long ($ wc -l file should print 2)
* All your files should end with a new line (why?)
* The first line of all your files should be exactly #!/bin/bash
* A README.md file at the root of the repo, containing a description of the repository
* A README.md file, at the root of the folder of this project, describing what each script is doing
* You are not allowed to use backticks, &&, || or ;
* All your scripts must be executable. To make your file executable, use the chmod command: chmod u+x file. Later, we’ll learn more about how to utilize this command.



# Extra resources around relational:

## More Info
* Example of line count and first line
```
julien@ubuntu:/tmp$ wc -l 12-file_type 
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type 
#!/bin/bash
julien@ubuntu:/tmp$ 
```

### More Info
In order to test your scripts, you will need to use this command: chmod u+x file. We will see later what does chmod mean and do, but you can have a look at man chmod if you are curious.

#### Example
```
julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$ 

```

## Files included

| File                 | Details                                    |
|--------------------- | ------------------------------------------ |
| [0-current_working_directory](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/0-current_working_directory) | Write a script that prints the absolute path name of the current working directory. |
| [1-listit](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/1-listit) | Display the contents list of your current directory.	       |
| [2-bring_me_home](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/2-bring_me_home) | Write a script that changes the working directory to the user’s home directory.	       |
| [3-listfiles](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/3-listfiles) | Display current directory contents in a long format	       |
| [4-listmorefiles](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/4-listmorefiles) |	Display current directory contents, including hidden files (starting with `.` ). Use the long format.       | 
| [5-listfilesdigitonly](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/5-listfilesdigitonly) | Display current directory contents.	       |
| [6-firstdirectory](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/6-firstdirectory) | Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.	       |
| [7-movethatfile](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/7-movethatfile) | Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.       |
| [8-firstdelete](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/8-firstdelete) | Delete the file betty.	       |
| [9-firstdirdeletion](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/9-firstdirdeletion) |        |
| [10-back](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/10-back) | Write a script that changes the working directory to the previous one.	       |
| [11-lists](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/11-lists) | Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.	       |
| [12-file_type](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/12-file_type) | Write a script that prints the type of the file name `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.	       |
| [13-symbolic_link](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/13-symbolic_link) | Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.	       |
| [14-copy_html](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/14-copy_html) | Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. You can consider that all HTML files have the extension `.html`|
| [100-lets_move](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/100-lets_move) | Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`. You can assume that the directory `/tmp/u` will exist when we will run your script 	       |
| [101-clean_emacs](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/101-clean_emacs) | Create a script that deletes all files in the current working directory that end with the character ~.	       |
| [102-tree](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/102-tree) | Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory. You are only allowed to use two spaces (and lines) in your script, not more.	       |
| [103-commas](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/103-commas) | Write a command that lists all the files and directories of the current directory, separated by commas (`,`).	       |
| [school.mgc](https://github.com/Juansepo13/holberton-system_engineering-devops/blob/main/0x00-shell_basics/school.mgc) | Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.	       |




### Author
***

## *Juan Sebastian Posada* - [*Github*](https://github.com/Juansepo13) - [*Twiter*](https://twitter.com/@JuanSeb35904130) 
### *Holberton School Student*