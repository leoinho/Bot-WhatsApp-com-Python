from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

message_text='Boa noite! Como posso ajudar?' # message
no_of_message=1 # no. of time 
moblie_no_list=[5521998505047,5521998505047] # list of phone number 

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10) #wait time to scan the code in second

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switchTo().alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :"+str(phone_no))

def escuta():
   texto = driver.find_element_by_class_name("_3zb-j ZhF0n")
   print(texto)
        
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)
        escuta()

    except Exception as e:
        sleep(10)
        is_connected()
        escuta()
