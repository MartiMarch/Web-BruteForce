<h1>Web-BruteForce</h1>
Launch a brute force attack over a web page with Selenium and Python.

<h2>Installation</h2>
<p aling="justify">Check the version of your broswer and download the <a href="https://selenium-python.readthedocs.io/installation.html#drivers">driver</a>. Got to "File", "Settings..." pycharm subdirectory and select "selenium" as interpreter. Now your python code can run Selenium. The next step consists to install a web page to attack. Launch a <a href="http://isoredirect.centos.org/centos/7/isos/x86_64/">Centos</a> image on <a href="https://www.virtualbox.org/">VirtualBox</a> and install an apache server with PHP using Ansible. The file <a href="https://github.com/MartiMarch/Ansible/blob/main/html-php.yml">html-php.yml</a> describe via comments how to do it.</p>  
<h2>Description</h2>
<p align="justify">The prupose of this repository is explain how is possible to launch a brute force attack over a web page generating all the permutations using a list of chars and Selenium.<p>
  
<p align="justify">There are two fundamentals stpes. The first step consits on create all the possible combinations. To do it i have used a default python function named "product", it's inside of itertools. The function work efficiently so i didn't take any effort to optimitze it. However, if you want to know more about the <a href="https://docs.python.org/3/library/itertools.html#itertools.permutations">implementation</a> here is the code:</p>

<pre>
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
</pre>
<br>
<p align="justify">The second step is send the petition to the web page. Selenium can search the input using the name of the input so the program only has to get the list of permutations and loop over it putting every element of the list as the password. If this is executed secuencialy it will take a lot of time so i parallelized the code using a queue (FIFO) with N threds. The parameters passed to the queue are the passwords and a random thread take it and launch the login petition.</p>
<img src="https://user-images.githubusercontent.com/82318419/138604360-af2bbb23-fb2e-4c8d-b198-ca4903a4337f.jpg"/>
<br>
<p align="justify">In conclusion, it's possible execute a brute force attack with Selenium, but it takes a lot of time. After a few searchs, i have decide to use the "mechanize" library. It also can be used to scrapping the web page and realize submit pettitions. After a changes on the code, it works better than selenium. Other important point is wich number of threads use. If you select a lower number of threads it don't use all the parralelition benefits, but if the number is higher it will increase the rescources of the pc without aport anything because they cant take any elemnt of the queue. After test some numbers of threads i think thath the optimal number is between 6 and 10, it can change in fuction of the computer. I would like take how much milliseconds take to found the correct password but i can't did it for the selected way used to stop the threads.</p>
<table>
  <tr>
    <th>
      VARIALBES
    </th>
  </tr>
  <tr>
    <td>
      URL
    </td>
    <td>
      URL of the web page
    </td>
  </tr>
  <tr>
    <td>
      CHARS
    </td>
    <td>
      Chars used to create the permutations
    </td>
  </tr>
  <tr>
    <td>
      USER
    </td>
    <td>
      User thath you want to hack
    </td>
  </tr>
  <tr>
    <td>
      PASS_LENG
    </td>
    <td>
      First length of the permutations
    </td>
  </tr>
  <tr>
    <td>
      N
    </td>
    <td>
      Number of threads
    </td>
  </tr>
</table>
<h2>How to prevent the brute force attack</h2>
<p align="justify">This type of attack need to scrap the web page so the mos popular options are just detect of any one is scrapping the web page. There are a lot of options:</p>
--> Put hidden elements that only the program will detect.<br>
--> Count the number of petitions of an IP.<br>
--> Detect a high volume of petitions on a specific section of the web page or URL.<br>
--> Use an AI to detect an irregular user pattern of conduction.<br><br>
<p align="justify">Of course, all this ideas are good but i wan to to think my personal solution. By my criteriuos the best way is just change the tags of all the elements when the HTML file is sended to the user. Th HTML file also has to be procesed by an ofuscator because it's possible automat the scrapping using the structure of the HTML. The problem of do it is that if there's for example a part of JavaScript code you need to validate the HTML file when the user send a POST or GET message, if not, a XSS attack could be raised. Just by this necessity of validate the HTML code is necessary to use a token or similar and save it into a database. If a list of conditions is given then the token will be deleted.</p>
