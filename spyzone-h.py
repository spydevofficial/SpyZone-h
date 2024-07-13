import requests
import re
import os
import sys
import platform
from colorama import Fore, Style, init

init(autoreset=True)
fg = [
    '\033[91;1m',  # red 0
    '\033[92;1m',  # green 1
    '\033[93;1m',  # yellow 2
    '\033[94;1m',  # blue 3
    '\033[95;1m',  # magenta 4
    '\033[96;1m',  # cyan 5
    '\033[97;1m'  # white 6
]

user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

url = "http://www.zone-h.org/archive/notifier="
urll = "http://zone-h.org/archive/published=0"

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
        os.system('color a')


def banner():
    clear()
    print('''              
        
        {0}  _____             ______                       _    _ 
        {0} / ____|           |___  /                      | |  | |
        {1}| (___  _ __  _   _   / / ___  _ __   ___ ______| |__| |
        {1} \___ \| '_ \| | | | / / / _ \| '_ \ / _ \______|  __  |
        {2} ____) | |_) | |_| |/ /_| (_) | | | |  __/      | |  | |
        {2}|_____/| .__/ \__, /_____\___/|_| |_|\___|      |_|  |_|
        {3}       | |     __/ |                                    
        {3}       |_|    |___/  channel : @spydev_channel                                                
       {2}\━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━/
       \t├╼ {3}BY : spydev{2}
       \t└╼ {3}Zone-h Grabber
    \033[0m'''.format(fg[1], fg[0], fg[5], fg[3]))


def get_cookies():
    zhe = input("Please Enter your ZHE: ")
    phpsessid = input("Please Enter your PHPSESSID: ")
    return {
        "ZHE": zhe,
        "PHPSESSID": phpsessid
    }


def zonehgrabber(cookie):
    print("\n  [1] Grabb Sites By Notifier")
    print("  [2] Grabb Sites By Onhold")
    sec = int(input("Option: "))
    if sec == 1:
        var1 = input("Enter notifier: ")

        for i in range(1, 51):
            var2 = requests.get(url + var1 + "/page=" + str(i), cookies=cookie)
            var3 = var2.content
            print("Grab From" + url + var1 + "/page=" + str(i))
            if b'<html><body>-<script type="text/javascript"' in var3:
                print("False Cookies!")
                sys.exit()
            elif b'<input type="text" name="captcha" value=""><input type="submit">' in var3:
                print("Verify The Captcha In Zone-H!")
                sys.exit()
            else:
                rgio_urls = re.findall(b'<td>(.*)\n							</td>', var3)
                if b'/mirror/id/' in var3:
                    for rgioo in rgio_urls:
                        drq0 = rgioo.replace(b'...', b'')
                        print('    [' + '+' + '] ' + drq0.split(b'/')[0].decode())
                        with open(var1 + '.txt', 'a') as rr:
                            rr.write("http://" + drq0.split(b'/')[0].decode() + '\n')
                else:
                    print("Grab Sites completed")
                    sys.exit()

    elif sec == 2:
        for sssss in range(1, 51):
            qie = requests.get(urll + "/page=" + str(sssss), cookies=cookie)
            var5 = qie.content

            if b'<html><body>-<script type="text/javascript"' in var5:
                print("False Cookies!")
                sys.exit()

            elif b"captcha" in var5:
                print("Verify The Captcha In Zone-H!")
            else:
                rgio_urlss = re.findall(b'<td>(.*)\n							</td>', var5)
                for rgioox in rgio_urlss:
                    drqqq = rgioox.replace(b'...', b'')
                    print('    [' + '+' + '] ' + drqqq.split(b'/')[0].decode())
                    with open('onhold_zone.txt', 'a') as rrr:
                        rrr.write("http://" + drqqq.split(b'/')[0].decode() + '\n')
    else:
        print("Error!")


def drrgio():
    banner()
    cookies = get_cookies()
    zonehgrabber(cookies)


drrgio()
