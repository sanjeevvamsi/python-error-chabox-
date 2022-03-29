import time
import pyautogui
from selenium import webdriver

search = ''

def open_chrome(get_data):
    
    search = get_data + ' python stackoverflow '
    
    if len(get_data) == 0:
        return 'please enter data'

    else:
        return run_chrome(search)
       
def run_chrome(search):
    
   driver = webdriver.Chrome("C:/Users/rajaa/Desktop/projects/Python_ErrorSolver/chromedriver.exe")
   driver.get('https://www.google.com')
   time.sleep(1)
   driver.maximize_window()
   time.sleep(3)
   pyautogui.click(x=281, y=68)
   pyautogui.write(search)
   time.sleep(1)
   pyautogui.press('enter')

   return 'chrome is open'