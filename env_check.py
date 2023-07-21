# -*- coding: utf-8 -*-
import sys
import os

def env_check():
    if sys.version_info < (3, 6):
        raise OSError('Python 3.6 or higher is required.')
    
    try:
        import selenium
    except ImportError:
        raise ImportError('selenium is not installed. Try: pip3 install --user selenium')

    if not os.path.exists('config.ini'):
        raise ValueError('config.ini not found. Try: cp config.sample.ini config.ini')
    
    print('env_check passed.')
    return

env_check()