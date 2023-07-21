import env_check
from configparser import ConfigParser
from selenium import webdriver
from func import *
import warnings
import sys
import os
warnings.filterwarnings('ignore')

def sys_path(browser):
    path = f'./{browser}/bin/'
    if sys.platform.startswith('win'):
        return path + f'{browser}.exe'
    elif sys.platform.startswith('linux'):
        return path + f'{browser}-linux'
    elif sys.platform.startswith('darwin'):
        return path + f'{browser}'
    else:
        raise OSError('Unknown OS Type')
    
def go(config):
    conf = ConfigParser()
    conf.read(config, encoding='utf-8')
    username, password = dict(conf['login']).values()
    
    run(driver, username, password)

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = './chromedriver/bin/chromedriver.exe'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
    print(f"Chromedriver is ready.")
    go('config.ini')
    driver.quit()