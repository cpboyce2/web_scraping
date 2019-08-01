from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from date_likes_conversions import DateLikesConversion as cd
from likes_conversion import LikeConversion as lc



class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("/Users/connorboyce/PycharmProjects/web_scraping/chromedriver")

    def closeBrowser(self):
        self.driver.close()

    def login(self):

        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        pass_elem = driver.find_element_by_xpath("//input[@name='password']")
        pass_elem.clear()
        pass_elem.send_keys(self.password)
        pass_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def get_photo_links_by_tag(self, hashtag):

        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # searching for picture links
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs_hashtags = [elem.get_attribute('href') for elem in hrefs]

        # pic_hrefs = [href for href in pic_hrefs if hashtag in href]

        return pic_hrefs_hashtags

    def get_photo_links_by_account(self, account_name):

        driver = self.driver
        driver.get("https://www.instagram.com/" + account_name + "/")
        time.sleep(2)
        for i in range(1, 2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # searching for picture links
        picture_href = []
        proper_class = driver.find_elements_by_xpath("//div[@class= 'v1Nh3 kIKUG  _bz0w']")

        for items in proper_class:
            picture_href.append(items.find_element_by_css_selector('a').get_attribute('href'))

        return picture_href

    def like_photo(self, links):

        driver = self.driver
        for pic_href in links:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                time.sleep(18)
            except Exception as e:
                time.sleep(2)

    def get_time_and_likes(self, links):

        driver = self.driver
        time_stamps2, unformatted_stamps, proper_likes = [], [], []
        value_dict = {}

        for pic_href in range(0, 5):
            driver.get(links[pic_href])
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            unformatted_stamps.append(driver.find_element_by_tag_name("time").get_attribute("datetime"))
            try:
                likes_text = driver.find_element_by_xpath("//div[@class='Nm9Fw']")
            except ReferenceError:
                likes_text = driver.find_element_by_xpath("//div[@class='vJRqr']")

            # The return from the lc call with bring back an integer value of likes
            likes_text = lc(likes_text.text).likes_string_to_int()
            # This list now has all of the likes for each picture in an integer list
            proper_likes.append(likes_text)

        # The cd method now takes the unformatted time stamps and the list of dates
        # It will convert the time stamp into something readable and put the date, time, and likes all in a dictionary full of lists
        # With this dictionary you can now access any element of each picture by referencing the key and the index
        # of the value
        time_stamps2 = cd(unformatted_stamps, proper_likes).convert_date_and_likes()

        for i in range(len(proper_likes)):
            value_dict[i] = time_stamps2[i]

        return value_dict


# Next step is to work on organizing the data
# ConnorIG = InstaBot("boyceconnor2019", "provlax14")
# ConnorIG.login()
# photo_links = ConnorIG.get_photo_links_by_account("natgeotravel")
# yerpie = (ConnorIG.get_time_and_likes(photo_links))





