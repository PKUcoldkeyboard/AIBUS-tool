from __future__ import annotations

import argparse
import warnings
from configparser import ConfigParser

from selenium import webdriver

import env_check
from func import *
warnings.filterwarnings('ignore')


def go(config):
    conf = ConfigParser()
    conf.read(config, encoding='utf-8')
    username, password = dict(conf['login']).values()

    run(driver, username, password)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AIBUS-tool')
    parser.add_argument('--driver_path', type=str, default='/usr/bin/chromedriver',
                        help='absolute path of your chromedriver or chromedrier.exe, \
                            default value=/usr/bin/chromedriver')
    args = parser.parse_args()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chromedriver = args.driver_path
    service = webdriver.ChromeService(executable_path=chromedriver)
    driver = webdriver.Chrome(options=chrome_options, service=service)
    print(f'Chromedriver is ready.')
    go('config.ini')
    driver.quit()
