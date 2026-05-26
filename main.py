from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import time
import os
import csv
import userAgent
import socialLinks as SL

class Clickbot:
    def __init__(self):
        # Set up Chrome options
        self.options = Options()
        self.options.set_capability("deviceOrientation", "landscape")
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument("--disable-blink-features")
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        # Path to chromedriver
        self.service = Service(r"E:\New folder\mrudula\kjsce\Internship\DEEPCYTES\DEEPCYTES Red Team\clickbot\drivers\chromedriver.exe")
        self.browser = webdriver.Chrome(service=self.service, options=self.options)

        # Initialize instance attributes
        self.rand_url = random.randrange(1, 17, 1)
        self.random_element = random.randrange(0, 6, 1)
        self.random_time = random.randrange(5, 30, 1)
        self.count = 0

        self.timezones = [
            "America/Chicago", "America/New_York", "America/Los_Angeles", "US/Eastern",
            "America/Phoenix", "America/Guatemala", "America/Detroit", "America/Denver",
            "America/Cambridge_Bay", "America/Belize"
        ]

        self.resolutions = [
            '480x800', '360x740', '480x853', '600x960', '360x800', '360x820', '360x780',
            '360x720', '337x512', '360x640', '320x534', '412x869', '412x846', '428x926',
            '414x896', '390x844'
        ]

        self.user_agent = random.choice(userAgent.headers_list)

    def startbrowser(self):
        self.browser.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": self.user_agent})
        tz_params = {'timezoneId': random.choice(self.timezones)}
        self.browser.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)

    def gotourl(self):
        wait = WebDriverWait(self.browser, 120)
        rnd = random.randrange(0, 10, 1)
        link = SL.url
        self.browser.get(link[rnd])
        time.sleep(self.random_time)

    def scrollthepage(self, counted):
        self.browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/10))")
        time.sleep(random.randrange(1, 5))
        self.browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/8))")
        time.sleep(random.randrange(4, 10))
        self.browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/6))")
        time.sleep(random.randrange(1, 7))
        self.browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*2/5))")
        time.sleep(random.randrange(1, 5))
        self.browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2))")
        time.sleep(random.randrange(5, 10))
        self.browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4))")
        time.sleep(random.randrange(1, 3))
        if counted % 3 == 0:
            self.browser.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/4))")

    def clickfirstelem(self, count_val):
        wait = WebDriverWait(self.browser, 120)
        rnd3 = random.randrange(1, 10, 1)
        rnd4 = random.randrange(1, 5, 1)

        if count_val % 3 == 0:
            elem = wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, f"//*[@id='newsup_posts_list-2']/div/div[2]/div[{rnd3}]/ul/li/div[2]/h5/a")))
        else:
            elem = wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, f"//*[@id='block-3']/div/div/ul/li[{rnd4}]/a")))

        webdriver.ActionChains(self.browser).click(elem).perform()

    def clearcookies(self):
        WebDriverWait(self.browser, 120)
        self.browser.delete_all_cookies()
        self.browser.execute_script('window.localStorage.clear();')

    def restartsession(self):
        rnd2 = random.randrange(12, 17, 1)
        url = SL.url
        self.browser.get(url[rnd2])

    def savecookies(self):
        WebDriverWait(self.browser, 120)
        rand_count = random.randrange(10, 99, 1)
        cookies = self.browser.get_cookies()
        keys = cookies[0].keys()
        keys2 = ['userAgent']
        with open(f'cookies/cookies-{rand_count}.csv', 'w', encoding='UTF8', newline='') as f:
            doc = csv.DictWriter(f, fieldnames=keys)
            doc.writeheader()
            doc.writerows(cookies)

        with open(f'uagents/ua-{rand_count}.csv', 'w', encoding='UTF8', newline='') as f:
            doc2 = csv.DictWriter(f, fieldnames=keys2)
            doc2.writeheader()
            doc2.writerow({"userAgent": self.user_agent})

    def retrievecookies(self):
        file = random.choice(os.listdir(r"E:\New folder\mrudula\kjsce\Internship\DEEPCYTES\DEEPCYTES Red Team\clickbot\cookies"))
        filename = os.path.basename(file)
        randvalue = filename[-6:-4]
        with open(f"E:/New folder/mrudula/kjsce/Internship/DEEPCYTES/DEEPCYTES Red Team/clickbot/uagents/ua-{randvalue}.csv", encoding='UTF8') as ua:
            current_agent = csv.DictReader(ua)
            browser_agent = list(current_agent)
        self.browser.execute_cdp_cmd("Network.setUserAgentOverride", random.choice(browser_agent))
        tz_params = {'timezoneId': random.choice(self.timezones)}
        self.browser.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)
        rnd = random.randrange(0, 20, 1)
        link = SL.url
        self.browser.get(link[rnd])
        WebDriverWait(self.browser, 120)
        with open(f"E://New folder/mrudula/kjsce/Internship/DEEPCYTES/DEEPCYTES Red Team/clickbot/cookies/{file}", encoding='utf-8-sig') as cf:
            cr = csv.DictReader(cf)
            list_cookies = list(cr)
            for line in list_cookies:
                if 'secure' in line:
                    del line['secure']
                if 'expiry' in line:
                    del line['expiry']
                if 'httpOnly' in line:
                    del line['httpOnly']
                self.browser.add_cookie(line)
        time.sleep(random.randrange(1, 20, 1))

    def mobilevisitor(self):
        WebDriverWait(self.browser, 120)
        res = random.choice(self.resolutions)
        res1 = res.split("x")
        self.browser.set_window_size(int(res1[0]), int(res1[1]), self.browser.window_handles[0])
        self.browser.get("https://nairobi24.co.ke")

    def visitotherpages(self):
        rnd = random.randrange(5, 10, 1)
        self.browser.get("https://nairobi24.co.ke")
        elem = WebDriverWait(self.browser, 120).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[@id='menu-item-{rnd}']/a")))
        webdriver.ActionChains(self.browser).click(elem).perform()
        self.scrollthepage()

        elem2 = WebDriverWait(self.browser, 120).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[@id='post-349']/div[1]/div/article[{rnd}]/div[2]/h4/a")))

# Main loop
if __name__ == "__main__":
    while True:
        bot = Clickbot()
        bot.startbrowser()
        bot.gotourl()
        if bot.count % 2 != 0:
            bot.scrollthepage(bot.count)
            bot.clickfirstelem(bot.count)
            bot.scrollthepage(bot.count)

        time.sleep(10)
        bot.savecookies()
        bot.clearcookies()
        bot.restartsession()
        time.sleep(random.randrange(15, 30, 1))
        bot.clearcookies()
        bot.restartsession()
        time.sleep(random.randrange(0, 10, 1))
        bot.scrollthepage(bot.count)
        bot.clickfirstelem(bot.count)
        time.sleep(random.randrange(1, 10, 1))
        bot.clearcookies()
        time.sleep(random.randrange(5, 10, 1))
        bot.count += 1
        print(bot.count)
