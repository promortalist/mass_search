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
#html_source = driver.page_source
#print (html_source)
#print(type(html_source))
#counter = 0
#max = 73
#while counter < max:
# counter2 = 0
# html_source = driver.page_source
# result = regexpHandler.findall(html_source)
# while counter2 < 500:
#      result2 = extURL.findall(result[counter2])
#      url = result2[0]
#      req = urllib.Request(url, headers={'User-Agent' : "Magic Browser"})
#      con = urllib.urlopen(req)
#      band = str(con.read())
#      bandname = regexBandName.findall(result[counter2])
#      th = str(bandf.findall(band))
#      genre =  genre_f.findall(band)
#      counter2 = counter2 + 1
#      if any(re.findall(r'Misanthropy|Nihilism|Anti-Christianity|Anti-christian|Blasphemy|Profanation|Profanity|Anti-Religion',th, re.IGNORECASE)):
#       print ("-----------------")
#       print ("Band: ", bandname)
#       print ("Genre: ", genre)
#       print ("Lyrical theme: ", th)
#       znalezione.write( "----------------------------------------------" +"\n")
#       znalezione.write( "Band: " +str(bandname)  +"\n")
#       znalezione.write( "Genre: " +str(genre)  +"\n")
#       znalezione.write( "Lyrical theme: " +str(th)  +"\n")
#      else:
#       c = 0
#i counter = counter + 1
#poleszukania =  driver.find_element_by_xpath('//*[@id="SimpleSearchForm_q"]')
#text_area = driver.find_element_by_id('textarea')
#text_area.send_keys("This text is send using Python code.")
olimpiada = open("olimpiada.txt")
znalezione = open('dostepne.txt', 'w')
for i in olimpiada.readlines():
#poleszukania.send_keys("Dyboski, R. Sto lat literatury angielskiej")
  poleszukania =  driver.find_element_by_xpath('//*[@id="SimpleSearchForm_q"]')
  poleszukania.clear()
  time.sleep(2)
  poleszukania.send_keys(i)
  poleszukania.submit()
  time.sleep(5)
#szukaj =  driver.find_element_by_xpath('//*[@id="btn-sub-top"]')
#szukaj = driver.find_element_by_id('btn-sub-top')
#szukaj = driver.find_element_by_xpath('//input[starts-with(@class,"bt]').click()
#szukaj.click()
#time.sleep(2)
#if driver.PageSource.Contains("Nie znaleziono") == 0:
  if "Nie znaleziono" in driver.page_source:
     print ("nie ma")
  else:    
     print ("Znaleziono: "+i)
     znalezione.write(i+"\n")
