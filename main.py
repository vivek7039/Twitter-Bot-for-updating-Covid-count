import time as t
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

CHROME_DRIVER_PATH = "CHROME_DRIVER_PATH"
TWITTER_EMAIL = "XYZ.com"
TWITTER_PASSWORD = "XYZ"


class CovidInfoTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.infected = 0
        self.cured = 0
        self.dead = 0

    def get_counts(self):
        self.driver.get("https://www.worldometers.info/coronavirus/country/india/")
        t.sleep(3.0)
        self.infected = self.driver.find_element_by_xpath('//*[@id="maincounter-wrap"]/div/span').text
        self.cured = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[6]/div/span').text
        self.dead = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[5]/div/span').text
        self.driver.quit()
    def tweetit(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        t.sleep(2)
        password.send_keys(Keys.ENTER)
        t.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Infected: {self.infected} Cured:{self.cured} Dead: {self.dead}"
        tweet_compose.send_keys(tweet)
        t.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        t.sleep(2)
        self.driver.quit()



bot = CovidInfoTwitterBot(CHROME_DRIVER_PATH)
bot.get_counts()
bot.tweetit()
