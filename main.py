'''
main.py
created: 2025.04.10
author: WSD
for: bz30
'''

import time
import os
from pathlib import Path

import time
from datetime import datetime as dt
import random
import json
import re
from multiprocessing import Pool

from libs.lib_ozy import POLog, _print, line, dump, setconf
from colorama import Fore, Back, init
import art

init()
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


lg = POLog()
lg.logTime()
lg.logTime('Start.')
# lg.logTime('Start.', start_colr=color.GREEN)

setconf('print', False)
setconf('log', False)
setconf('logprint', False)

hendless=False
hendless=True
category='/category/sistemnye-bloki-15704/?page=7'
categoryPage = 0
categoryPage = 7
category=f'/category/sistemnye-bloki-15704/?page={categoryPage}'


title = (Fore.GREEN + 'start' + Fore.RESET)
_print(title)
title = 'OZY v0.1'
t = art.text2art(title, 'epic')
title = (Fore.GREEN + t + Fore.RESET)
print(title)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CrOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as FxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

from selenium_stealth import stealth
from fake_useragent import UserAgent
import pickle

lg.logTime('libs loaded')

# Select browser driver
way='f'
way='c'

url='https://www.ozon.ru/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094/';
# url='https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/artbuk-h-r-a-m-monohromnyy-uzhas-h-r-a-m-1173897628/?avtc=1&avte=2&avts=1719315501';
# url='https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/artbuk-h-r-a-m-monohromnyy-uzhas-h-r-a-m-1173897628/?avtc=1&avte=2&avts=1719315501';
# url='https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094?at=Z8tXKO0JEfmYmRkVtORRA3zHYGG8xgF95q5ZEtPJxmZo'
url='https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094'
url='https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094'
# url='https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094/'\
#     '?at=vQtrwMRQGcYX4GYJi84PZ38SLDrgZ1Inm60BJi8O8nw0&layout_container=BottomShelfs'\
#     '&layout_page_index=3'\
#     '&sh=OSLp7qRZ3A'\
#     '&start_page_id=1fc54c823b42e7221ebba9aa82b8dac5'
rootd = os.path.dirname(os.path.abspath(__file__))
chrWebDrivPath = os.path.join(rootd,'driver_chrome/chromedriver')
foxWebDrivPath = os.path.join(rootd,'driver_firefox/geckodriver')
# _print(chrWebDrivPath)

# webdkargs = {
#     'executable_path':chrWebDrivPath,
# }


# url='https://homdy.ru'
# url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# webdriver.CromeOptions()  
if way == 'c':options = CrOptions()
if way == 'f':options = FxOptions()
# _print(webdriver.Chrome.__doc__)


# service=type('WebDrive',(),{"path":chrWebDrivPath})
# _print(service)
# _print()

user_agents=[
    '1',
    '2',
    '3',
]

# options ====
# if hendless: options.headless = True
# options.add_argument('user-agent=HiWebDett')
if hendless:
    options.add_argument('--headless')
lg.logTime('started {} hendless'.format('as'if hendless else 'without'))
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
usag = UserAgent()
if way == 'c':
    # extension_path = "V:\\VISHESH AGRAWAL\\Chrome Extension\\Word Counter"
    # __tests/po_py/ectensions/chr_ext_001/popup.js
    extension_path = os.path.dirname(os.path.realpath(__file__))+'/ectensions/chr_ext_001/'
    options.add_argument("load-extension=" + extension_path)
    # options.add_argument(f'user-agent={usag.random}')
    ua='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    options.add_argument(f'user-agent={ua}')
    options.add_argument(f'--disable-blink-features=AutomationControlled')
usag = UserAgent()
if way == 'f':
    options.set_preference('general.useragent.override', usag.random)
    options.set_preference('dom.webdriver.enabled', False)
# options.add_argument(f'user-agent={random.choice(user_agents)}')
try:
    driver = None
    if way == 'c':
        # options.binary_location=chrWebDrivPath
        # _print(list(options))
        # _print(chrWebDrivPath)
        lg.logTime('used Chrome')
        # options.add_argument('--user-agent')
        # driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome(options=options,executable_path=chrWebDrivPath)
        # driver = webdriver.Chrome(options=options,executable_path=chrWebDrivPath)
        driver = webdriver.Chrome(service=Service(executable_path=chrWebDrivPath), options=options)
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # driver = webdriver.Chrome(service=type('',(),{"path":chrWebDrivPath}))
    if way == 'f':
        lg.logTime('used Firefox')
        # _print(list(options))
        # driver = webdriver.Firefox( options=options)
        driver = webdriver.Firefox(service=FirefoxService(executable_path=foxWebDrivPath), options=options)
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        # driver = webdriver.Firefox(service=Service(ChromeDriverManager().install()), options=options)
        # driver = webdriver.Firefox(foxWebDrivPath)

except Exception as ex:
    _print(ex)
    lg.logTime('driver error: '+str(ex))
    lg.logTime('Finish.')
    lg.end()   
    exit()

lg.logTime('driver created')

# ! error kwargs
# driver = webdriver.Chrome(executable_path=chrWebDrivPath)
# driver = webdriver.Chrome(**webdkargs)
# try:
#     ...
# except Exception as ex:
#     _print(ex)
# finally:
#     driver.close()
#     driver.quit()

'''
get_screenshot_as_file('file.png')
save_screenshot('file2.png')
'''

if way == 'c':
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver.quit()

        lg.logTime('driver exit')

    def __aenter__(self):
        return self.driver

    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver.quit()



cook2=[{
"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
"accept-encoding": 'gzip, deflate, br',
"accept-language": 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
"cache-control": 'no-cache',
"pragma": 'no-cache',
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
"sec-ch-ua-arch": "x86",
"sec-ch-ua-bitness": "64",
"sec-ch-ua-full-version": "96.0.4664.45",
"sec-ch-ua-mobile": '?0',
"sec-ch-ua-model": "",
"sec-ch-ua-platform": "Linux",
"sec-ch-ua-platform-version": "5.15.0",
"sec-fetch-dest": 'document',
"sec-fetch-mode": 'navigate',
"sec-fetch-site": 'none',
"sec-fetch-user": '?1',
"service-worker-navigation-preload": 'true',
"upgrade-insecure-requests": 1,
"user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}]
# cook2 = json.load(cook2)

'__Secure-ab-group=60; xcid=e6f1ddbf8a6eca300b1123bab4b38461; ADDRESSBOOKBAR_WEB_CLARIFICATION=1744154153; rfuid=NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxOTg5NTUxNDI1LC0xLC0zNjI5NDkyMzIsVzNzaWJtRnRaU0k2SWxCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxbElGQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMXBkVzBnVUVSR0lGWnBaWGRsY2lJc0ltUmxjMk55YVhCMGFXOXVJam9pVUc5eWRHRmliR1VnUkc5amRXMWxiblFnUm05eWJXRjBJaXdpYldsdFpWUjVjR1Z6SWpwYmV5SjBlWEJsSWpvaVlYQndiR2xqWVhScGIyNHZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlN4N0luUjVjR1VpT2lKMFpYaDBMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4xZGZTeDdJbTVoYldVaU9pSk5hV055YjNOdlpuUWdSV1JuWlNCUVJFWWdWbWxsZDJWeUlpd2laR1Z6WTNKcGNIUnBiMjRpT2lKUWIzSjBZV0pzWlNCRWIyTjFiV1Z1ZENCR2IzSnRZWFFpTENKdGFXMWxWSGx3WlhNaU9sdDdJblI1Y0dVaU9pSmhjSEJzYVdOaGRHbHZiaTl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOUxIc2lkSGx3WlNJNkluUmxlSFF2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZWMTlMSHNpYm1GdFpTSTZJbGRsWWt0cGRDQmlkV2xzZEMxcGJpQlFSRVlpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgxZCxXeUp5ZFMxU1ZTSmQsMCwxLDAsMjQsMjM3NDE1OTMwLDgsMjI3MTI2NTIwLDEsMSwwLC0xLFIyOXZaMnhsSUVsdVl5NGdUbVYwYzJOaGNHVWdSMlZqYTI4Z1RHbHVkWGdnZURnMlh6WTBJRFV1TUNBb1dERXhPeUJNYVc1MWVDQjRPRFpmTmpRcElFRndjR3hsVjJWaVMybDBMelV6Tnk0ek5pQW9TMGhVVFV3c0lHeHBhMlVnUjJWamEyOHBJRU5vY205dFpTODVOaTR3TGpRMk5qUXVORFVnVTJGbVlYSnBMelV6Tnk0ek5pQXlNREF6TURFd055Qk5iM3BwYkd4aCxleUpqYUhKdmJXVWlPbnNpWVhCd0lqcDdJbWx6U1c1emRHRnNiR1ZrSWpwbVlXeHpaU3dpU1c1emRHRnNiRk4wWVhSbElqcDdJa1JKVTBGQ1RFVkVJam9pWkdsellXSnNaV1FpTENKSlRsTlVRVXhNUlVRaU9pSnBibk4wWVd4c1pXUWlMQ0pPVDFSZlNVNVRWRUZNVEVWRUlqb2libTkwWDJsdWMzUmhiR3hsWkNKOUxDSlNkVzV1YVc1blUzUmhkR1VpT25zaVEwRk9UazlVWDFKVlRpSTZJbU5oYm01dmRGOXlkVzRpTENKU1JVRkVXVjlVVDE5U1ZVNGlPaUp5WldGa2VWOTBiMTl5ZFc0aUxDSlNWVTVPU1U1SElqb2ljblZ1Ym1sdVp5SjlmU3dpY25WdWRHbHRaU0k2ZXlKUGJrbHVjM1JoYkd4bFpGSmxZWE52YmlJNmV5SkRTRkpQVFVWZlZWQkVRVlJGSWpvaVkyaHliMjFsWDNWd1pHRjBaU0lzSWtsT1UxUkJURXdpT2lKcGJuTjBZV3hzSWl3aVUwaEJVa1ZFWDAxUFJGVk1SVjlWVUVSQlZFVWlPaUp6YUdGeVpXUmZiVzlrZFd4bFgzVndaR0YwWlNJc0lsVlFSRUZVUlNJNkluVndaR0YwWlNKOUxDSlBibEpsYzNSaGNuUlNaWEYxYVhKbFpGSmxZWE52YmlJNmV5SkJVRkJmVlZCRVFWUkZJam9pWVhCd1gzVndaR0YwWlNJc0lrOVRYMVZRUkVGVVJTSTZJbTl6WDNWd1pHRjBaU0lzSWxCRlVrbFBSRWxESWpvaWNHVnlhVzlrYVdNaWZTd2lVR3hoZEdadmNtMUJjbU5vSWpwN0lrRlNUU0k2SW1GeWJTSXNJa0ZTVFRZMElqb2lZWEp0TmpRaUxDSk5TVkJUSWpvaWJXbHdjeUlzSWsxSlVGTTJOQ0k2SW0xcGNITTJOQ0lzSWxnNE5sOHpNaUk2SW5nNE5pMHpNaUlzSWxnNE5sODJOQ0k2SW5nNE5pMDJOQ0o5TENKUWJHRjBabTl5YlU1aFkyeEJjbU5vSWpwN0lrRlNUU0k2SW1GeWJTSXNJazFKVUZNaU9pSnRhWEJ6SWl3aVRVbFFVelkwSWpvaWJXbHdjelkwSWl3aVdEZzJYek15SWpvaWVEZzJMVE15SWl3aVdEZzJYelkwSWpvaWVEZzJMVFkwSW4wc0lsQnNZWFJtYjNKdFQzTWlPbnNpUVU1RVVrOUpSQ0k2SW1GdVpISnZhV1FpTENKRFVrOVRJam9pWTNKdmN5SXNJa3hKVGxWWUlqb2liR2x1ZFhnaUxDSk5RVU1pT2lKdFlXTWlMQ0pQVUVWT1FsTkVJam9pYjNCbGJtSnpaQ0lzSWxkSlRpSTZJbmRwYmlKOUxDSlNaWEYxWlhOMFZYQmtZWFJsUTJobFkydFRkR0YwZFhNaU9uc2lUazlmVlZCRVFWUkZJam9pYm05ZmRYQmtZWFJsSWl3aVZFaFNUMVJVVEVWRUlqb2lkR2h5YjNSMGJHVmtJaXdpVlZCRVFWUkZYMEZXUVVsTVFVSk1SU0k2SW5Wd1pHRjBaVjloZG1GcGJHRmliR1VpZlgxOWZRPT0sNjUsLTEyODU1NTEzLDEsMSwtMSwxNjk5OTU0ODg3LDE2OTk5NTQ4ODcsODM1OTM2NjM0LDI='


ADDRESSBOOKBAR_WEB_CLARIFICATION=int(time.time())+(365*86400)
ADDRESSBOOKBAR_WEB_CLARIFICATION=int(time.time())-(50*3600)

cook2={
    'abt_data':'7.iWq6ZJ5BOM8LktW0d5k7US_wuYpTuNxczY_dSZ3kHKyABU_Oe-9OFMJRaBo8Pit5Eu5GpuRdlrWncHempy70axaRMqYcJJGbE65pRSYIn5Qt8StjVEXEMMomrKdlHvkW5GSWYiy6fXH621HVSdtjq6QV8iNpZWeu8aNsM-HfxBNDdV9R5dm6YIqfN5Oisb6UuRWkDui_uVk608f8Gji9IiI6p6y_Rw7jsXmcT0cZyyi7BecEscO4ZYkhpdiH-LgOoL632WDI4X08BnDdtlc_iIUzccYxyFSZeI7ZvWP_N7M-bvXJr5lWC8mL7gHz9CVqIE-j2418wF2PGawKYZVyYT6tMh07sSr_qWYhfc6q8fyRx3Sae9uUCIOkofFGTSU7EvTSiEQKss8vXQsciTuGm29VOZwAxhdbg-EEFNZOrOA5MNLM6EcupSJCO-p1iOoLFr3MGrsj9wifg7JvgIjBBf-SBXPmYeG2yUf9',
    '__Secure-refresh-token':'7.0.Y6cGNICVQRmhC8DKgrLkPQ.60.ASnBFsuUyp5ZIIZcMeE_4d9u_Rn733S4Ez94hQnsnu8ZAJrE889nzRzW2OScVDiUNw..20250411005106.A0VvzhczfCuRbXWkpEb9oVygIBGjzwVNWTLzD1eYYQc.1e6ab2286534600ce',
    '__Secure-ETC':'d44e290d024bef62205d5e9287076c9d',
    # 'ADDRESSBOOKBAR_WEB_CLARIFICATION':'1744154153',
    'ADDRESSBOOKBAR_WEB_CLARIFICATION': str(ADDRESSBOOKBAR_WEB_CLARIFICATION),
    '__Secure-user-id':'0',
    '__Secure-ext_xcid':'e6f1ddbf8a6eca300b1123bab4b38461',
    '__Secure-access-token':'7.0.Y6cGNICVQRmhC8DKgrLkPQ.60.ASnBFsuUyp5ZIIZcMeE_4d9u_Rn733S4Ez94hQnsnu8ZAJrE889nzRzW2OScVDiUNw..20250411005106.h95BhVm-PAPfS5QndXAzUULVn_wUFhIpWwwq_LqbAgg.1a46ca17badb5de8',
    'rfuid':'NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxOTg5NTUxNDI1LC0xLC0zNjI5NDkyMzIsVzNzaWJtRnRaU0k2SWxCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxbElGQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMXBkVzBnVUVSR0lGWnBaWGRsY2lJc0ltUmxjMk55YVhCMGFXOXVJam9pVUc5eWRHRmliR1VnUkc5amRXMWxiblFnUm05eWJXRjBJaXdpYldsdFpWUjVjR1Z6SWpwYmV5SjBlWEJsSWpvaVlYQndiR2xqWVhScGIyNHZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlN4N0luUjVjR1VpT2lKMFpYaDBMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4xZGZTeDdJbTVoYldVaU9pSk5hV055YjNOdlpuUWdSV1JuWlNCUVJFWWdWbWxsZDJWeUlpd2laR1Z6WTNKcGNIUnBiMjRpT2lKUWIzSjBZV0pzWlNCRWIyTjFiV1Z1ZENCR2IzSnRZWFFpTENKdGFXMWxWSGx3WlhNaU9sdDdJblI1Y0dVaU9pSmhjSEJzYVdOaGRHbHZiaTl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOUxIc2lkSGx3WlNJNkluUmxlSFF2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZWMTlMSHNpYm1GdFpTSTZJbGRsWWt0cGRDQmlkV2xzZEMxcGJpQlFSRVlpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgxZCxXeUp5ZFMxU1ZTSmQsMCwxLDAsMjQsMjM3NDE1OTMwLDgsMjI3MTI2NTIwLDEsMSwwLC0xLFIyOXZaMnhsSUVsdVl5NGdUbVYwYzJOaGNHVWdSMlZqYTI4Z1RHbHVkWGdnZURnMlh6WTBJRFV1TUNBb1dERXhPeUJNYVc1MWVDQjRPRFpmTmpRcElFRndjR3hsVjJWaVMybDBMelV6Tnk0ek5pQW9TMGhVVFV3c0lHeHBhMlVnUjJWamEyOHBJRU5vY205dFpTODVOaTR3TGpRMk5qUXVORFVnVTJGbVlYSnBMelV6Tnk0ek5pQXlNREF6TURFd055Qk5iM3BwYkd4aCxleUpqYUhKdmJXVWlPbnNpWVhCd0lqcDdJbWx6U1c1emRHRnNiR1ZrSWpwbVlXeHpaU3dpU1c1emRHRnNiRk4wWVhSbElqcDdJa1JKVTBGQ1RFVkVJam9pWkdsellXSnNaV1FpTENKSlRsTlVRVXhNUlVRaU9pSnBibk4wWVd4c1pXUWlMQ0pPVDFSZlNVNVRWRUZNVEVWRUlqb2libTkwWDJsdWMzUmhiR3hsWkNKOUxDSlNkVzV1YVc1blUzUmhkR1VpT25zaVEwRk9UazlVWDFKVlRpSTZJbU5oYm01dmRGOXlkVzRpTENKU1JVRkVXVjlVVDE5U1ZVNGlPaUp5WldGa2VWOTBiMTl5ZFc0aUxDSlNWVTVPU1U1SElqb2ljblZ1Ym1sdVp5SjlmU3dpY25WdWRHbHRaU0k2ZXlKUGJrbHVjM1JoYkd4bFpGSmxZWE52YmlJNmV5SkRTRkpQVFVWZlZWQkVRVlJGSWpvaVkyaHliMjFsWDNWd1pHRjBaU0lzSWtsT1UxUkJURXdpT2lKcGJuTjBZV3hzSWl3aVUwaEJVa1ZFWDAxUFJGVk1SVjlWVUVSQlZFVWlPaUp6YUdGeVpXUmZiVzlrZFd4bFgzVndaR0YwWlNJc0lsVlFSRUZVUlNJNkluVndaR0YwWlNKOUxDSlBibEpsYzNSaGNuUlNaWEYxYVhKbFpGSmxZWE52YmlJNmV5SkJVRkJmVlZCRVFWUkZJam9pWVhCd1gzVndaR0YwWlNJc0lrOVRYMVZRUkVGVVJTSTZJbTl6WDNWd1pHRjBaU0lzSWxCRlVrbFBSRWxESWpvaWNHVnlhVzlrYVdNaWZTd2lVR3hoZEdadmNtMUJjbU5vSWpwN0lrRlNUU0k2SW1GeWJTSXNJa0ZTVFRZMElqb2lZWEp0TmpRaUxDSk5TVkJUSWpvaWJXbHdjeUlzSWsxSlVGTTJOQ0k2SW0xcGNITTJOQ0lzSWxnNE5sOHpNaUk2SW5nNE5pMHpNaUlzSWxnNE5sODJOQ0k2SW5nNE5pMDJOQ0o5TENKUWJHRjBabTl5YlU1aFkyeEJjbU5vSWpwN0lrRlNUU0k2SW1GeWJTSXNJazFKVUZNaU9pSnRhWEJ6SWl3aVRVbFFVelkwSWpvaWJXbHdjelkwSWl3aVdEZzJYek15SWpvaWVEZzJMVE15SWl3aVdEZzJYelkwSWpvaWVEZzJMVFkwSW4wc0lsQnNZWFJtYjNKdFQzTWlPbnNpUVU1RVVrOUpSQ0k2SW1GdVpISnZhV1FpTENKRFVrOVRJam9pWTNKdmN5SXNJa3hKVGxWWUlqb2liR2x1ZFhnaUxDSk5RVU1pT2lKdFlXTWlMQ0pQVUVWT1FsTkVJam9pYjNCbGJtSnpaQ0lzSWxkSlRpSTZJbmRwYmlKOUxDSlNaWEYxWlhOMFZYQmtZWFJsUTJobFkydFRkR0YwZFhNaU9uc2lUazlmVlZCRVFWUkZJam9pYm05ZmRYQmtZWFJsSWl3aVZFaFNUMVJVVEVWRUlqb2lkR2h5YjNSMGJHVmtJaXdpVlZCRVFWUkZYMEZXUVVsTVFVSk1SU0k2SW5Wd1pHRjBaVjloZG1GcGJHRmliR1VpZlgxOWZRPT0sNjUsLTEyODU1NTEzLDEsMSwtMSwxNjk5OTU0ODg3LDE2OTk5NTQ4ODcsODM1OTM2NjM0LDI=',
    'xcid':'e6f1ddbf8a6eca300b1123bab4b38461',
    '__Secure-ab-group':'60',
    }

nextTime=int(time.time())+(365*86400)
cookdict = {
        "domain": "www.ozon.ru",
    "expiry": nextTime, #1775861041,
    "httpOnly": True,
    "name": "__Secure-ETC",
    "path": "/",
    "sameSite": "None",
    "secure": True,
    "value": "2cb43aca32027c5015f8eb6ef31b60b3"
}


def decodeUnucode(str):
    # match = re.match()
    match = re.search(r"(\d\d\d\d)",str)
    if match:
        codes = match.groups()
        _print('codes', codes)
    else:
        _print('???', str)
        for ch in str:
            _print(ch)
    return str
    


def getData(jsnin):
    """
    jsnin -- json in
    """
    logOut = False
    # if logOut: ...
    tplFound = '{key} found'
    tplFound = 'Found: {key}'
    global lg

    dpsrc = jsnin

    dumptusave = {}
    result = {}
    # key='url'
    # dumptusave[key] = url

    '''
    get: all data block
    '''
    key = 'widgetStates'
    if key in dpsrc:
        dpsrc = dpsrc[key]
        # dumptusave[key] = dpsrc
    else:
        _print(f'{key} not found')

    '''
    get: url
    '''
    key='webProductMainWidget-347746-default-1'
    if key in dpsrc:
        ...
        _print(tplFound.format(key=key))
        webPrice = json.loads(dpsrc[key])
        key = 'url'
        if key in webPrice:
            _print(tplFound.format(key=key))
            # "cardPrice": "2\u2009588\u2009\u20bd",
            dumptusave[key] = webPrice[key] #.replace('\u2009','').replace('\u20bd','')
            result[key] = dumptusave[key]

    '''
    get: cardPrice, price
    '''
    key='webPrice-3121879-default-1'
    if key in dpsrc:
        ...
        _print(tplFound.format(key=key))
        webPrice = json.loads(dpsrc[key])
        dumptusave[key] = webPrice
        # _print(webPrice)
        _key=key
        key = 'cardPrice'
        if key in webPrice:
            _print(tplFound.format(key=key))
            # "cardPrice": "2\u2009588\u2009\u20bd",
            dumptusave[key] = webPrice[key].replace('\u2009','').replace('\u20bd','')
            result[key] = dumptusave[key]
        key = 'price'
        if key in webPrice:
            _print(tplFound.format(key=key))
            dumptusave[key] = webPrice[key].replace('\u2009','').replace('\u20bd','')
            result[key] = dumptusave[key]

    '''
    get: title
    '''
    key='webProductHeading-3385933-default-1'
    if key in dpsrc:
        ...
        _print(tplFound.format(key=key))
        webProductHeading = json.loads(dpsrc[key])
        dumptusave[key] = webProductHeading
        # _print(webProductHeading)
        key = 'title'
        if key in webProductHeading:
            _print(tplFound.format(key=key))
            # _print(webPrice[key].decode('utf-8'))
            dumptusave[key] = webProductHeading[key]
            result[key] = dumptusave[key]
            _print(key,dumptusave[key])
            # decodeUnucode(dumptusave[key])

    '''
    get: sku, images
    '''
    key='webGallery-3311626-default-1'
    if key in dpsrc:
        ...
        _print(tplFound.format(key=key))
        webGallery = json.loads(dpsrc[key])
        # _print(webGallery)
        sku=''
        images=[]
        key = 'sku'
        if 'sku' in webGallery:
            _print(tplFound.format(key=key))
            sku = webGallery['sku']
            dumptusave[key] = sku
        key = 'images'
        if 'images' in webGallery:
            _print(tplFound.format(key=key))
            images = webGallery['images']
            images = [img['src'] for img in images]
            dumptusave[key] = images
            result[key] = dumptusave[key]
        if logOut: _print(f'sku {sku}')
        if logOut: _print('images', images)

    

    # _print(dpsrc)
    return result

def saveData(jsn,file_name = 'content.json'):
    """
    jsn complited data
    """
    global lg
    srcdump = jsn
    with open(f'./result/{file_name}', 'w') as cjhend:
        cjhend.write(srcdump)
        lg.logTime('json saved')


def getContent(url, driver, getAsJson = True):
    """
    get page content
    """
    # _print('getContent ...', f'line: {line()}')
    wd = driver
    wd.get(url)
    # _print('getContent ...', f'line: {line()}')
    lg.logTime('page get')
    jsnin = False
    # time.sleep(3)
    # time.sleep(10)
    # time.sleep(60)
    # time.sleep(60)
    # time.sleep(60)
    htpsrc = wd.page_source
    # element methods
    '''
    accessible_name
    aria_role
    clear
    click
    find_element
    find_elements
    get_attribute
    get_dom_attribute
    get_property
    id
    is_displayed
    is_enabled
    is_selected
    location
    location_once_scrolled_into_view
    parent
    rect
    screenshot
    screenshot_as_base64
    screenshot_as_png
    send_keys
    shadow_root
    size
    submit
    tag_name
    text
    value_of_css_property

    '''
    # _print(htpsrc)
    # getAsJson = True
    if getAsJson:

        for i in range(10):
            element = False
            try:
                # _print(type(htpsrc))
                element = driver.find_element(By.TAG_NAME, 'pre')
                # _print(jpsrc)
            except Exception as ex:
                    # print(ex.split('\n')[0])
                    # print(ex)
                    print(ex.msg, f'line: {line()}')
                    # a=[print(att) for att in dir(ex)]
            if not element:
                _print(color.RED + 'sleep +1s' + color.END )
                time.sleep(1)
                continue


            # dts=[str(_print(attr))+attr for attr in dir(element) ] # attr dump
            jpsrc = element.text
            _print('try to load')
            jsn =jpsrc.encode('utf-8').strip()
            # jsn =jsn.encode('utf-8')
            jsn =jsn.decode('utf-8')
            jsn =jsn.strip()
            dpsrc = json.loads(jsn)
            jsnin = dpsrc
            break
        
        # _print(wd.page_source)
        # lg.logTime('html out')
        # wd.save_screenshot('imgs/shot/homdy.png')
        # wd.get_screenshot_as_file('imgs/shot/homdy2.png')
        # lg.logTime('scrinshot save')
        # element = driver.find_element(By.TAG_NAME, 'myElement')
        # element = driver.find_element(By.CLASS_NAME, 'myElement')
        # element = driver.find_element(By.CSS_SELECTOR, 'div.myElement')
        # elem.clear()
        # elem.send_keys('123456789')
        # elem = driver.find_element(By.ID, 'm-documentationwebdriver')
        # elem.click()
        # elem.send_keys(Keys.ENTER )

    return jsnin


def getPages(wd,urls):
    # _print('getPages ...', f'line: {line()}')
    apnum=0
    getAsJson = True
    results = []
    # _print('urls ...', f'line: {line()}',urls)
    # _print('urls ...', f'line: {line()}',urls)
    if not len(urls):
        # url=urls.pop(0)
        return results
    for url in urls:
        jsonUrl = f'https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url={url}'
        # _print('getPages ...', f'line: {line()}')
        # _print('url', url, f'line: {line()}')
        jsnin = getContent(jsonUrl, wd, getAsJson)
        # _print('getPages ...', f'line: {line()}')
        jsn = getData(jsnin)
        # _print('getPages ...', f'line: {line()}')
        results.append(jsn)
        lg.logTime(f'append {apnum}');apnum+=1

    # jsnin = getContent(url, wd, getAsJson)
    # jsn = getData(jsnin)
    # results.append(jsn)
    # lg.logTime(f'append {apnum}');apnum+=1

    # jsnin = getContent(url, wd, getAsJson)
    # jsn = getData(jsnin)
    # results.append(jsn)
    # lg.logTime(f'append {apnum}');apnum+=1
    # _print('getPages ...', f'line: {line()}')
    return results



def getUrls(catalogUrl='',driver=False):
    '''
    url -- url to catalog json
    get products catalog urls
    '''
    ozDomen = 'https://www.ozon.ru'
    # print('getUrls ...')
    wd = driver
    # global url
    # urls = [url]
    urls = []
    # print('getUrls ...')
    try:
        # time.sleep(5)
        getAsJson = False
        getAsJson = True
        print(catalogUrl)
        msg = (Fore.GREEN + 'start get catalog' + Fore.RESET)
        print(msg)
        html = getContent(catalogUrl, wd, getAsJson)
        # print(html)
        # items = driver.find_elements_by_xpath('//div[@data-market="item-photo"]')
        # items[0].click()

        key='widgetStates'

        data = html[key]
        # print(data)
        
        # a=[print(k) for k,v in data.items()]

        key_path=r'^searchResults*'
        key_path=r'^searchResultsV2*'
        for k in dict(data).keys():
            res = re.match(key_path,k)
            if res:
                key = k
                _print(f'{key} found')
                # _print('search_', k, res)
                search = data[key]
                search = json.loads(data[key])
                # found dump
                # cooJsn = json.dumps(search['items'][0],indent=4)
                # print(cooJsn)
                for item in search['items']:
                    # _print('line: ', line())
                    try:
                        url = item['action']['link']
                        # url = f'{ozDomen}{url}'
                        urls.append(url)
                        # print(url)
                    except Exception as ex:
                        print(ex)
                        msg = ex.msg
                        msg = (Fore.GREEN + msg + Fore.RESET)
                        _print(msg, f'line: {line()}')
                # dump('urls', urls)

        msg = (Fore.GREEN + 'end get catalog' + Fore.RESET)
        print(msg)


# widgetStates
# searchResultsV2-3669723-default-4

        # time.sleep(5)
        # time.sleep(5)
        # time.sleep(5)
    except Exception as ex:
        print(ex)
        msg = ex.msg
        msg = (Fore.GREEN + msg + Fore.RESET)
        _print(msg)
    return urls

# with WebDriver(webdriver.Chrome(**webdkargs)) as wd:
hasErr=True
hasErr=False
with WebDriver(driver) as wd:
    try:
        _print(url)
        lg.logTime('parse start')
        wd.get(url)
        lg.logTime('page get')
        coo_keys = 'cookeys_123456'
        fn = f'/resrs/{coo_keys}_{way}_cookies' # resrs -- resorces
        pdest = os.path.dirname(os.path.realpath(__file__))+fn # path for cookies
        dest_ex = os.path.isfile(pdest)
        # if not hasErr:
        try:
            ...
            if hasErr:
                raise ValueError('cercles with no data')
            if dest_ex:
                _print ('fl exists:',fn)
                with open(f'.{fn}','rb') as hendl: # relative file path
                    cookies = pickle.load( hendl)
                    # cookies = cook2
                    lg.logTime('cookies add')
                    # _print('cookies')
                    # _print(cookies)
                    for cookie in cookies:
                    #     cookie['domain'] = 'www.ozon.ru'
                        # cooJsn = json.dumps(cookie,indent=4)
                        # _print(cooJsn)
                        wd.add_cookie(cookie)
                    #     lg.logTime("cookie:\n"+cooJsn)

        except Exception as ex:
            _print(ex, f'line: {line()}')
            lg.logTime('cookies error')
            _print('COOKS 2')
            for cookN,cookV in cook2.items():
                cookdict['name'] = cookN
                cookdict['value'] = cookV
                # _print(f'{cookN:20}',cookV)
                wd.add_cookie(cookdict)

        try:
            lg.logTime('get json start')
            '''
.


https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094&__rr=1
https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/category/sistemnye-bloki-15704/?page=7

widgetStates
searchResultsV2-3669723-default-4

https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2Fcategory%2Fsistemnye-bloki-15704%2F%3Flayout_page_index%3D2%26page%3D7%26paginator_token%3D3618992%26search_page_state%3DbhSpmKzdnYg6J3A0Y5aAaTX08WhdhPG6q0io7XN_YwXnMseXdHkJbXgcZ2jkEltyHnMzRx5gHc4zhxT_0wG_o74N2C0AIAnQ7z9-twF2vEj6p_WvQZoNP60XZHY%253D%26start_page_id%3Ddb613ceb683804acddfb3ce651639428
https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/category/sistemnye-bloki-15704/?layout_page_index=2&page=7&paginator_token=3618992&search_page_state=bhSpmKzdnYg6J3A0Y5aAaTX08WhdhPG6q0io7XN_YwXnMseXdHkJbXgcZ2jkEltyHnMzRx5gHc4zhxT_0wG_o74N2C0AIAnQ7z9-twF2vEj6p_WvQZoNP60XZHY%3D&start_page_id=db613ceb683804acddfb3ce651639428


https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/category/sistemnye-bloki-15704/%3Fpage=7%3D

"{\"tileLayout\":\"LAYOUT_GRID4\",\"items\":[
    {\"action\":
    
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",
    \"link\":\"/product/jetgame-sistemnyy-blok-igrovoy-kompyuter-intel-xeon-e5-2650v2-ram-32-gb-ssd-512-gb-amd-radeon-rx-580-1874744714/
    ?at=pZtp4Dz7Zs2m31DQCgZGZjzUyKrWgZhxnRr5LirJRxjY\",
    \"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[
        {\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":
        {\"price\":[{\"text\":\"24 371 ₽\",\"textStyle\":\"PRICE\"},
        {\"text\":\"60 000 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],
        \"discount\":\"−59%\",\"priceStyle\":
        {\"styleType\":\"SALE_PRICE\",\"gradient\":{\"startColor\":\"#F1117E\",\"endColor\":\"#F1117E\"}},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},
        {\"type\":\"atom\",\"id\":\"blackFridayStockbar\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":
        {\"text\":\"Осталось 31 шт\",\"textStyle\":\"tsBodyControl400Small\",\"textColor\":\"textAccent\",\"maxLines\":1,\"testInfo\":{\"automatizationId\":\"tile-blackFridayStockbar\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"JetGame Системный блок Игровой компьютер (Intel Xeon E5-2650V2, RAM 32 ГБ, SSD 512 ГБ, AMD Radeon RX 580 (4 Гб), Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.7  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"34 отзыва\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"15 апреля\",\"maxItems\":98,\"currentItems\":0,\"action\":{\"id\":\"1874744714\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"pZtp4Dz7Zs2m31DQCgZGZjzUyKrWgZhxnRr5LirJRxjY\",\"custom\":{\"advertLite\":\"AMUBIm37vDt0-4TDf6Wrvy7pVKRI8nxdJqeQhe2B-_MA2aS4ApoY-r_Xw52D4mkHnWMVTfuoA9ScSmYWaA\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}},\"expressButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"+1 408 ₽ завтра\",\"maxItems\":10,\"currentItems\":0,\"action\":{\"id\":\"1874744714\",\"quantity\":1,\"selectedDeliverySchema\":243},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"z6tOWLR7zclL1lklhkmNqk6t1RgL40sAN5qxZcyrxXO5\",\"custom\":{\"advertLite\":\"AMUBIm37vDt0-4TDf6Wrvy7pVKRI8nxdJqeQhe2B-_MA2aS4ApoY-r_Xw52D4mkHnWMVTfuoA9ScSmYWaA\"}}},\"testInfo\":{\"automatizationId\":\"expressAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY_EXPRESS\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1874744714\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-j/7326916435.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-h/7326916073.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-e/7326916394.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-v/7326916195.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-i/7326916578.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-a/7326916174.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Распродажа\",\"image\":\"ic_s_hot_filled_compact\",\"tintColor\":\"#ffffffff\",\"iconTintColor\":\"#ffffffff\",\"backgroundColor\":\"#f1117eff\",\"testInfo\":{\"automatizationId\":\"badge-marketingSuperHigh\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1874744714\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"GRt23gJ69ilv0746h62ApDyfLVMOl5uMy12DpIVlGMw\",\"custom\":{\"advertLite\":\"AMUBIm37vDt0-4TDf6Wrvy7pVKRI8nxdJqeQhe2B-_MA2aS4ApoY-r_Xw52D4mkHnWMVTfuoA9ScSmYWaA\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"GRt23gJ69ilv0746h62ApDyfLVMOl5uMy12DpIVlGMw\",\"custom\":{\"advertLite\":\"AMUBIm37vDt0-4TDf6Wrvy7pVKRI8nxdJqeQhe2B-_MA2aS4ApoY-r_Xw52D4mkHnWMVTfuoA9ScSmYWaA\"}},\"click\":{\"actionType\":\"click\",\"key\":\"GRt23gJ69ilv0746h62ApDyfLVMOl5uMy12DpIVlGMw\",\"custom\":{\"advertLite\":\"AMUBIm37vDt0-4TDf6Wrvy7pVKRI8nxdJqeQhe2B-_MA2aS4ApoY-r_Xw52D4mkHnWMVTfuoA9ScSmYWaA\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"GRt23gJ69ilv0746h62ApDyfLVMOl5uMy12DpIVlGMw\",\"custom\":{\"advertLite\":\"AMUBIm37vDt0-4TDf6Wrvy7pVKRI8nxdJqeQhe2B-_MA2aS4ApoY-r_Xw52D4mkHnWMVTfuoA9ScSmYWaA\"}},\"view\":{\"actionType\":\"view\",\"key\":\"GRt23gJ69ilv0746h62ApDyfLVMOl5uMy12DpIVlGMw\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/sistemnyy-blok-aurora-pc-intel-core-i7-3770-ram-16-gb-ssd-512-gb-intel-hd-graphics-4000-windows-10-1412508908/?at=mqtky259qhW05BYRhWYW85XFgWNv83F29owvms1BJ6P3\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"18 608 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"52 900 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−64%\",\"priceStyle\":{\"styleType\":\"SALE_PRICE\",\"gradient\":{\"startColor\":\"#F1117E\",\"endColor\":\"#F1117E\"}},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"blackFridayStockbar\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Осталось 92 шт\",\"textStyle\":\"tsBodyControl400Small\",\"textColor\":\"textAccent\",\"maxLines\":1,\"testInfo\":{\"automatizationId\":\"tile-blackFridayStockbar\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Системный блок AURORA PC (Intel Core i7-3770, RAM 16 ГБ, SSD 512 ГБ, Intel HD Graphics 4000, Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.8  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"348 отзывов\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"Завтра\",\"maxItems\":92,\"currentItems\":0,\"action\":{\"id\":\"1412508908\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"mqtky259qhW05BYRhWYW85XFgWNv83F29owvms1BJ6P3\",\"custom\":{\"advertLite\":\"AMUBtsGZB7A3iOLa0NgtxyFcrp7iWmiIxbPScsEnLcEbb-1V7xFx--lKmwmLhy2E-8rfeyMSaR7k-EgKyQ\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1412508908\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-d/7362460021.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-5/7362402089.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-s/7362338356.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-a/7396800418.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-2/7362338402.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-4/7362338620.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Распродажа\",\"image\":\"ic_s_hot_filled_compact\",\"tintColor\":\"#ffffffff\",\"iconTintColor\":\"#ffffffff\",\"backgroundColor\":\"#f1117eff\",\"testInfo\":{\"automatizationId\":\"badge-marketingSuperHigh\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1412508908\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"mqtky259qhW05BYRhWYW85XFgWNv83F29owvms1BJ6P3\",\"custom\":{\"advertLite\":\"AMUBtsGZB7A3iOLa0NgtxyFcrp7iWmiIxbPScsEnLcEbb-1V7xFx--lKmwmLhy2E-8rfeyMSaR7k-EgKyQ\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"mqtky259qhW05BYRhWYW85XFgWNv83F29owvms1BJ6P3\",\"custom\":{\"advertLite\":\"AMUBtsGZB7A3iOLa0NgtxyFcrp7iWmiIxbPScsEnLcEbb-1V7xFx--lKmwmLhy2E-8rfeyMSaR7k-EgKyQ\"}},\"click\":{\"actionType\":\"click\",\"key\":\"mqtky259qhW05BYRhWYW85XFgWNv83F29owvms1BJ6P3\",\"custom\":{\"advertLite\":\"AMUBtsGZB7A3iOLa0NgtxyFcrp7iWmiIxbPScsEnLcEbb-1V7xFx--lKmwmLhy2E-8rfeyMSaR7k-EgKyQ\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"mqtky259qhW05BYRhWYW85XFgWNv83F29owvms1BJ6P3\",\"custom\":{\"advertLite\":\"AMUBtsGZB7A3iOLa0NgtxyFcrp7iWmiIxbPScsEnLcEbb-1V7xFx--lKmwmLhy2E-8rfeyMSaR7k-EgKyQ\"}},\"view\":{\"actionType\":\"view\",\"key\":\"mqtky259qhW05BYRhWYW85XFgWNv83F29owvms1BJ6P3\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/intel-sistemnyy-blok-ofisnyy-kompyuter-intel-core-i5-12400-ram-16-gb-ssd-512-gb-intel-hd-graphics-1943071901/?at=mqtky259qhQrmDkLU3w65lmsojJWDMt5E5omPUv0nrWv\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"34 081 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"59 750 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−42%\",\"priceStyle\":{\"styleType\":\"CARD_PRICE\"},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"title\":\"<b>Intel</b>\",\"titleColor\":\"textPrimary\",\"testInfo\":{\"automatizationId\":\"tile-list-paid-brand\"}}],\"textStyle\":\"tsBodyM\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-labels\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Intel Системный блок - офисный компьютер (Intel Core i5-12400, RAM 16 ГБ, SSD 512 ГБ, Intel HD Graphics, Windows 11 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"5.0  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"3 отзыва\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"15 апреля\",\"maxItems\":6,\"currentItems\":0,\"action\":{\"id\":\"1943071901\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"mqtky259qhQrmDkLU3w65lmsojJWDMt5E5omPUv0nrWv\",\"custom\":{\"advertLite\":\"AMUBnPk_hTKdqarXOyqhdKmFBOrKrBqcKUtzPa7pmgu19IKbNJzVVXkX5xzJFekVVJNht7kuOsYftFMLAQ\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}},\"expressButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"Завтра\",\"maxItems\":5,\"currentItems\":0,\"action\":{\"id\":\"1943071901\",\"quantity\":1,\"selectedDeliverySchema\":243},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"oZt624XQmCV8G1p0uwWJPmC9gyzACRpRK7QSJy4MxW\",\"custom\":{\"advertLite\":\"AMUBnPk_hTKdqarXOyqhdKmFBOrKrBqcKUtzPa7pmgu19IKbNJzVVXkX5xzJFekVVJNht7kuOsYftFMLAQ\"}}},\"testInfo\":{\"automatizationId\":\"expressAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY_EXPRESS\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1943071901\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-3/7390785351.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-2/7400279738.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-6/7390785354.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-u/7390783218.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-u/7390426062.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-s/7390426060.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"500 баллов за отзыв\",\"image\":\"ic_s_points_filled_compact\",\"tintColor\":\"#FFFFFF\",\"iconTintColor\":\"#FFFFFF\",\"backgroundColor\":\"#5B51DE\",\"testInfo\":{\"automatizationId\":\"badge-reviewPayout\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1943071901\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"Eqtk4PWYjhqLXGByFABZ833T7EGQgPCg745Zrc96ygkY\",\"custom\":{\"advertLite\":\"AMUBnPk_hTKdqarXOyqhdKmFBOrKrBqcKUtzPa7pmgu19IKbNJzVVXkX5xzJFekVVJNht7kuOsYftFMLAQ\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"Eqtk4PWYjhqLXGByFABZ833T7EGQgPCg745Zrc96ygkY\",\"custom\":{\"advertLite\":\"AMUBnPk_hTKdqarXOyqhdKmFBOrKrBqcKUtzPa7pmgu19IKbNJzVVXkX5xzJFekVVJNht7kuOsYftFMLAQ\"}},\"click\":{\"actionType\":\"click\",\"key\":\"Eqtk4PWYjhqLXGByFABZ833T7EGQgPCg745Zrc96ygkY\",\"custom\":{\"advertLite\":\"AMUBnPk_hTKdqarXOyqhdKmFBOrKrBqcKUtzPa7pmgu19IKbNJzVVXkX5xzJFekVVJNht7kuOsYftFMLAQ\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"Eqtk4PWYjhqLXGByFABZ833T7EGQgPCg745Zrc96ygkY\",\"custom\":{\"advertLite\":\"AMUBnPk_hTKdqarXOyqhdKmFBOrKrBqcKUtzPa7pmgu19IKbNJzVVXkX5xzJFekVVJNht7kuOsYftFMLAQ\"}},\"view\":{\"actionType\":\"view\",\"key\":\"Eqtk4PWYjhqLXGByFABZ833T7EGQgPCg745Zrc96ygkY\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/robotcomp-sistemnyy-blok-bosc-v2-intel-core-i3-12100-ram-16-gb-ssd-512-gb-intel-uhd-graphics-730-276312879/?at=w0tglpL2nF4wqAjDCB55nVOHxXQ7ENfMo6gBGhY0463Y\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"34 347 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"58 684 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−41%\",\"priceStyle\":{\"styleType\":\"SALE_PRICE\",\"gradient\":{\"startColor\":\"#F1117E\",\"endColor\":\"#F1117E\"}},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"blackFridayStockbar\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Осталось 288 шт\",\"textStyle\":\"tsBodyControl400Small\",\"textColor\":\"textAccent\",\"maxLines\":1,\"testInfo\":{\"automatizationId\":\"tile-blackFridayStockbar\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_confirmed_filled_compact\",\"tintColor\":\"graphicPositivePrimary\"},\"title\":\"<b>Оригинал</b>\",\"titleColor\":\"textPrimary\",\"testInfo\":{\"automatizationId\":\"tile-list-original-in-label\"}}],\"textStyle\":\"tsBodyM\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-labels\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Robotcomp Системный блок Босc V2 (Intel Core i3-12100, RAM 16 ГБ, SSD 512 ГБ, Intel UHD Graphics 730, Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.8  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"59 отзывов\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"15 апреля\",\"maxItems\":89,\"currentItems\":0,\"action\":{\"id\":\"276312879\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"XQtkEJnWZholgJrqT793OkBFjzgO52F4WmLgsQM3zQm\",\"custom\":{\"advertLite\":\"AMUBWKKuM2Kbe3RLb4hte5GYw9iPBGcyP87csB0-5IuibvZuPF5NpbAVGqYb5gScX_vgEHb_BiYziYkr\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}},\"expressButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"Завтра\",\"maxItems\":199,\"currentItems\":0,\"action\":{\"id\":\"276312879\",\"quantity\":1,\"selectedDeliverySchema\":243},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"w0tglpL2nF4wqAjDCB55nVOHxXQ7ENfMo6gBGhY0463Y\",\"custom\":{\"advertLite\":\"AMUBWKKuM2Kbe3RLb4hte5GYw9iPBGcyP87csB0-5IuibvZuPF5NpbAVGqYb5gScX_vgEHb_BiYziYkr\"}}},\"testInfo\":{\"automatizationId\":\"expressAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY_EXPRESS\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"276312879\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-o/7354926852.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-5/7354926833.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-z/7352807867.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-0/7352808156.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-l/7352807673.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-8/7352808380.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Распродажа\",\"image\":\"ic_s_hot_filled_compact\",\"tintColor\":\"#ffffffff\",\"iconTintColor\":\"#ffffffff\",\"backgroundColor\":\"#f1117eff\",\"testInfo\":{\"automatizationId\":\"badge-marketingSuperHigh\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"276312879\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"DqtDYPByZTELn40BCzLNrnDFnXlqnji0YpGPRhq1vX99\",\"custom\":{\"advertLite\":\"AMUBWKKuM2Kbe3RLb4hte5GYw9iPBGcyP87csB0-5IuibvZuPF5NpbAVGqYb5gScX_vgEHb_BiYziYkr\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"DqtDYPByZTELn40BCzLNrnDFnXlqnji0YpGPRhq1vX99\",\"custom\":{\"advertLite\":\"AMUBWKKuM2Kbe3RLb4hte5GYw9iPBGcyP87csB0-5IuibvZuPF5NpbAVGqYb5gScX_vgEHb_BiYziYkr\"}},\"click\":{\"actionType\":\"click\",\"key\":\"DqtDYPByZTELn40BCzLNrnDFnXlqnji0YpGPRhq1vX99\",\"custom\":{\"advertLite\":\"AMUBWKKuM2Kbe3RLb4hte5GYw9iPBGcyP87csB0-5IuibvZuPF5NpbAVGqYb5gScX_vgEHb_BiYziYkr\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"DqtDYPByZTELn40BCzLNrnDFnXlqnji0YpGPRhq1vX99\",\"custom\":{\"advertLite\":\"AMUBWKKuM2Kbe3RLb4hte5GYw9iPBGcyP87csB0-5IuibvZuPF5NpbAVGqYb5gScX_vgEHb_BiYziYkr\"}},\"view\":{\"actionType\":\"view\",\"key\":\"DqtDYPByZTELn40BCzLNrnDFnXlqnji0YpGPRhq1vX99\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/intel-sistemnyy-blok-moshchnyy-igrovoy-intel-core-i7-8700t-ram-32-gb-ssd-512-gb-amd-radeon-pro-1864221094/?at=jYtZo9jV0iwpE34Yu7Wg4LLsGOJ64vcGgORDLu0yKR5X\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"38 609 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"70 000 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−44%\",\"priceStyle\":{\"styleType\":\"CARD_PRICE\"},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"title\":\"<b>Intel</b>\",\"titleColor\":\"textPrimary\",\"testInfo\":{\"automatizationId\":\"tile-list-paid-brand\"}}],\"textStyle\":\"tsBodyM\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-labels\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Intel Системный блок Мощный игровой (Intel Core i7-8700T, RAM 32 ГБ, SSD 512 ГБ, AMD Radeon Pro Vega 56 (8 Гб), Windows 11 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.9  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"31 отзыв\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"15 апреля\",\"maxItems\":20,\"currentItems\":0,\"action\":{\"id\":\"1864221094\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"jYtZo9jV0iwpE34Yu7Wg4LLsGOJ64vcGgORDLu0yKR5X\",\"custom\":{\"advertLite\":\"AMUBSOdX98ZulfMuIfxRRUiWcVBm3meqUooO9bFbsRUc_LAi0jmiihsweGAM1GOWD2Qw67n78RccMndKUA\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1864221094\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-8/7357356008.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-c/7313576556.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-a/7313576554.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-8/7313576552.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-r/7419401163.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-b/7313576555.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"800 баллов за отзыв\",\"image\":\"ic_s_points_filled_compact\",\"tintColor\":\"#FFFFFF\",\"iconTintColor\":\"#FFFFFF\",\"backgroundColor\":\"#5B51DE\",\"testInfo\":{\"automatizationId\":\"badge-reviewPayout\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1864221094\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"jYtZo9jV0iwpE34Yu7Wg4LLsGOJ64vcGgORDLu0yKR5X\",\"custom\":{\"advertLite\":\"AMUBSOdX98ZulfMuIfxRRUiWcVBm3meqUooO9bFbsRUc_LAi0jmiihsweGAM1GOWD2Qw67n78RccMndKUA\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"jYtZo9jV0iwpE34Yu7Wg4LLsGOJ64vcGgORDLu0yKR5X\",\"custom\":{\"advertLite\":\"AMUBSOdX98ZulfMuIfxRRUiWcVBm3meqUooO9bFbsRUc_LAi0jmiihsweGAM1GOWD2Qw67n78RccMndKUA\"}},\"click\":{\"actionType\":\"click\",\"key\":\"jYtZo9jV0iwpE34Yu7Wg4LLsGOJ64vcGgORDLu0yKR5X\",\"custom\":{\"advertLite\":\"AMUBSOdX98ZulfMuIfxRRUiWcVBm3meqUooO9bFbsRUc_LAi0jmiihsweGAM1GOWD2Qw67n78RccMndKUA\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"jYtZo9jV0iwpE34Yu7Wg4LLsGOJ64vcGgORDLu0yKR5X\",\"custom\":{\"advertLite\":\"AMUBSOdX98ZulfMuIfxRRUiWcVBm3meqUooO9bFbsRUc_LAi0jmiihsweGAM1GOWD2Qw67n78RccMndKUA\"}},\"view\":{\"actionType\":\"view\",\"key\":\"jYtZo9jV0iwpE34Yu7Wg4LLsGOJ64vcGgORDLu0yKR5X\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/trade-electronics-sistemnyy-blok-intel-intel-core-i7-7700-ram-32-gb-ssd-1000-gb-amd-radeon-rx-580-1973641599/?at=Y7tjV83wXsPn56vASjjGk1BCDBD9QmCxBMZLpUNKpGQO\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"29 971 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"59 990 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−50%\",\"priceStyle\":{\"styleType\":\"CARD_PRICE\"},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"TRADE Electronics Системный блок Intel (Intel Core i7-7700, RAM 32 ГБ, SSD 1000 ГБ, AMD Radeon RX 580 (8 Гб), Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.8  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"58 отзывов\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"16 апреля\",\"maxItems\":39,\"currentItems\":0,\"action\":{\"id\":\"1973641599\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"Y7tjV83wXsPn56vASjjGk1BCDBD9QmCxBMZLpUNKpGQO\",\"custom\":{\"advertLite\":\"AMUBWz8pMKw7wVGkjlH9sux49POPjaSANkDqhDSeiINPMksQHQuwQa-WMp8rTKC5IpMnnIrZMFyGUqV7kA\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1973641599\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-2/7447591982.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-9/7453728585.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-b/7453728587.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-2/7453728578.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Новинка\",\"tintColor\":\"textLightKey\",\"backgroundColor\":\"bgPositivePrimary\",\"testInfo\":{\"automatizationId\":\"badge-novel\"},\"theme\":\"STYLE_TYPE_MEDIUM\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1973641599\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"Y7tjV83wXsPn56vASjjGk1BCDBD9QmCxBMZLpUNKpGQO\",\"custom\":{\"advertLite\":\"AMUBWz8pMKw7wVGkjlH9sux49POPjaSANkDqhDSeiINPMksQHQuwQa-WMp8rTKC5IpMnnIrZMFyGUqV7kA\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"Y7tjV83wXsPn56vASjjGk1BCDBD9QmCxBMZLpUNKpGQO\",\"custom\":{\"advertLite\":\"AMUBWz8pMKw7wVGkjlH9sux49POPjaSANkDqhDSeiINPMksQHQuwQa-WMp8rTKC5IpMnnIrZMFyGUqV7kA\"}},\"click\":{\"actionType\":\"click\",\"key\":\"Y7tjV83wXsPn56vASjjGk1BCDBD9QmCxBMZLpUNKpGQO\",\"custom\":{\"advertLite\":\"AMUBWz8pMKw7wVGkjlH9sux49POPjaSANkDqhDSeiINPMksQHQuwQa-WMp8rTKC5IpMnnIrZMFyGUqV7kA\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"Y7tjV83wXsPn56vASjjGk1BCDBD9QmCxBMZLpUNKpGQO\",\"custom\":{\"advertLite\":\"AMUBWz8pMKw7wVGkjlH9sux49POPjaSANkDqhDSeiINPMksQHQuwQa-WMp8rTKC5IpMnnIrZMFyGUqV7kA\"}},\"view\":{\"actionType\":\"view\",\"key\":\"Y7tjV83wXsPn56vASjjGk1BCDBD9QmCxBMZLpUNKpGQO\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/jetgame-sistemnyy-blok-kompyuter-ofisnyy-intel-core-i3-2100-ram-16-gb-ssd-512-gb-intel-hd-graphics-1315807923/?at=46tR4oJqxiMZD0D9h6zQmWDfykvk7qFrq95VWSvV3D69\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"11 852 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"26 000 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−54%\",\"priceStyle\":{\"styleType\":\"SALE_PRICE\",\"gradient\":{\"startColor\":\"#F1117E\",\"endColor\":\"#F1117E\"}},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"blackFridayStockbar\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Осталось 125 шт\",\"textStyle\":\"tsBodyControl400Small\",\"textColor\":\"textAccent\",\"maxLines\":1,\"testInfo\":{\"automatizationId\":\"tile-blackFridayStockbar\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"JetGame Системный блок Компьютер офисный (Intel Core i3-2100, RAM 16 ГБ, SSD 512 ГБ, Intel HD Graphics, Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.7  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"98 отзывов\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"15 апреля\",\"maxItems\":115,\"currentItems\":0,\"action\":{\"id\":\"1315807923\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"46tR4oJqxiMZD0D9h6zQmWDfykvk7qFrq95VWSvV3D69\",\"custom\":{\"advertLite\":\"AMUBFA_1FYZa5PNRHpFeBtHKSAsx1gga0a9jLxshdGoCRjZZtCFdNUvpulxB-sNgWlxr2bsL2zTV-Gg88w\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}},\"expressButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"+17 ₽ завтра\",\"maxItems\":10,\"currentItems\":0,\"action\":{\"id\":\"1315807923\",\"quantity\":1,\"selectedDeliverySchema\":243},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"vQtrwXWRZhXR2Bl2tPN4kAnUWwjWmVs7JkqYRFKMr4O9\",\"custom\":{\"advertLite\":\"AMUBFA_1FYZa5PNRHpFeBtHKSAsx1gga0a9jLxshdGoCRjZZtCFdNUvpulxB-sNgWlxr2bsL2zTV-Gg88w\"}}},\"testInfo\":{\"automatizationId\":\"expressAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY_EXPRESS\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1315807923\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-w/7113991208.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-z/7113991175.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-i/7113991194.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-u/7113991206.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-2/7113991178.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-6/7113991182.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Распродажа\",\"image\":\"ic_s_hot_filled_compact\",\"tintColor\":\"#ffffffff\",\"iconTintColor\":\"#ffffffff\",\"backgroundColor\":\"#f1117eff\",\"testInfo\":{\"automatizationId\":\"badge-marketingSuperHigh\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1315807923\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"DqtDYPByZTjwDJo1UJmrlx6sXL6Pl1uRXxY6nHPmwBB\",\"custom\":{\"advertLite\":\"AMUBFA_1FYZa5PNRHpFeBtHKSAsx1gga0a9jLxshdGoCRjZZtCFdNUvpulxB-sNgWlxr2bsL2zTV-Gg88w\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"DqtDYPByZTjwDJo1UJmrlx6sXL6Pl1uRXxY6nHPmwBB\",\"custom\":{\"advertLite\":\"AMUBFA_1FYZa5PNRHpFeBtHKSAsx1gga0a9jLxshdGoCRjZZtCFdNUvpulxB-sNgWlxr2bsL2zTV-Gg88w\"}},\"click\":{\"actionType\":\"click\",\"key\":\"DqtDYPByZTjwDJo1UJmrlx6sXL6Pl1uRXxY6nHPmwBB\",\"custom\":{\"advertLite\":\"AMUBFA_1FYZa5PNRHpFeBtHKSAsx1gga0a9jLxshdGoCRjZZtCFdNUvpulxB-sNgWlxr2bsL2zTV-Gg88w\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"DqtDYPByZTjwDJo1UJmrlx6sXL6Pl1uRXxY6nHPmwBB\",\"custom\":{\"advertLite\":\"AMUBFA_1FYZa5PNRHpFeBtHKSAsx1gga0a9jLxshdGoCRjZZtCFdNUvpulxB-sNgWlxr2bsL2zTV-Gg88w\"}},\"view\":{\"actionType\":\"view\",\"key\":\"DqtDYPByZTjwDJo1UJmrlx6sXL6Pl1uRXxY6nHPmwBB\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/lenovo-sistemnyy-blok-kompyuter-sff-amd-pro-a8-8650b-ram-16-gb-ssd-120-gb-amd-radeon-r7-windows-10-1590381111/?at=DqtDYPByZT05z7owTQN2g5snKyVxAfx3NXvAiooRq20\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"6 091 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"44 100 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−86%\",\"priceStyle\":{\"styleType\":\"SALE_PRICE\",\"gradient\":{\"startColor\":\"#F1117E\",\"endColor\":\"#F1117E\"}},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"blackFridayStockbar\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Осталось 235 шт\",\"textStyle\":\"tsBodyControl400Small\",\"textColor\":\"textAccent\",\"maxLines\":1,\"testInfo\":{\"automatizationId\":\"tile-blackFridayStockbar\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"title\":\"<b>Lenovo</b>\",\"titleColor\":\"textPrimary\",\"testInfo\":{\"automatizationId\":\"tile-list-paid-brand\"}}],\"textStyle\":\"tsBodyM\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-labels\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Lenovo Системный блок Компьютер SFF (AMD PRO A8-8650B, RAM 16 ГБ, SSD 120 ГБ, AMD Radeon R7, Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.7  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"3 266 отзывов\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"Завтра\",\"maxItems\":235,\"currentItems\":0,\"action\":{\"id\":\"1590381111\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"DqtDYPByZT05z7owTQN2g5snKyVxAfx3NXvAiooRq20\",\"custom\":{\"advertLite\":\"AMUBb3afhXjDUeHOkSqWmoULqk4xcXOAoyW0v9VgP8lJ-HqgH3tBaYUlwhSmCosEZlTxtrVccxjYxgzf\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1590381111\",\"tileDefer\":0,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-m/7429824238.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-g/7429824160.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-l/7429824201.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-x/7429824177.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-3/7429824183.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-h/7429824197.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Распродажа\",\"image\":\"ic_s_hot_filled_compact\",\"tintColor\":\"#ffffffff\",\"iconTintColor\":\"#ffffffff\",\"backgroundColor\":\"#f1117eff\",\"testInfo\":{\"automatizationId\":\"badge-marketingSuperHigh\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1590381111\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"DqtDYPByZT05z7owTQN2g5snKyVxAfx3NXvAiooRq20\",\"custom\":{\"advertLite\":\"AMUBb3afhXjDUeHOkSqWmoULqk4xcXOAoyW0v9VgP8lJ-HqgH3tBaYUlwhSmCosEZlTxtrVccxjYxgzf\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"DqtDYPByZT05z7owTQN2g5snKyVxAfx3NXvAiooRq20\",\"custom\":{\"advertLite\":\"AMUBb3afhXjDUeHOkSqWmoULqk4xcXOAoyW0v9VgP8lJ-HqgH3tBaYUlwhSmCosEZlTxtrVccxjYxgzf\"}},\"click\":{\"actionType\":\"click\",\"key\":\"DqtDYPByZT05z7owTQN2g5snKyVxAfx3NXvAiooRq20\",\"custom\":{\"advertLite\":\"AMUBb3afhXjDUeHOkSqWmoULqk4xcXOAoyW0v9VgP8lJ-HqgH3tBaYUlwhSmCosEZlTxtrVccxjYxgzf\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"DqtDYPByZT05z7owTQN2g5snKyVxAfx3NXvAiooRq20\",\"custom\":{\"advertLite\":\"AMUBb3afhXjDUeHOkSqWmoULqk4xcXOAoyW0v9VgP8lJ-HqgH3tBaYUlwhSmCosEZlTxtrVccxjYxgzf\"}},\"view\":{\"actionType\":\"view\",\"key\":\"DqtDYPByZT05z7owTQN2g5snKyVxAfx3NXvAiooRq20\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/ironcore-sistemnyy-blok-igrovoy-kompyuter-pk-air-3600-amd-ryzen-5-3600-ram-32-gb-ssd-1000-gb-1653713652/?at=6WtZLDoqJixz2L29Cv2mWRxC50q8wKHvkqv6ZIomGMvZ\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"71 658 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"140 445 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−48%\",\"priceStyle\":{\"styleType\":\"SALE_PRICE\",\"gradient\":{\"startColor\":\"#F1117E\",\"endColor\":\"#F1117E\"}},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"blackFridayStockbar\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Осталось 79 шт\",\"textStyle\":\"tsBodyControl400Small\",\"textColor\":\"textAccent\",\"maxLines\":1,\"testInfo\":{\"automatizationId\":\"tile-blackFridayStockbar\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"iRONCORE Системный блок Игровой компьютер ПК AIR 3600 (AMD Ryzen 5 3600, RAM 32 ГБ, SSD 1000 ГБ, NVIDIA GeForce RTX 3060 (12 Гб), Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.8  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"81 отзыв\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"18 апреля\",\"maxItems\":79,\"currentItems\":0,\"action\":{\"id\":\"1653713652\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"6WtZLDoqJixz2L29Cv2mWRxC50q8wKHvkqv6ZIomGMvZ\",\"custom\":{\"advertLite\":\"AMUBN_z6g7N5y4ITuphmuU2Pd4gaX0XFxmch5_mnlFbYfAMCsJ5CR2P4tlTJWXDaKjbYq3UJ6WuwSQJc\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1653713652\",\"tileDefer\":2,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-9/7059133593.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-2/7059133550.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-q/7059133574.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-r/7059133575.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-5/7059133553.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-p/7059133573.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"450 баллов за отзыв\",\"image\":\"ic_s_points_filled_compact\",\"tintColor\":\"#FFFFFF\",\"iconTintColor\":\"#FFFFFF\",\"backgroundColor\":\"#5B51DE\",\"testInfo\":{\"automatizationId\":\"badge-reviewPayout\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"},\"secondLeftBottomBadge\":{\"text\":\"Распродажа\",\"image\":\"ic_s_hot_filled_compact\",\"tintColor\":\"#ffffffff\",\"iconTintColor\":\"#ffffffff\",\"backgroundColor\":\"#f1117eff\",\"testInfo\":{\"automatizationId\":\"badge-marketingSuperHigh\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1653713652\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"6WtZLDoqJixz2L29Cv2mWRxC50q8wKHvkqv6ZIomGMvZ\",\"custom\":{\"advertLite\":\"AMUBN_z6g7N5y4ITuphmuU2Pd4gaX0XFxmch5_mnlFbYfAMCsJ5CR2P4tlTJWXDaKjbYq3UJ6WuwSQJc\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"6WtZLDoqJixz2L29Cv2mWRxC50q8wKHvkqv6ZIomGMvZ\",\"custom\":{\"advertLite\":\"AMUBN_z6g7N5y4ITuphmuU2Pd4gaX0XFxmch5_mnlFbYfAMCsJ5CR2P4tlTJWXDaKjbYq3UJ6WuwSQJc\"}},\"click\":{\"actionType\":\"click\",\"key\":\"6WtZLDoqJixz2L29Cv2mWRxC50q8wKHvkqv6ZIomGMvZ\",\"custom\":{\"advertLite\":\"AMUBN_z6g7N5y4ITuphmuU2Pd4gaX0XFxmch5_mnlFbYfAMCsJ5CR2P4tlTJWXDaKjbYq3UJ6WuwSQJc\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"6WtZLDoqJixz2L29Cv2mWRxC50q8wKHvkqv6ZIomGMvZ\",\"custom\":{\"advertLite\":\"AMUBN_z6g7N5y4ITuphmuU2Pd4gaX0XFxmch5_mnlFbYfAMCsJ5CR2P4tlTJWXDaKjbYq3UJ6WuwSQJc\"}},\"view\":{\"actionType\":\"view\",\"key\":\"6WtZLDoqJixz2L29Cv2mWRxC50q8wKHvkqv6ZIomGMvZ\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/sistemnyy-blok-igrovoy-kompyuter-intel-xeon-e5-2650v3-ram-32-gb-ssd-512-gb-nvidia-geforce-gtx-1751822143/?at=83tBNrjEgFOJNKJRuWVoW9viRYY491hkRVN8KTRZYvR4\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"34 646 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"48 618 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−28%\",\"priceStyle\":{\"styleType\":\"SALE_PRICE\",\"gradient\":{\"startColor\":\"#F1117E\",\"endColor\":\"#F1117E\"}},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"blackFridayStockbar\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Осталось 299 шт\",\"textStyle\":\"tsBodyControl400Small\",\"textColor\":\"textAccent\",\"maxLines\":1,\"testInfo\":{\"automatizationId\":\"tile-blackFridayStockbar\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Системный блок Игровой компьютер (Intel Xeon E5-2650V3, RAM 32 ГБ, SSD 512 ГБ, NVIDIA GeForce GTX 1660 SUPER (6 Гб), Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.8  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"171 отзыв\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"16 апреля\",\"maxItems\":149,\"currentItems\":0,\"action\":{\"id\":\"1751822143\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"OgtE1GAMkIwORKKPI6AlZQoh2Mym4XTyRMz8jcMMQ6EG\",\"custom\":{\"advertLite\":\"AMUBMfYc-OlPVyUMlz8JbP4cTUgANW-9pyhthyKFVMZggfcoQAzUCKhtnzk9tGdxGPBlCjOpYVpEiSG1zQ\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}},\"expressButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"Завтра\",\"maxItems\":150,\"currentItems\":0,\"action\":{\"id\":\"1751822143\",\"quantity\":1,\"selectedDeliverySchema\":243},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"NOtwkRNzpcmnBmxLfYLRENoCGz5Y26fxAEgzkSl8zo5B\",\"custom\":{\"advertLite\":\"AMUBMfYc-OlPVyUMlz8JbP4cTUgANW-9pyhthyKFVMZggfcoQAzUCKhtnzk9tGdxGPBlCjOpYVpEiSG1zQ\"}}},\"testInfo\":{\"automatizationId\":\"expressAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY_EXPRESS\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"sellerIcon\":{\"sellerIconId\":\"ic_m_premium_circle_filled\",\"sellerIconBgColor\":\"#ffffff\",\"tintColor\":\"#ffb800\",\"testInfo\":{\"automatizationId\":\"premium-seller-icon\"}},\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1751822143\",\"tileDefer\":2,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-s/7405844824.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-e/7405844810.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-8/7405844876.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-k/7405844816.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Распродажа\",\"image\":\"ic_s_hot_filled_compact\",\"tintColor\":\"#ffffffff\",\"iconTintColor\":\"#ffffffff\",\"backgroundColor\":\"#f1117eff\",\"testInfo\":{\"automatizationId\":\"badge-marketingSuperHigh\"},\"theme\":\"STYLE_TYPE_MEDIUM\",\"iconPosition\":\"ICON_POSITION_LEFT\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1751822143\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"83tBNrjEgFOJNKJRuWVoW9viRYY491hkRVN8KTRZYvR4\",\"custom\":{\"advertLite\":\"AMUBMfYc-OlPVyUMlz8JbP4cTUgANW-9pyhthyKFVMZggfcoQAzUCKhtnzk9tGdxGPBlCjOpYVpEiSG1zQ\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"83tBNrjEgFOJNKJRuWVoW9viRYY491hkRVN8KTRZYvR4\",\"custom\":{\"advertLite\":\"AMUBMfYc-OlPVyUMlz8JbP4cTUgANW-9pyhthyKFVMZggfcoQAzUCKhtnzk9tGdxGPBlCjOpYVpEiSG1zQ\"}},\"click\":{\"actionType\":\"click\",\"key\":\"83tBNrjEgFOJNKJRuWVoW9viRYY491hkRVN8KTRZYvR4\",\"custom\":{\"advertLite\":\"AMUBMfYc-OlPVyUMlz8JbP4cTUgANW-9pyhthyKFVMZggfcoQAzUCKhtnzk9tGdxGPBlCjOpYVpEiSG1zQ\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"83tBNrjEgFOJNKJRuWVoW9viRYY491hkRVN8KTRZYvR4\",\"custom\":{\"advertLite\":\"AMUBMfYc-OlPVyUMlz8JbP4cTUgANW-9pyhthyKFVMZggfcoQAzUCKhtnzk9tGdxGPBlCjOpYVpEiSG1zQ\"}},\"view\":{\"actionType\":\"view\",\"key\":\"83tBNrjEgFOJNKJRuWVoW9viRYY491hkRVN8KTRZYvR4\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/sistemnyy-blok-bushidopc-v1-0-intel-xeon-e5-2650v2-ram-32-gb-ssd-1024-gb-amd-radeon-rx-580-8-gb-1748977832/?at=gpt4EklDJC5BRQ61CR6AANMs5MQ4qQc1zOJK2uDZ7krY\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"30 399 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"72 250 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−57%\",\"priceStyle\":{\"styleType\":\"CARD_PRICE\"},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_download_filled_compact\",\"tintColor\":\"bgPositivePrimary\"},\"title\":\"Стало дешевле\",\"titleColor\":\"\",\"testInfo\":{\"automatizationId\":\"tile-list-price-dropped\"}}],\"textStyle\":\"tsBodyM\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-labels\"}}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Системный блок BushidoPC v1.0 (Intel Xeon E5-2650V2, RAM 32 ГБ, SSD 1024 ГБ, AMD Radeon RX 580 (8 Гб), Windows 10 Pro), черный\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.9  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"146 отзывов\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"19 апреля\",\"maxItems\":3,\"currentItems\":0,\"action\":{\"id\":\"1748977832\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"gpt4EklDJC5BRQ61CR6AANMs5MQ4qQc1zOJK2uDZ7krY\",\"custom\":{\"advertLite\":\"AMUBf3FNYOlcHdYwTIwiI_9epjTokv86SOh8gJpp2e9_BzUXetACQyJ3xTB_0a-8nDqB-Y36_aaPE8KI7A\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1748977832\",\"tileDefer\":4,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-c/7438598184.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-7/7438598143.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-c/7436661744.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-c/7357720152.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-w/7137151772.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-i/7183862838.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Осталось 3 шт\",\"tintColor\":\"#FFFFFF\",\"backgroundColor\":\"bgAttentionPrimary\",\"testInfo\":{\"automatizationId\":\"badge-stock\"},\"theme\":\"STYLE_TYPE_MEDIUM\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1748977832\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"gpt4EklDJC5BRQ61CR6AANMs5MQ4qQc1zOJK2uDZ7krY\",\"custom\":{\"advertLite\":\"AMUBf3FNYOlcHdYwTIwiI_9epjTokv86SOh8gJpp2e9_BzUXetACQyJ3xTB_0a-8nDqB-Y36_aaPE8KI7A\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"gpt4EklDJC5BRQ61CR6AANMs5MQ4qQc1zOJK2uDZ7krY\",\"custom\":{\"advertLite\":\"AMUBf3FNYOlcHdYwTIwiI_9epjTokv86SOh8gJpp2e9_BzUXetACQyJ3xTB_0a-8nDqB-Y36_aaPE8KI7A\"}},\"click\":{\"actionType\":\"click\",\"key\":\"gpt4EklDJC5BRQ61CR6AANMs5MQ4qQc1zOJK2uDZ7krY\",\"custom\":{\"advertLite\":\"AMUBf3FNYOlcHdYwTIwiI_9epjTokv86SOh8gJpp2e9_BzUXetACQyJ3xTB_0a-8nDqB-Y36_aaPE8KI7A\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"gpt4EklDJC5BRQ61CR6AANMs5MQ4qQc1zOJK2uDZ7krY\",\"custom\":{\"advertLite\":\"AMUBf3FNYOlcHdYwTIwiI_9epjTokv86SOh8gJpp2e9_BzUXetACQyJ3xTB_0a-8nDqB-Y36_aaPE8KI7A\"}},\"view\":{\"actionType\":\"view\",\"key\":\"gpt4EklDJC5BRQ61CR6AANMs5MQ4qQc1zOJK2uDZ7krY\"}}},{\"action\":
\{\"behavior\":\"BEHAVIOR_TYPE_REDIRECT\",\"link\":\"/product/sistemnyy-blok-bushidopc-v1-0-intel-xeon-e5-2650v2-ram-32-gb-ssd-1024-gb-amd-radeon-rx-580-8-1995124423/?at=oZt624XQmC7D2PAmtXGgVLVcrOxWkgSlDr5qWuNEYllM\",\"params\":{\"target\":\"_blank\"}},\"brandLogo\":null,\"isAdult\":false,\"mainState\":[{\"type\":\"atom\",\"id\":\"atom\",\"atom\":{\"type\":\"priceV2\",\"priceV2\":{\"price\":[{\"text\":\"30 399 ₽\",\"textStyle\":\"PRICE\"},{\"text\":\"72 250 ₽\",\"textStyle\":\"ORIGINAL_PRICE\"}],\"discount\":\"−57%\",\"priceStyle\":{\"styleType\":\"CARD_PRICE\"},\"preset\":\"SIZE_500\",\"paddingBottom\":\"PADDING_200\"}}},{\"type\":\"atom\",\"id\":\"name\",\"atom\":{\"type\":\"textAtom\",\"textAtom\":{\"text\":\"Системный блок BushidoPC v1.0 (Intel Xeon E5-2650V2, RAM 32 ГБ, SSD 1024 ГБ, AMD Radeon RX 580 (8 Гб), Windows 10 Pro), черный матовый\",\"textStyle\":\"tsBodyL\",\"maxLines\":2,\"testInfo\":{\"automatizationId\":\"tile-name\"}}}},{\"atom\":{\"type\":\"labelList\",\"labelList\":{\"items\":[{\"icon\":{\"image\":\"ic_s_star_filled_compact\",\"tintColor\":\"graphicRating\"},\"title\":\"4.9  \",\"titleColor\":\"textPremium\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}},{\"icon\":{\"image\":\"ic_s_dialog_filled_compact\",\"tintColor\":\"graphicTertiary\"},\"title\":\"146 отзывов\",\"titleColor\":\"textSecondary\",\"testInfo\":{\"automatizationId\":\"tile-list-comments\"}}],\"textStyle\":\"tsBodyMBold\",\"maxLines\":1,\"align\":\"ALIGN_LEFT\",\"testInfo\":{\"automatizationId\":\"tile-list-rating\"}}}}],\"multiButton\":{\"theme\":\"THEME_TYPE_VERTICAL\",\"ozonButton\":{\"type\":\"addToCartButtonWithQuantity\",\"addToCartButtonWithQuantity\":{\"text\":\"19 апреля\",\"maxItems\":2,\"currentItems\":0,\"action\":{\"id\":\"1995124423\",\"quantity\":1},\"trackingInfo\":{\"click\":{\"actionType\":\"to_cart\",\"key\":\"oZt624XQmC7D2PAmtXGgVLVcrOxWkgSlDr5qWuNEYllM\",\"custom\":{\"advertLite\":\"AMUBF9aXZ6xY5a6hRlASPcNzzjmkRaIaYVlVweNujPbeubb_Pql81hYwMedNOv7wwlWbwdF3iwyW4J3kxg\"}}},\"testInfo\":{\"automatizationId\":\"ozonAddToCart\"},\"theme\":\"STYLE_TYPE_PRIMARY\",\"mode\":\"UPDATE_MODE_STEP\",\"buttonIconId\":\"ic_m_grocery_cart_filled\",\"qtyTextDisabled\":true,\"buttonSizeMode\":\"SIZE_MODE_FILL\"}}},\"skuId\":\"1995124423\",\"tileDefer\":4,\"tileImage\":{\"imageRatio\":\"3:4\",\"items\":[{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-2/7443230618.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-n/7443232403.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-c/7443230592.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-q/7443230606.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-v/7443230611.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}},{\"type\":\"image\",\"image\":{\"link\":\"https://cdn1.ozone.ru/s3/multimedia-1-6/7443230622.jpg\",\"contentMode\":\"SCALE_ASPECT_FIT\"}}],\"leftBottomBadge\":{\"text\":\"Осталось 2 шт\",\"tintColor\":\"#FFFFFF\",\"backgroundColor\":\"bgAttentionPrimary\",\"testInfo\":{\"automatizationId\":\"badge-stock\"},\"theme\":\"STYLE_TYPE_MEDIUM\"},\"secondLeftBottomBadge\":{\"text\":\"Новинка\",\"tintColor\":\"textLightKey\",\"backgroundColor\":\"bgPositivePrimary\",\"testInfo\":{\"automatizationId\":\"badge-novel\"},\"theme\":\"STYLE_TYPE_MEDIUM\"}},\"topRightButtons\":[{\"type\":\"favoriteProductMoleculeV2\",\"favoriteProductMoleculeV2\":{\"id\":\"1995124423\",\"isFav\":false,\"trackingInfo\":{\"click\":{\"actionType\":\"favorite\",\"key\":\"oZt624XQmC7D2PAmtXGgVLVcrOxWkgSlDr5qWuNEYllM\",\"custom\":{\"advertLite\":\"AMUBF9aXZ6xY5a6hRlASPcNzzjmkRaIaYVlVweNujPbeubb_Pql81hYwMedNOv7wwlWbwdF3iwyW4J3kxg\"}}},\"testInfo\":{\"favoriteButton\":{\"automatizationId\":\"favorite-button\"},\"unFavoriteButton\":{\"automatizationId\":\"unfavorite-button\"}}}}],\"trackingInfo\":{\"aux_click\":{\"actionType\":\"aux_click\",\"key\":\"oZt624XQmC7D2PAmtXGgVLVcrOxWkgSlDr5qWuNEYllM\",\"custom\":{\"advertLite\":\"AMUBF9aXZ6xY5a6hRlASPcNzzjmkRaIaYVlVweNujPbeubb_Pql81hYwMedNOv7wwlWbwdF3iwyW4J3kxg\"}},\"click\":{\"actionType\":\"click\",\"key\":\"oZt624XQmC7D2PAmtXGgVLVcrOxWkgSlDr5qWuNEYllM\",\"custom\":{\"advertLite\":\"AMUBF9aXZ6xY5a6hRlASPcNzzjmkRaIaYVlVweNujPbeubb_Pql81hYwMedNOv7wwlWbwdF3iwyW4J3kxg\"}},\"right_click\":{\"actionType\":\"right_click\",\"key\":\"oZt624XQmC7D2PAmtXGgVLVcrOxWkgSlDr5qWuNEYllM\",\"custom\":{\"advertLite\":\"AMUBF9aXZ6xY5a6hRlASPcNzzjmkRaIaYVlVweNujPbeubb_Pql81hYwMedNOv7wwlWbwdF3iwyW4J3kxg\"}},\"view\":{\"actionType\":\"view\",\"key\":\"oZt624XQmC7D2PAmtXGgVLVcrOxWkgSlDr5qWuNEYllM\"}}}],\"templates\":null,\"cols\":12,\"imageHeight\":500,\"page\":1}"

https://www.ozon.ru/product/ironcore-sistemnyy-blok-igrovoy-kompyuter-pk-air-7700x-amd-ryzen-7-7700x-ram-64-gb-ssd-2000-gb-1653513227/?at=6WtZLDoqJiLD7L5jTZPAWY5t97Q0DjinnJJBtln0ByN

https://www.ozon.ru/product/sevengroup-sistemnyy-blok-igrovoy-kompyuter-pk-intel-xeon-e5-2650-ram-32-gb-ssd-1024-gb-1768402974/?at=VvtzqvlY8toJM1zZsYo82lWsLXvpR2s7mYOzYcOZ1xLJ

https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094
https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/category/sistemnye-bloki-15704/?page=6
https://www.ozon.ru/category/sistemnye-bloki-15704/?page=6
https://www.ozon.ru/category/sistemnye-bloki-15704/?__rr=1&
layout_container=default&
layout_page_index=6&
page=6&
paginator_token=3635012&
search_page_state=eNbbaXgU9saDSiVJeBJ7wBlQr5pJbXl5Xuc4FHaM0Dln6C3Lqzfpcnak5u6gvTTegIueFdqA1mxcxpQaeJm7Nro0c6NNXqPIpebGgRsLM8h-3n4rg1zzNMQPHVRFLOuRvKZZtOzcZqXQTiVK8wdrRfSkwRgC8CFrl2TI_DP4mPJVO429Rcp4Kn2Mfj1w0dzfZO9eV6U%253D
&start_page_id=643906aac3effa1a9031863301fee5db/

https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=%2Fproduct%2Fonkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094&__rr=1&abt_att=1
            '''
            catalogUrl = ''
            catalogUrl = 'https://www.ozon.ru/category/sistemnye-bloki-15704/'

            results = []
            categoryPage = 0
            categoryPage = 7

            pageCount = 3
            pageCount = 1
            for categoryPage in range(1, pageCount+1):
                category=f'/category/sistemnye-bloki-15704/?page={categoryPage}'
                catalogUrl = f'https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url={category}'
                uargs = ('From: ',catalogUrl)
                lg.save(' '.join(uargs))
                # urls = [url]

                # https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/category/sistemnye-bloki-15704/?page=7
                urls = getUrls(catalogUrl, wd)
                # _print(f'line: {line()}')
                lg.logTime(f'got urls: {len(urls)}')
                _results = getPages(wd, urls)
                results.extend(_results)
            uniclen = set()
            if results:
                num=0
                for item in results:
                    _print('-'*10, num);num+=1
                    _print('Title:', item['title'])
                    _print()
                    uniclen.add(item['title'])


            setconf('log', True)
            setconf('logprint', True)

            lg.logTime(f'Total load: {len(results)}')
            lg.logTime(f'Total unique: {len(uniclen)}')
            _print('try to dumps')
            # srcdump = json.dumps(dpsrc,indent=4)
            # srcdump = json.dumps(dumptusave,indent=4)
            srcdump = json.dumps(results,indent=4)

            # save dump for observe
            # _print(srcdump)
            lg.logTime('get json end')

            if srcdump:
                out_file_name = 'content.json'
                saveData(srcdump, out_file_name)
        except Exception as ex:
            _print(ex)
            lg.logTime('get json error '+ f'line: {line()}')

        # tsp=4
        # tsp=100
        # time.sleep(tsp)
        # time.sleep(100)
        # lg.logTime(f'Timeout {tsp}')
        cookies = wd.get_cookies()
        with open(f'.{fn}','wb') as hendl: # relative file path
            pickle.dump(cookies, hendl)
            lg.logTime('cookies saved')
    except Exception as ex:
        _print(ex)
        print(ex)
        lg.logTime('parse error')


lg.logTime('Finish.')
lg.end()
def process(url):
    ...

urls = [
    1,2,3
]

if __name__ == '__main__':
    ...
    p = Pool(processes=3)
    p.map(process, urls)


def calcBetweenTimes(ntime=1775861041,ctime=0,com=''):
    if com: com+=': '
    if ctime==0: ctime = time.time()
    _print()
    _print(ntime)
    _print(ctime)
    between = ntime - int(time.time()) 
    _print()
    _print(between)
    betw=between
    h = betw//3600
    bt = betw-(h*3600)
    m = bt//60
    s = int(bt-(m*60))
    ms = int((bt-int(bt))*10000)
    tpl='{0:02d}h {1:02d}m {2:02d}s .{3:04d}ms '
    args = (com,'between:',tpl.format(int(h),int(m),s, ms))
    _print(*args)


calcBetweenTimes(1775861041,0,'')
calcBetweenTimes(1744154153,0,'')
calcBetweenTimes(1744154153,0,'')
_print('ADDRESSBOOKBAR_WEB_CLARIFICATION',ADDRESSBOOKBAR_WEB_CLARIFICATION)