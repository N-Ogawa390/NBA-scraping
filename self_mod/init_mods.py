from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import openpyxl as px
import time
import csv
import sys
from decimal import Decimal

br = webdriver.Firefox()
wt = WebDriverWait(br,10)

def wtpath(path):
    wt.until(ec.visibility_of_element_located((By.XPATH,path)))

def permission(text = '続けますか？\n『ok』or『no』：'):
    while True:
        gonext = input(text)
        if gonext == 'ok':
            break
        elif gonext == 'no':
            print('処理を終了します')
            br.close()
            br.quit()
            sys.exit()
