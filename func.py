from __future__ import annotations

import json
import time
import traceback
import warnings

from PIL import Image
from selenium.webdriver.common.by import By

from captcha import base64_api
from captcha import report_error
warnings.filterwarnings('ignore')


def login(driver, username, password, retry=0):
    if retry == 3:
        raise ValueError('login failed.')
    try:
        print('login...')
        url = 'https://www.aibusx.com/pages/login'
        driver.get(url)
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'MuiButton-sizeLarge')))
        time.sleep(3)
        driver.find_element(By.ID, 'email').send_keys(username)
        time.sleep(0.1)
        driver.find_element(By.ID, 'auth-login-password').send_keys(password)
        time.sleep(0.1)
        driver.find_elements(By.CLASS_NAME, 'MuiButton-sizeLarge')[0].click()
        print('login succesfully.')
    except Exception as e:
        print('Retrying...')
        login(driver, username, password, retry+1)

    time.sleep(3)


# 签到
def checkin(driver, retry=0):
    if retry == 3:
        raise ValueError('check in failed.')
    try:
        time.sleep(3)
        button = driver.find_elements(
            By.CLASS_NAME, 'MuiButton-textCheckinBtn')[0]
        print(button.get_dom_attribute('class'))
        # 检查button是否有效，可点击
        if button.is_enabled():
            button.click()
        else:
            raise RuntimeError('Button is disabled or not clickable')
        time.sleep(5)

        # 获取网页截图
        driver.save_screenshot('screenshot.png')

        window_size = driver.get_window_size()
        center_x = window_size['width'] / 2
        center_y = window_size['height'] / 2
        width = 150
        height = 50

        left = center_x - width / 2
        top = center_y - height
        right = center_x + width / 2
        bottom = center_y + 20

        # 裁剪验证码
        im = Image.open('screenshot.png')
        im = im.crop((int(left), int(top), int(right), int(bottom)))
        im.save('captcha.png')

        with open('apikey.json') as f:
            apikey = json.load(f)
        uname = apikey['username']
        pwd = apikey['password']
        captcha_id, captcha_code = base64_api(
            uname=uname, pwd=pwd, img='captcha.png', typeid=7)
        print(f'验证码答案：{captcha_code}')

        if not (captcha_code.isdigit() and 0 <= int(captcha_code) <= 18):
            report_error(captcha_id)
            raise ValueError('Answer not valid.')

        driver.find_element(
            By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/input').send_keys(captcha_code)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]').click()

        time.sleep(2)

        print('签到成功！')
    except Exception as e:
        print('签到失败！')
        traceback.print_exc()
        driver.refresh()
        checkin(driver, retry+1)


def run(driver, username, password):
    login(driver, username, password)
    checkin(driver)


if __name__ == '__main__':
    pass
