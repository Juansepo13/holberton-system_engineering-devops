# 0x0C. Web server
***
## This is a README.md for the repository
* 0x0C. Web server
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
* [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
* [Nginx](https://en.wikipedia.org/wiki/Nginx)
* [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
* [Child process concept page]()
* [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
* [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
* [HTTP redirection](https://moz.com/learn/seo/redirection)
* [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
* [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

## Read or watch:
* [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
* [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)

## Extra resources around relational:

### General
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests

### DNS
* What DNS stands for
* What is DNS main role

### DNS Record Types
* `A`
* `CNAME`
* `TXT`
* `MX`

### More Info

#### Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* You can???t use systemctl for restarting a process

## Files included

| File                 | Details                                    |
|--------------------- | ------------------------------------------ |
| [0-transfer_file]() |	Write a Bash script that transfers a file from our client to a server:  |
| [1-install_nginx_web_server]() | Web servers are the piece of software generating and serving HTML pages, let???s install one!	       |
| [2-setup_a_domain_name]() | .TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS. .TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your tools space. Feel free to drop a thank you tweet for .TECH Domains. Provide the domain name in your answer file.	       |
| [3-redirection]() |	Configure your Nginx server so that /redirect_me is redirecting to another page.       |
| [4-not_found_page_404]() |Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.	       |
| [5-design_a_beautiful_404_page]() |Note that if you decide to have your creative 404 page as the default one, make sure that it still contains the string Ceci n'est pas une page (otherwise the checker will fail your previous project). Submit the URL of your 404 page in the field bellow. Please, remember that these blogs must be written in English to further your technical ability in a variety of settings. It is your responsibility to request a review for this task from a peer before the project???s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.	       |
| [7-puppet_install_nginx_web_server.pp]() |Time to practice configuring your server with Puppet! Just as you did before, we???d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.	       |



### Author
***
*Holberton School Student*

Juan Sebastian Posada  - [Github](https://github.com/Juansepo13) - [Twiter](https://twitter.com/@JuanSeb35904130)s