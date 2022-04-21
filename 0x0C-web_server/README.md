# 0x0C. Web server
***
## This is a README.md for the repository
### 0x0C. Web server
```
For Holberton School
Cohort 16.
```
![imag1](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)
## General
In this project, some of the tasks will be graded on 2 aspects:

* Is your web-01 server configured according to requirements
* Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use emacs on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:
```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```
As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://www.atlassian.com/incident-management/devops/sre), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.

A good Software Engineer is a lazy [Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb)
![imag](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

## Resources

## Read or watch:

## Extra resources around relational:

*
*

### More Info

*
*

## Files included

| File                 | Details                                    |
|--------------------- | ------------------------------------------ |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |
| []() |	       |


### Author
***
*Holberton School Student*

Juan Sebastian Posada  - [Github](https://github.com/Juansepo13) - [Twiter](https://twitter.com/@JuanSeb35904130)s