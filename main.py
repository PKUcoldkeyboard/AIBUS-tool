import env_check
from configparser import ConfigParser
from selenium.webdriver.chrome.options import Options
from func import *
import warnings
import sys
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
    # driver_pjs = webdriver.PhantomJS(executable_path=sys_path(browser='phantomjs'))
    browser = 'chromedriver'
    driver = webdriver.Chrome(executable_path=sys_path(browser=browser))
    print(f"Driver {browser} is ready.")
    go('config.ini')
    driver.quit()