import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random



driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(6)
driver.maximize_window()
action = ActionChains(driver)

# move to config file
first_name = "Samvel"
last_name = "Simonyan"
phone = "123456789"
hotel_location = "Yerevan"
base_url = "https://www.phptravels.net/signup"

def email_generator(name):
    r = random.randint(10000, 99999)
    email = name + str(r) + "@gmail.com"
    print(email)
    return email

email = email_generator("Samvel")
password = email

def to_english():
    l_bar = driver.find_element_by_xpath('//*[@id="languages"]')
    action.move_to_element(l_bar).click().perform()
    eng_l = driver.find_element_by_xpath('//*[@id="fadein"]/header/div[1]/div/div/div[2]/div/div/div[1]/div/ul/li[8]/a')
    action.move_to_element(eng_l).click().perform()
    time.sleep(1)

def sign_up():

    driver.find_element_by_xpath('//*[@placeholder="First Name"]').send_keys(first_name)
    driver.find_element_by_xpath('//*[@placeholder="Last Name"]').send_keys(last_name)
    driver.find_element_by_xpath('//*[@placeholder="Phone"]').send_keys(phone)
    driver.find_element_by_xpath('//*[@placeholder="Email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@placeholder="Password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[7]/button').click()


def login():
    driver.find_element_by_xpath('//*[@placeholder="Email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@placeholder="Password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button').click()


def close_popup():
    try:
        driver.find_element_by_xpath('/html/body/div[16]/div/div/i').click()
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath('/html/body/div[15]/div/div/i').click()
        except NoSuchElementException:
            pass


def click_a_hotel(hotel_location, hotel_number):
    driver.find_element_by_xpath('//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a').click()
    search = driver.find_element_by_xpath('//*[@id="select2-hotels_city-container"]')
    action.move_to_element(search).click().perform()
    driver.find_element_by_class_name('select2-search__field').send_keys(hotel_location)
    time.sleep(3)
    driver.find_element_by_class_name('select2-search__field').send_keys(Keys.ENTER * 1)
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    hotel_list = driver.find_elements_by_xpath('//*/div/div[2]/div/div[2]/div/a/span[1]')
    hotel_list[hotel_number].click()


def get_room_list():
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath('//*[@id="SearchBoxContainer"]/div/div/button/span').click()
    close_popup()
    room_list = driver.find_elements_by_xpath('//*[*]/button/div/div/div/span')
    return room_list


def add_to_card():
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="hotelNavBar"]/div/div/div/div/button').click()
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//*[contains(@id,'BGgQoBjAB')]/div/div[5]/div[1]/div/div[1]/div/button/div/div/span").click()
    except NoSuchElementException:
        try:
            action.send_keys(Keys.PAGE_DOWN * 1)
            action.perform()
            add_toCard_list = driver.find_elements_by_xpath('//*/div/div[5]/div[1]/div/div[1]/div/button/div/div/span')
            add_toCard_list[0].click()
        except NoSuchElementException:
            pass
    driver.find_element_by_xpath('//*[@id="roomGrid"]/div[5]/div[2]/div[1]/div[4]/button/div/div/span').click()

def customer_info_filler():
    driver.find_element_by_xpath('//*[@id="firstName_lastName"]').send_keys(first_name + " " + last_name)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="retypeEmail"]').send_keys(email)
    time.sleep(1)
    action.send_keys(Keys.PAGE_DOWN*1)
    action.perform()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="SiteContent"]/div/div[1]/div[6]/div/button/div/div/span').click()
