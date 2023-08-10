import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

def create_folder(token, path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    header = {'Authorization': token}
    params = {'path': path}
    return requests.put(url=url, headers=header, params=params)

def delete_folder(token, path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    header = {'Authorization': token}
    params = {'path': path, 'permanently': True}
    return requests.delete(url=url, headers=header, params=params)

def get_info(token, path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    header = {'Authorization': token}
    params = {'path': path}
    return requests.get(url=url, headers=header, params=params)