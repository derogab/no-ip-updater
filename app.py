#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import schedule
import requests

from dotenv import load_dotenv
from datetime import datetime

# Load environments from .env
load_dotenv()

# Enable debug
DEBUG = os.environ.get('ENABLE_DEBUG')

def update_ip():
    # Get current time
    date = datetime.now()
    # Get the No-IP credentials
    USER = os.getenv('NOIP_USER')
    PASSWORD = os.environ.get('NOIP_PASSWORD')
    HOSTNAME = os.environ.get('NOIP_HOSTNAME')
    # Check if the credentials are set
    if not USER or not PASSWORD or not HOSTNAME:
        print('[ERROR] No-IP credentials are not set.')
        return
    # Log
    if DEBUG:
        print('[DEBUG] Auth: ', HOSTNAME, '/', USER)
    # Try to get the IP and update the data on No-IP
    try:
        # Get the public ip
        r = requests.get('https://api.ipify.org/?format=json')
        ip = r.json()['ip']
        # Update
        r = requests.get("https://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(USER, PASSWORD, HOSTNAME, ip))
        # Log
        print('[INFO] IP (' + str(ip) + ') updated at ' + str(date))
    except e:
        print('[ERROR] ', e)

def main():
    # Get the frequency
    MINUTES = os.getenv('FREQUENCY_MINUTES')
    # Set default frequency if custom is not set
    if not MINUTES:
        MINUTES = 15
        print('[WARN] Custom frequency is not set. Setting default (15).')
    # Convert to integer
    MINUTES = int(MINUTES)
    # Log the frequency
    print('[INFO] Ready to update every ', str(MINUTES), ' minute(s).')
    # Cron Tab
    schedule.every(MINUTES).minutes.do(update_ip)
    # App started
    print('[INFO] App started.')
    # Run the script
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()