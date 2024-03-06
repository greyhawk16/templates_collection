"""
    더미
"""


import os
import csv
import re
import platform
import requests
import json
import hashlib

from dotenv import load_dotenv

# target_directory = input('Enter target directory: ')
load_dotenv()


def print_env():
    res = os.getenv("abc")
    return res

# target_directory = "./uploads"
# x = detect_webshell(target_directory) # specify the root directory of the web server
# print(x)
