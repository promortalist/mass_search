from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
import re
import urllib.request as urllib
import time
opt = Options()
opt.headless = True
#plik = open("prof2.html","r")
#fragment = plik.readlines()
#string_fr = str(fragment)
regexpHandler = re.compile('<td class=" sorting_1">(.*?)</td>')
#result = regexpHandler.findall(string_fr)
#bandf = re.compile('<dt>Lyrical themes:</dt>\\\\n<dd>(.*?)</dd>')
#genre_f = re.compile('<dt>Genre:</dt>\\\\n<dd>(.*?)</dd>')
#extURL = re.compile('"(.*?)"')
#regexBandName = re.compile('">(.*?)</a>')
#max_counter = len(regexpHandler.findall(string_fr))
#znalezione = open("filtered_bands.txt","w")
driver = webdriver.Firefox(options=opt)
#driver = webdriver.Firefox()
driver.get("https://integro.ksiaznica.torun.pl/integro/catalog")
time.sleep(1)
olimpiada = open("olimpiada.txt")
znalezione = open('dostepne.txt', 'w')
for i in olimpiada.readlines():
  poleszukania =  driver.find_element_by_xpath('//*[@id="SimpleSearchForm_q"]')
  poleszukania.clear()
  time.sleep(2)
  poleszukania.send_keys(i)
  poleszukania.submit()
  time.sleep(5)
  if "Nie znaleziono" in driver.page_source:
     print ("nie ma")
  else:    
     print ("Znaleziono: "+i)
     znalezione.write(i+"\n")
