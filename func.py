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
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, ':r1:')))
        print('login succesfully.')
    except:
        print('Retrying...')
        login(driver, username, password, retry+1)
        
        
# 签到
def checkin(driver):
    try:
        driver.find_element_by_id(':r1:').click()
        print('签到成功！')
    except Exception as e:
        print('签到失败！')
        print(e)
        

def run(driver, username, password):
    login(driver, username, password)
    checkin(driver)
    
if __name__ == '__main__':
    pass