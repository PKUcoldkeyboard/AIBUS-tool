from __future__ import annotations

import base64
import json

import requests


def base64_api(uname, pwd, img, typeid, retry=0):
    if retry == 3:
        raise ValueError('Validation API failed.')
    try:
        with open(img, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            b64 = base64_data.decode()
        data = {'username': uname, 'password': pwd,
                'typeid': typeid, 'image': b64}
        result = json.loads(requests.post(
            'http://api.ttshitu.com/predict', json=data).text)
        if result['success']:
            return result['data']['id'], result['data']['result']
        else:
            return None, result['message']

    except Exception as e:
        print('Retrying validating...')
        return base64_api(uname, pwd, img, typeid, retry+1)


def report_error(id):
    data = {'id': id}
    result = json.loads(requests.post(
        'http://api.ttshitu.com/reporterror.json', json=data).text)
    if result['success']:
        return '报错成功'
    else:
        return result['message']
