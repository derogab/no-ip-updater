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

def debug(*args):
    # Get debug value from .env
    DEBUG = os.getenv('ENABLE_DEBUG')
    # Check if debug is enabled
    if DEBUG == "1" or DEBUG.lower() == "true":
        # Log
        print("[DEBUG]", *args)

def update_ip():
    # Get current time
    date = datetime.now()
    # Get the No-IP credentials
    USER = os.getenv('NOIP_USER')
    PASSWORD = os.getenv('NOIP_PASSWORD')
    HOSTNAME = os.getenv('NOIP_HOSTNAME')
    # Check if the credentials are set
    if not USER or not PASSWORD or not HOSTNAME:
        print('[ERROR] No-IP credentials are not set.')
        return
    # Log
    debug('Auth: ', HOSTNAME, '/', USER)
    # Try to get the IP and update the data on No-IP
    try:
        # Get the public ip
        r = requests.get('http://ipv4.iplocation.net')
        ip = r.json()['ip']
        # Update
        r = requests.get("https://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(USER, PASSWORD, HOSTNAME, ip))
        # Log
        print('[INFO] IP (' + str(ip) + ') updated at ' + str(date))
    except Exception as e:
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
    # First run at startup
    update_ip()
    # App started
    print('[INFO] App started.')
    # Run the script
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()