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
from libs.env import envservstat

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


script_name = 'OZY'
script_version = '0.2.000' # 0.1
lg = POLog()
lg.logTime()
lg.logTime('Start.')
# lg.logTime('Start.', start_colr=color.GREEN)

# log config settings
setconf('print', False)
# setconf('log', False)
# setconf('logprint', False)

isserv = 10
isserv = envservstat
hendless=False
hendless=True

category='/category/sistemnye-bloki-15704/?page=7'
categoryPage = 0
categoryPage = 7
category=f'/category/sistemnye-bloki-15704/?page={categoryPage}'


def intro():
    title = (Fore.GREEN + 'start' + Fore.RESET)
    _print(title)
    # title = 'OZY v0.1'
    title = f'{script_name} v{script_version}'
    t = art.text2art(title, 'epic')
    title = (Fore.GREEN + t + Fore.RESET)
    print(title)

intro()


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

if isserv :
    from chromedriver_py import binary_path



lg.logTime('libs loaded')

# Select browser driver
way='f'
way='c'


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
        self.driver.close()
        self.driver.quit()

        lg.logTime('driver exit')

    def __aenter__(self):
        return self.driver

    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver.quit()


class Ozy:
    driver = False
    catalogTargetUrls = [] # array
    catalogUrl = False # str
    strategy = 'catalog' # parsing strategy
    driver_way='c'
    way='c'
    strategy='catalog'
    category = False
    categories = False
    pfrom = 1
    pcou = 1
    url = 'https://www.ozon.com'
    url = 'https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/onkron-kronshteyn-dlya-monitora-nastolnyy-13-32-dyuymov-g45-chernyy-podstavka-pod-monitor-do-8-kg-1429652094'
    domine = 'www.ozon.ru'
    def __init__(self, urls=[],strategy='catalog', driver='c',**kwargs):
        '''
        urls -- url catalog list
        '''
        self.driver_way = driver
        self.way = driver
        self.strategy = strategy
        self.init(urls,**kwargs)
    
    def init(self, urls,**kwargs):
        if urls:
            if isinstance(urls, str):
                urls = [urls]
            self.catalogTargetUrls = urls
        
        key = 'category'
        if key in kwargs:
            setattr(self, key, kwargs[key])
        key = 'pfrom'
        if key in kwargs:
            setattr(self, key, kwargs[key])
        key = 'pcou'
        if key in kwargs:
            setattr(self, key, kwargs[key])

        self.scenario()

        lg.logTime(f'pages from: {self.pfrom}, count: {self.pcou}')

    
    def scenario(self):
        if self.strategy == 'catalog':
            ...
        if self.strategy == 'catalog-test':
            self.initTestUrls()
    
    def initTestUrls(self):
        '''
        init testing urls
        '''
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

        self.url = url
        self.category = '/category/sistemnye-bloki-15704/'

    def process(self, urls=False,**kwargs):
        '''
        urls -- target urls list
        '''
        # self.catalogUrl = self.urls = []
        self.init(urls,**kwargs)

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
            options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        lg.logTime('started {} hendless'.format('as'if hendless else 'without'))
        usag = UserAgent()
        if way == 'c':
            # extension_path = "V:\\VISHESH AGRAWAL\\Chrome Extension\\Word Counter"
            # __tests/po_py/ectensions/chr_ext_001/popup.js
            extension_path = os.path.dirname(os.path.realpath(__file__))+'/ectensions/chr_ext_001/'
            __dir_user = os.path.dirname(os.path.realpath(__file__))+'/__chr_user_data/'
            # extension_path = binary_path
            # if isserv :
            #     chrWebDrivPath = binary_path
            #     print('binary_path', binary_path)
                # options.add_argument('--user-data-dir='+__dir_user)
                
            #     options.add_argument("load-extension=" + binary_path)
            # else:
            options.add_argument("load-extension=" + extension_path)
            # print('chr extension',options['load-extension'])
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
                # driver = webdriver.Chrome(service=Service(executable_path=chrWebDrivPath), options=options)
                driver = webdriver.Chrome(service=Service(executable_path=chrWebDrivPath), options=options)
                # driver = webdriver.Remote("http://localhost:4444", options=webdriver.ChromeOptions())
                # driver = webdriver.Remote("http://localhost:4444", options=options)
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
            driver.execute_script("return navigator.userAgent")

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

        # if way == 'c':
        #     stealth(driver,
        #             languages=["en-US", "en"],
        #             vendor="Google Inc.",
        #             platform="Win32",
        #             webgl_vendor="Intel Inc.",
        #             renderer="Intel Iris OpenGL Engine",
        #             fix_hairline=True,
        #             )


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


        self.ADDRESSBOOKBAR_WEB_CLARIFICATION=int(time.time())+(365*86400)
        self.ADDRESSBOOKBAR_WEB_CLARIFICATION=int(time.time())-(50*3600)

        self.cook2={
            'abt_data':'7.iWq6ZJ5BOM8LktW0d5k7US_wuYpTuNxczY_dSZ3kHKyABU_Oe-9OFMJRaBo8Pit5Eu5GpuRdlrWncHempy70axaRMqYcJJGbE65pRSYIn5Qt8StjVEXEMMomrKdlHvkW5GSWYiy6fXH621HVSdtjq6QV8iNpZWeu8aNsM-HfxBNDdV9R5dm6YIqfN5Oisb6UuRWkDui_uVk608f8Gji9IiI6p6y_Rw7jsXmcT0cZyyi7BecEscO4ZYkhpdiH-LgOoL632WDI4X08BnDdtlc_iIUzccYxyFSZeI7ZvWP_N7M-bvXJr5lWC8mL7gHz9CVqIE-j2418wF2PGawKYZVyYT6tMh07sSr_qWYhfc6q8fyRx3Sae9uUCIOkofFGTSU7EvTSiEQKss8vXQsciTuGm29VOZwAxhdbg-EEFNZOrOA5MNLM6EcupSJCO-p1iOoLFr3MGrsj9wifg7JvgIjBBf-SBXPmYeG2yUf9',
            '__Secure-refresh-token':'7.0.Y6cGNICVQRmhC8DKgrLkPQ.60.ASnBFsuUyp5ZIIZcMeE_4d9u_Rn733S4Ez94hQnsnu8ZAJrE889nzRzW2OScVDiUNw..20250411005106.A0VvzhczfCuRbXWkpEb9oVygIBGjzwVNWTLzD1eYYQc.1e6ab2286534600ce',
            '__Secure-ETC':'d44e290d024bef62205d5e9287076c9d',
            # 'ADDRESSBOOKBAR_WEB_CLARIFICATION':'1744154153',
            'ADDRESSBOOKBAR_WEB_CLARIFICATION': str(self.ADDRESSBOOKBAR_WEB_CLARIFICATION),
            '__Secure-user-id':'0',
            '__Secure-ext_xcid':'e6f1ddbf8a6eca300b1123bab4b38461',
            '__Secure-access-token':'7.0.Y6cGNICVQRmhC8DKgrLkPQ.60.ASnBFsuUyp5ZIIZcMeE_4d9u_Rn733S4Ez94hQnsnu8ZAJrE889nzRzW2OScVDiUNw..20250411005106.h95BhVm-PAPfS5QndXAzUULVn_wUFhIpWwwq_LqbAgg.1a46ca17badb5de8',
            'rfuid':'NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxOTg5NTUxNDI1LC0xLC0zNjI5NDkyMzIsVzNzaWJtRnRaU0k2SWxCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxbElGQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMXBkVzBnVUVSR0lGWnBaWGRsY2lJc0ltUmxjMk55YVhCMGFXOXVJam9pVUc5eWRHRmliR1VnUkc5amRXMWxiblFnUm05eWJXRjBJaXdpYldsdFpWUjVjR1Z6SWpwYmV5SjBlWEJsSWpvaVlYQndiR2xqWVhScGIyNHZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlN4N0luUjVjR1VpT2lKMFpYaDBMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4xZGZTeDdJbTVoYldVaU9pSk5hV055YjNOdlpuUWdSV1JuWlNCUVJFWWdWbWxsZDJWeUlpd2laR1Z6WTNKcGNIUnBiMjRpT2lKUWIzSjBZV0pzWlNCRWIyTjFiV1Z1ZENCR2IzSnRZWFFpTENKdGFXMWxWSGx3WlhNaU9sdDdJblI1Y0dVaU9pSmhjSEJzYVdOaGRHbHZiaTl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOUxIc2lkSGx3WlNJNkluUmxlSFF2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZWMTlMSHNpYm1GdFpTSTZJbGRsWWt0cGRDQmlkV2xzZEMxcGJpQlFSRVlpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgxZCxXeUp5ZFMxU1ZTSmQsMCwxLDAsMjQsMjM3NDE1OTMwLDgsMjI3MTI2NTIwLDEsMSwwLC0xLFIyOXZaMnhsSUVsdVl5NGdUbVYwYzJOaGNHVWdSMlZqYTI4Z1RHbHVkWGdnZURnMlh6WTBJRFV1TUNBb1dERXhPeUJNYVc1MWVDQjRPRFpmTmpRcElFRndjR3hsVjJWaVMybDBMelV6Tnk0ek5pQW9TMGhVVFV3c0lHeHBhMlVnUjJWamEyOHBJRU5vY205dFpTODVOaTR3TGpRMk5qUXVORFVnVTJGbVlYSnBMelV6Tnk0ek5pQXlNREF6TURFd055Qk5iM3BwYkd4aCxleUpqYUhKdmJXVWlPbnNpWVhCd0lqcDdJbWx6U1c1emRHRnNiR1ZrSWpwbVlXeHpaU3dpU1c1emRHRnNiRk4wWVhSbElqcDdJa1JKVTBGQ1RFVkVJam9pWkdsellXSnNaV1FpTENKSlRsTlVRVXhNUlVRaU9pSnBibk4wWVd4c1pXUWlMQ0pPVDFSZlNVNVRWRUZNVEVWRUlqb2libTkwWDJsdWMzUmhiR3hsWkNKOUxDSlNkVzV1YVc1blUzUmhkR1VpT25zaVEwRk9UazlVWDFKVlRpSTZJbU5oYm01dmRGOXlkVzRpTENKU1JVRkVXVjlVVDE5U1ZVNGlPaUp5WldGa2VWOTBiMTl5ZFc0aUxDSlNWVTVPU1U1SElqb2ljblZ1Ym1sdVp5SjlmU3dpY25WdWRHbHRaU0k2ZXlKUGJrbHVjM1JoYkd4bFpGSmxZWE52YmlJNmV5SkRTRkpQVFVWZlZWQkVRVlJGSWpvaVkyaHliMjFsWDNWd1pHRjBaU0lzSWtsT1UxUkJURXdpT2lKcGJuTjBZV3hzSWl3aVUwaEJVa1ZFWDAxUFJGVk1SVjlWVUVSQlZFVWlPaUp6YUdGeVpXUmZiVzlrZFd4bFgzVndaR0YwWlNJc0lsVlFSRUZVUlNJNkluVndaR0YwWlNKOUxDSlBibEpsYzNSaGNuUlNaWEYxYVhKbFpGSmxZWE52YmlJNmV5SkJVRkJmVlZCRVFWUkZJam9pWVhCd1gzVndaR0YwWlNJc0lrOVRYMVZRUkVGVVJTSTZJbTl6WDNWd1pHRjBaU0lzSWxCRlVrbFBSRWxESWpvaWNHVnlhVzlrYVdNaWZTd2lVR3hoZEdadmNtMUJjbU5vSWpwN0lrRlNUU0k2SW1GeWJTSXNJa0ZTVFRZMElqb2lZWEp0TmpRaUxDSk5TVkJUSWpvaWJXbHdjeUlzSWsxSlVGTTJOQ0k2SW0xcGNITTJOQ0lzSWxnNE5sOHpNaUk2SW5nNE5pMHpNaUlzSWxnNE5sODJOQ0k2SW5nNE5pMDJOQ0o5TENKUWJHRjBabTl5YlU1aFkyeEJjbU5vSWpwN0lrRlNUU0k2SW1GeWJTSXNJazFKVUZNaU9pSnRhWEJ6SWl3aVRVbFFVelkwSWpvaWJXbHdjelkwSWl3aVdEZzJYek15SWpvaWVEZzJMVE15SWl3aVdEZzJYelkwSWpvaWVEZzJMVFkwSW4wc0lsQnNZWFJtYjNKdFQzTWlPbnNpUVU1RVVrOUpSQ0k2SW1GdVpISnZhV1FpTENKRFVrOVRJam9pWTNKdmN5SXNJa3hKVGxWWUlqb2liR2x1ZFhnaUxDSk5RVU1pT2lKdFlXTWlMQ0pQVUVWT1FsTkVJam9pYjNCbGJtSnpaQ0lzSWxkSlRpSTZJbmRwYmlKOUxDSlNaWEYxWlhOMFZYQmtZWFJsUTJobFkydFRkR0YwZFhNaU9uc2lUazlmVlZCRVFWUkZJam9pYm05ZmRYQmtZWFJsSWl3aVZFaFNUMVJVVEVWRUlqb2lkR2h5YjNSMGJHVmtJaXdpVlZCRVFWUkZYMEZXUVVsTVFVSk1SU0k2SW5Wd1pHRjBaVjloZG1GcGJHRmliR1VpZlgxOWZRPT0sNjUsLTEyODU1NTEzLDEsMSwtMSwxNjk5OTU0ODg3LDE2OTk5NTQ4ODcsODM1OTM2NjM0LDI=',
            'xcid':'e6f1ddbf8a6eca300b1123bab4b38461',
            '__Secure-ab-group':'60',
            }

        nextTime=int(time.time())+(365*86400)
        self.cookdict = {
            "domain": "www.ozon.ru",
            "expiry": nextTime, #1775861041,
            "httpOnly": True,
            "name": "__Secure-ETC",
            "path": "/",
            "sameSite": "None",
            "secure": True,
            "value": "2cb43aca32027c5015f8eb6ef31b60b3"
        }

        self.driver = driver
        self.extract(self.url)


    def extract(self, url):
        # with WebDriver(webdriver.Chrome(**webdkargs)) as wd:
        hasErr=True
        hasErr=False
        print('strategy:\033[96m\033[1m', self.strategy, '\033[0m', line(), end='\n')
        print('cold url:\033[96m\033[1m', url, '\033[0m', line(), end='\n')
        with WebDriver(self.driver) as wd:
            try:
                print(url)
                lg.logTime('parse start')
                wd.get(url)
                lg.logTime('page get')

                coo_keys = 'cookeys_123456'
                fn = f'/resrs/{coo_keys}_{way}_cookies' # resrs -- resorces
                self.addCookies(fn, False, wd)

                try:
                    lg.logTime('get json start')
                    catalogUrl = ''
                    catalogUrl = 'https://www.ozon.ru/category/sistemnye-bloki-15704/'
                    self.jsonnGateway = 'https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url='

                    results = []
                    categoryPage = 0
                    categoryPage = 7

                    pageCount = 3
                    pageCount = self.pcou
                    for categoryPage in range(self.pfrom, pageCount+1):
                        category=f'{self.category}?page={categoryPage}'
                        catalogUrl = f'{self.jsonnGateway}{category}'
                        
                        uargs = ('From: ',catalogUrl)
                        lg.save(' '.join(uargs))
                        # urls = [url]

                        # get catalog
                        # https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/category/sistemnye-bloki-15704/?page=7
                        urls = self.getUrls(catalogUrl, wd)
                        # _print(f'line: {line()}')
                        lg.logTime(f'got urls: {len(urls)}')
                        
                        # get page item
                        _results = self.getPages(wd, urls)
                        results.extend(_results)
                    uniclen = set()
                    if results:
                        num=0
                        for item in results:
                            print('-'*10, num);num+=1
                            print('Title:', item['title'])
                            print()
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
                        self.saveData(srcdump, out_file_name)
                except Exception as ex:
                    _print(ex)
                    lg.logTime('get json error '+ f'line: {line()}')

                # tsp=4
                # tsp=100
                # time.sleep(tsp)
                # time.sleep(100)
                # lg.logTime(f'Timeout {tsp}')
                self.saveCookies(fn, wd)
            except Exception as ex:
                _print(ex)
                print(ex)
                lg.logTime('parse error')
    


    def decodeUnucode(self, str):
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
        


    def getData(self, jsnin):
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

    def saveData(self, jsn,file_name = 'content.json'):
        """
        jsn complited data
        """
        global lg
        srcdump = jsn
        with open(f'./result/{file_name}', 'w') as cjhend:
            cjhend.write(srcdump)
            lg.logTime('json saved')


    def getContent(self, url, driver, getAsJson = True):
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

            loaded = False

            coo_keys = 'cookeys_123456'
            fn = f'/resrs/{coo_keys}_{way}_cookies' # resrs -- resorces
            coore = 2
            stage = 'nothing'
            for i in range(20): # 10
                element = False

                title = driver.title
                if title == 'Antibot Challenge Page':
                    stage = 'wait'
                if title == 'Доступ ограничен':
                    stage = 'btnClick'

                _print('title',title)
                _print('stage', stage)
                
                if stage == 'wait' :
                    _print('! title',title)
                    _print('! stage', stage)
                    sec=2
                    _print(color.GREEN + f'sleep +{sec}s ({i})' + color.END )
                    time.sleep(sec)
                    continue
                    print('never work')
                if stage == 'wait' :
                    _print('never work')
                try:

                    if stage == 'btnClick' :
                        _print('! title',title)
                        _print('! stage', stage)
                        sec=2
                        time.sleep(sec)
                        try:
                            sec=2
                            time.sleep(sec)
                            _element = driver.find_element(By.CSS_SELECTOR, 'button#reload-button.rb')
                            _element.click()
                            _print(color.GREEN + f'click +{sec}s ({i})' + color.END )
                        except Exception as ex:
                            _print( f'click fail. line: {line()}')
                            _print(ex.msg, f'line: {line()}')
                        continue

                    # driver.execute_script("document.querySelector('#g-recaptcha-response-1').setAttribute('style', 'width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px;');")
                    driver.execute_script("document.querySelector('body').setAttribute('data-ts-ozy', 'ozy-test');")
                    # _print(type(htpsrc))
                    element = driver.find_element(By.TAG_NAME, 'pre')
                    # _print(jpsrc)
                    loaded = True
                except Exception as ex:
                        # print(ex.split('\n')[0])
                        # print(ex)
                        _print(ex.msg, f'line: {line()}')
                        # a=[print(att) for att in dir(ex)]
                        # class="rb"
                if not element:
                    print(driver.page_source)
                    lg.logTime(f'html filed. try {i}')
                    print(driver.title)
                    sec=7
                    _print(color.RED + f'sleep +{sec}s' + color.END )
                    time.sleep(sec)
                    self.saveCookies(fn, wd, True)
                    driver.get(url)
                    cookieReload = False
                    if coore:
                        cookieReload = True
                    self.addCookies(fn, cookieReload, wd)
                    if coore>0:
                        coore-=1
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
            if not loaded:
                _print(wd.page_source)
                lg.logTime('html out')

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


    def getPages(self, wd,urls):
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
            jsnin = self.getContent(jsonUrl, wd, getAsJson)
            if not jsnin:
                continue
            # _print('getPages ...', f'line: {line()}')
            jsn = self.getData(jsnin)
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



    def getUrls(self, catalogUrl='',driver=False):
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
            _print(msg)
            html = self.getContent(catalogUrl, wd, getAsJson)
            if not html:
                return urls
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
                            _print(ex)
                            msg = ex.msg
                            msg = (Fore.GREEN + msg + Fore.RESET)
                            _print(msg, f'line: {line()}')
                    # dump('urls', urls)

            msg = (Fore.GREEN + 'end get catalog' + Fore.RESET)
            _print(msg)


    # widgetStates
    # searchResultsV2-3669723-default-4

            # time.sleep(5)
            # time.sleep(5)
            # time.sleep(5)
        except Exception as ex:
            _print(ex)
            msg = ex.msg
            msg = (Fore.GREEN + msg + Fore.RESET)
            _print(msg, f'line: {line()}')
        return urls


    def addCookies(self, coofname, hasErr, wd):
        fn = coofname
        pdest = os.path.dirname(os.path.realpath(__file__))+fn # path for cookies
        dest_ex = os.path.isfile(pdest)
        # if not hasErr:
        try:
            ...
            if hasErr:
                raise ValueError('cercles with no data')
            if dest_ex:
                print ('fl exists:',fn)
                with open(f'.{fn}','rb') as hendl: # relative file path
                    cookies = pickle.load( hendl)
                    # cookies = cook2
                    lg.logTime('cookies add')
                    # _print('cookies')
                    # _print(cookies)
                    for cookie in cookies:
                        # cookie['domain'] = 'www.ozon.ru'
                        # cookie['domain'] = self.domine
                        # cooJsn = json.dumps(cookie,indent=4)
                        # _print(cooJsn)
                        wd.add_cookie(cookie)
                    #     lg.logTime("cookie:\n"+cooJsn)

        except Exception as ex:
            _print(ex, f'line: {line()}')
            lg.logTime('cookies error')
            _print('COOKS 2')
            for cookN,cookV in self.cook2.items():
                self.cookdict['name'] = cookN
                self.cookdict['value'] = cookV
                # _print(f'{cookN:20}',cookV)
                wd.add_cookie(self.cookdict)


    def saveCookies(self, coofname, wd, logdump=False):
        fn = coofname
        cookies = wd.get_cookies()
        if logdump:
            _print('cookies log dump:')
            for coo in cookies:
                _print(type(coo))
                _print(coo)
                # _cook = json.loads(cookies)
                _cook = json.dumps(coo, indent=4)
                _print(_cook)
        with open(f'.{fn}','wb') as hendl: # relative file path
            pickle.dump(cookies, hendl)
            lg.logTime('cookies saved')

def process(url):
    catalogUls = [
        url
    ]
    way = 'c'
    scenario = 'catalog-test'
    scenario = 'catalog'
    ozy = Ozy(catalogUls, scenario, way)
    category = '/category/sistemnye-bloki-15704/'
    category = '/category/monitory-15738/'
    pfrom=1;
    pcou=1
    settings = {
        'category': category,
        'pfrom': pfrom,
        'pcou': pcou,
    }
    ozy.process(**settings)

    lg.logTime('Finish.')
    lg.end()

urls = [
    ''
]

if __name__ == '__main__':
    ...
    p = Pool(processes=3)
    p.map(process, urls)


def calcBetweenTimes(ntime=1775861041,ctime=0,com=''):
    '''
    ntime -- needed time
    ctime -- current time
    com -- comment, message prefix
    '''
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


# calcBetweenTimes(1775861041,0,'')
# calcBetweenTimes(1744154153,0,'')
# calcBetweenTimes(1744154153,0,'')
# _print('ADDRESSBOOKBAR_WEB_CLARIFICATION',ozy.ADDRESSBOOKBAR_WEB_CLARIFICATION)