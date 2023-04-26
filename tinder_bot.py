from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import credentials
from time import sleep
from random import random, uniform


class TinderBot():
    def __init__(self) -> None:
        service = Service(
            executable_path="./chromedriver_mac_arm64/chromedriver")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self) -> None:
        # Go Tinder
        self.driver.get("https://tinder.com")

        sleep(2)

        # Login button
        self.driver.find_element(
            By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()

        sleep(2)

        # Connect with Facebook
        self.driver.find_element(
            By.XPATH, '//*[@id="o697594959"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div').click()

        sleep(2)

        # Switch popup window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        sleep(1)
        # Type email/password:
        self.driver.find_element(
            By.XPATH, '//*[@id="email"]').send_keys(credentials.EMAIL)
        self.driver.find_element(
            By.XPATH, '//*[@id="pass"]').send_keys(credentials.PASSWORD)

        sleep(1.5)
        self.driver.find_element(
            By.XPATH, '//input[contains(@value, "Log In")]').click()

        sleep(4)
        self.driver.switch_to.window(base_window)
        sleep(2)

        self.driver.find_element(
            By.XPATH, '//*[@id="o697594959"]/main/div/div/div/div[3]/button[1]').click()
        sleep(1)
        self.driver.find_element(
            By.XPATH, '//*[@id="o697594959"]/main/div/div/div/div[3]/button[2]').click()

    def firstLike(self) -> None:
        self.driver.find_element(
            By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button').click()

    def like(self) -> None:
        self.driver.find_element(
            By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button').click()

    def dislike(self) -> None:
        self.driver.find_element(
            By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button').click()

    # Close Add to Home Popup window
    def add_home_popup(self) -> None:
        self.driver.find_element(
            By.XPATH, '//*[@id="o697594959"]/main/div/div[2]/button[2]').click()

    # Close Match Popup window
    def match_popup(self) -> None:
        self.driver.find_element(
            By.XPATH, '//*[@id="o-1538620060"]/main/div/div[1]/div/div[4]/button').click()

    # Close Super Like Popup window
    def super_like_popup(self) -> None:
        self.driver.find_element(
            By.XPATH, '//*[@id="o697594959"]/main/div/button[2]').click()

    # Auto Switch feature
    def swipe(self) -> None:
        # Must call on first swipe
        self.firstLike()

        likeCount, dislikeCount = 0, 0

        while likeCount + dislikeCount < 1000:
            sleep(uniform(0.5, 3.5))
            try:
                randomNum = random()  # Random from 0 -> 0.99999
                # 85% swipe like, 15% swipe dislike

                if randomNum < 0.85:
                    self.like()
                    likeCount += 1
                else:
                    self.dislike()
                    dislikeCount += 1

                print(f"Swipe Count: {likeCount+dislikeCount}")

            except Exception:
                try:
                    self.add_home_popup()
                except Exception:
                    try:
                        self.match_popup()
                    except Exception:
                        try:
                            self.super_like_popup()
                        except Exception:
                            print("Errorrrr!!!")

        print(
            f'Final Report ({likeCount+dislikeCount} swipes): \n Likes: {likeCount} \n Dislikes: {dislikeCount}')


bot = TinderBot()
bot.login()
# Wait facebook login redirect to main page
sleep(15)
bot.swipe()
