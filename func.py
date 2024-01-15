from __future__ import annotations

import time
import traceback
import warnings

from selenium.webdriver.common.by import By
warnings.filterwarnings('ignore')


def login(driver, username, password, retry=0):
    if retry == 3:
        raise ValueError('login failed.')

    print('login...')
    url = 'https://www.aibusx.com/pages/login'
    driver.get(url)
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'MuiButton-sizeLarge')))
    time.sleep(5)
    driver.find_element(By.ID, 'email').send_keys(username)
    time.sleep(0.1)
    driver.find_element(By.ID, 'auth-login-password').send_keys(password)
    time.sleep(0.1)
    driver.find_elements(By.CLASS_NAME, 'MuiButton-sizeLarge')[0].click()
    try:
        print('login succesfully.')
    except Exception as e:
        print('Retrying...')
        login(driver, username, password, retry+1)

    time.sleep(3)


# 签到
def checkin(driver):
    try:
        time.sleep(10)
        button = driver.find_elements(
            By.CLASS_NAME, 'MuiButton-textCheckinBtn')[0]
        print(button.get_dom_attribute('class'))
        # 检查button是否有效，可点击
        if button.is_enabled():
            button.click()
        else:
            raise RuntimeError('Button is disabled or not clickable')
        time.sleep(3)
        print('签到成功！')
    except Exception as e:
        print('签到失败！')
        traceback.print_exc()


def run(driver, username, password):
    login(driver, username, password)
    checkin(driver)


if __name__ == '__main__':
    pass
