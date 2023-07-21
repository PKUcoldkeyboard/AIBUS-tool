from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import warnings
warnings.filterwarnings('ignore')

def login(driver, username, password, retry=0):
    if retry == 3:
        raise ValueError('login failed.')
    
    print('login...')
    url = 'https://i.aibusx.com/pages/login'
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/div/form/button')))
    driver.find_element_by_id('email').send_keys(username)
    time.sleep(0.1)
    driver.find_element_by_id('auth-login-password').send_keys(password)
    time.sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div/form/button').click()
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div/div/div/button[2]')))
        print('login succesfully.')
    except:
        print('Retrying...')
        login(driver, username, password, retry+1)
        
        
# 签到
def checkin(driver):
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div/div/div/button[2]').click()
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located()
        print('签到成功！')
    except:
        print('签到失败！')

def run(driver, username, password):
    login(driver, username, password)
    checkin(driver)
    
if __name__ == '__main__':
    pass