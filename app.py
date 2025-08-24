#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import logging
import schedule
import requests

from dotenv import load_dotenv
from datetime import datetime

# Set up logging
DEBUG = os.getenv('ENABLE_DEBUG')
logging_level = logging.DEBUG if DEBUG == "1" or DEBUG.lower() == "true" else logging.INFO
logging.basicConfig(format="%(asctime)s\t%(levelname)s\t%(message)s", datefmt='%Y-%m-%d %H:%M:%S', level=logging_level)
logger = logging.getLogger(__name__)

# Load environments from .env
load_dotenv()

# Update the IP address on No-IP
def update_ip():
    # Get current time
    date = datetime.now()
    # Get the No-IP credentials
    USER = os.getenv('NOIP_USER')
    PASSWORD = os.getenv('NOIP_PASSWORD')
    HOSTNAME = os.getenv('NOIP_HOSTNAME')
    # Check if the credentials are set
    if not USER or not PASSWORD or not HOSTNAME:
        logger.error('No-IP credentials are not set.')
        return
    # Log
    logger.debug('No-IP Auth: ' + HOSTNAME + '/' + USER)
    # Try to get the IP and update the data on No-IP
    try:
        # Get the public ip
        r = requests.get('http://ipv4.iplocation.net')
        ip = r.json()['ip']
        # Update
        r = requests.get("https://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(USER, PASSWORD, HOSTNAME, ip))
        # Log
        logger.info('IP (' + str(ip) + ') updated.')
    except Exception as e:
        logger.error('Error: ' + e)

# Main function
def main():
    # Get the frequency
    MINUTES = os.getenv('FREQUENCY_MINUTES')
    # Set default frequency if custom is not set
    if not MINUTES:
        MINUTES = 15
        logger.warning('Custom frequency is not set. Setting default (15).')
    # Convert to integer
    MINUTES = int(MINUTES)
    # Log the frequency
    logger.info('Ready to update every ' + str(MINUTES) + ' minute(s).')
    # Cron Tab
    schedule.every(MINUTES).minutes.do(update_ip)
    # App started
    logger.debug('App started.')
    # First run at startup
    update_ip()
    # Run the script
    while True:
        schedule.run_pending()
        time.sleep(1)

# Run the script
if __name__ == "__main__":
    main()