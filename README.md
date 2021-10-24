<h1>Web-BruteForce</h1>
Launch a brute force attack over a web page with Selenium and Python.


<h2>Installation</h2>
<p aling="justify">Check the version of your broswer and download the <a href="https://selenium-python.readthedocs.io/installation.html#drivers">driver</a>. Got to "File", "Settings..." pycharm subdirectory and select "selenium" as interpreter. Now your python code can run Selenium. The next step consists to install a web page to attack. Launch a <a href="http://isoredirect.centos.org/centos/7/isos/x86_64/">Centos</a> image on <a href="https://www.virtualbox.org/">VirtualBox</a> and install an apache server with PHP using Ansible. The file <a href="https://github.com/MartiMarch/Ansible/blob/main/html-php.yml">html-php.yml</a> describe via comments how to do it.</p>  
<h2>Description</h2>
<p align="justify">The prupose of this repository is explain how is possible to launch a brute force attack over web page generating all the permutations using a list of chars and Selenium.<p>
  
<p align="justify">There are two fundamentals stpes. The first step consits on create all the possible permutations. To do it i have used a default python function named "permutations", it's inside of itertools. The function work efficiently so i didn't take any effort to optimitze it. However, if you want to know more about it the <a href="https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list">implementation</a> of th function is the next:</p>

<pre>
def all_perms(elements):<br>
    if len(elements) <=1:<br>
        yield elements<br>
    else:<br>
        for perm in all_perms(elements[1:]):<br>
            for i in range(len(elements)):<br>
                # nb elements[0:1] works in both string and list contexts<br>
                yield perm[:i] + elements[0:1] + perm[i:]<br>
</pre>
<p align="justify">The second step is send the petition to the web page. Selenium can search the input using the name of the input so the program only has to get the list of permutations and loop it setting every elemnt of the list as the password. If this is xecuted secuencialy it will take a lot of time so i parrallelized the code using a queue (FIFO) with N threds./p>
