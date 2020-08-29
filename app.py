import os
import time
import schedule
import requests

from dotenv import load_dotenv
from datetime import datetime

# Load environments from .env
load_dotenv()

def update_ip():
    try:
        # Get the public ip
        r = requests.get('https://api.ipify.org/?format=json')
        ip = r.json()['ip']
        # Get current time
        date = datetime.now()
        # Get the No-IP credentials
        USER = os.getenv('NOIP_USER')
        PASSWORD = os.environ.get('NOIP_PASSWORD')
        HOSTNAME = os.environ.get('NOIP_HOSTNAME')
        # Update
        r = requests.get("https://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(USER, PASSWORD, HOSTNAME, ip))
        # Log
        print('[INFO] IP (' + str(ip) + ') updated at ' + str(date))
    except e:
        print('[ERROR] ', e)

def main():
    # Cron Tab
    schedule.every(15).minutes.do(update_ip)
    # App started
    print('[INFO] App started.')
    # Run the script
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()