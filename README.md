<h1>Web-BruteForce</h1>
Launch a brute force attack over a web page with Selenium and Python.


<h2>Installation</h2>
<p aling="justify">Check the version of your broswer and download the <a href="https://selenium-python.readthedocs.io/installation.html#drivers">driver</a>. Got to "File", "Settings..." pycharm subdirectory and select "selenium" as interpreter. Now your python code can run Selenium. The next step consists to install a web page to attack. Launch a <a href="http://isoredirect.centos.org/centos/7/isos/x86_64/">Centos</a> image on <a href="https://www.virtualbox.org/">VirtualBox</a> and install an apache server with PHP using Ansible. The file <a href="https://github.com/MartiMarch/Ansible/blob/main/html-php.yml">html-php.yml</a> describe via comments how to do it.</p>  
<h2>Description</h2>
<p align="justify">The prupose of this repository is explain how is possible to launch a brute force attack over web page generating all the permutations using a list of chars and Selenium.<p>
  
<p align="justify">There are two fundamentals stpes. The first step consits on create all the possible permutations. To do it i have used a default python function named "permutations", it's inside of itertools. The function work efficiently so i don't take any effort optimitzation it a bit. However, if you want to know more about it the implementation of th function is the next:</p>

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
