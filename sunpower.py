# Generated by Selenium IDE
#import pytest
import time
#import json
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import csv
#import glob
import os
import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas

current_date = datetime.datetime.today().strftime('%Y%m%d')
file = "/home/mbales/Downloads/" + current_date + "_538_ASILOMAR_WAY_UNIT_104_ENERGY.csv"
data = []
lastline = []

kwhprodcum = 0
kwhusecum = 0
kwhnetcum = 0
kwhprodcur = 0
kwhusecur = 0
kwhusenet = 0
colnames = ['per', 'perprod', 'perused', 'pernet', 'cumprod', 'cumused', 'cumnet']
#os.remove("/home/mbales/sunpower/images/fignet.jpeg")
#os.remove("/home/mbales/sunpower/images/figuse.jpeg")
#os.remove("/home/mbales/sunpower/images/figprod.jpeg")

class TestUntitled():
  def setup_method(self, method):
    options = Options()
    options.headless = True
    fp = webdriver.FirefoxProfile("/home/mbales/.mozilla/firefox/vbwrjuz8.default-release/")
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    self.driver = webdriver.Firefox(executable_path="/home/mbales/Downloads/geckodriver", capabilities=firefox_capabilities, firefox_profile=fp)#, options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("https://monitor.us.sunpower.com/")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("mtbales@fastmail.fm")
    self.driver.find_element(By.CSS_SELECTOR, ".view-password > .radius").click()
    self.driver.find_element(By.CSS_SELECTOR, ".view-password > .radius").send_keys("Rfs387Ax@")
    self.driver.find_element(By.CSS_SELECTOR, ".right").click()
    time.sleep(20)
    self.driver.find_element(By.CSS_SELECTOR, "#energy_mix_landscape .sp-dash-btn").click()
    time.sleep(20)
    self.driver.find_element(By.CSS_SELECTOR, ".sp-widget-item:nth-child(2) > section #sp-dots > span:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".make-blue a > .widget-settings-icons").click()
    #self.driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()
    #self.driver.find_element(By.CSS_SELECTOR, "#signout > div:nth-child(2)").click()
 
if __name__ == '__main__':
   testClass = TestUntitled()
   testClass.setup_method("")
   testClass.test_untitled()
   testClass.teardown_method("")
   with open(file, 'r') as csvfile:
     lastline = (csvfile.readlines()[-1])
   with open(file, 'r') as csvfile:
     delta = (csvfile.readlines()[-2])
   delta = delta.strip('\n')
   lastline = lastline.strip('\n')
   deltadata = delta.split(',')
   data = lastline.split(',')

   chartdata = pandas.read_csv(file, names=colnames)
   col_a = list(chartdata.per)
   col_b = list(chartdata.perprod)
   print(col_a[2:13])
   print(col_b[2:13])
   figtest = px.bar(x=col_a, y=col_b)
   figtest.write_image("/home/mbales/sunpower/images/figtest.jpeg", width=960, height=540)
   figtest.show()


   #for row in reversed(list(csv.reader(csvfile, delimiter=","))):
       #print(', '.join(row))
   os.remove(file)
   #print(lastline)
   kwhprodcum = (float(data[4]))
   kwhusecum = (float(data[5]))
   kwhnetcum = (float(data[6]))
   deltakwhprodcum = (float(deltadata[4]))
   deltakwhusecum = (float(deltadata[5]))
   deltakwhnetcum = (float(deltadata[6]))


   fignetcum = go.Figure(go.Indicator(
       mode="number+delta",
       value=kwhnetcum,
       number={"font": {"size": 200}},
       delta={'position': 'top', 'reference': deltakwhnetcum},
       domain={'x': [1, 0], 'y': [0, 1]},
       title={'text': "Cumulative Daily kWh Net"}))


   figusecum = go.Figure(go.Indicator(
       mode="number+delta",
       value=kwhusecum,
       number={"font": {"size": 200}},
       delta={'position': 'top', 'reference': deltakwhusecum},
       domain={'x': [0, 1], 'y': [0, 1]},
       title={'text': "Cumulative Daily kWh Used"}))

   figprodcum = go.Figure(go.Indicator(
       mode="number+delta",
       value=kwhprodcum,
       number={"font": {"size": 200}},
       delta={'position': 'top', 'reference': deltakwhprodcum},
       domain={'x': [0, 1], 'y': [0, 1]},
       title={'text': "Cumulative Daily kWh Generated"}))

   fignetcum.write_image("/home/mbales/sunpower/images/fignet.jpeg", width=960, height=540)
   #fignetcum.show()

   figusecum.write_image("/home/mbales/sunpower/images/figuse.jpeg", width=960, height=540)
   #figusecum.show()

   figprodcum.write_image("/home/mbales/sunpower/images/figprod.jpeg", width=960, height=540)
   #figprodcum.show()