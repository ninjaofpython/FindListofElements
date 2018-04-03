from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class ListofElements():
   
    
    def test(self):
        baseURL = "https://www."
        driver = webdriver.Firefox()
        driver.get(baseURL)
        
        getElementByClassName = driver.find_elements_by_class_name("inputs")
        length = len(getElementByClassName)


        if getElementByClassName is not None:
           print("Size of the list is " + str(length))

        getElementListByTagName = driver.find_elements(By.TAG_NAME, "tr")
        length2 = len(getElementListByTagName)

        if getElementListByTagName is not None:
            print("Size of the list is: " + str(length2))
        
       
ff = ListofElements()
ff.test()
