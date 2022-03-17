import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random

def email_generator(name):
    r = random.randint(10000,99999)
    email = name + str(r) + "@gmail.com"
    print(email)
    return email

first_name = "Samvel"
last_name = "Simonyan"
phone = "123456789"
email = email_generator("Samvel")
password = email
hotel_location = "Yerevan"
base_url = "https://www.phptravels.net/signup"


driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
action = ActionChains(driver)
driver.get(base_url)


driver.find_element_by_xpath('//*[@placeholder="First Name"]').send_keys(first_name)
driver.find_element_by_xpath('//*[@placeholder="Last Name"]').send_keys(last_name)
driver.find_element_by_xpath('//*[@placeholder="Phone"]').send_keys(phone)
driver.find_element_by_xpath('//*[@placeholder="Email"]').send_keys(email)
driver.find_element_by_xpath('//*[@placeholder="Password"]').send_keys(password)

driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[7]/button').click()

driver.find_element_by_xpath('//*[@placeholder="Email"]').send_keys(email)
driver.find_element_by_xpath('//*[@placeholder="Password"]').send_keys(password)


driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a').click()


search = driver.find_element_by_xpath('//*[@id="select2-hotels_city-container"]')
action.move_to_element(search).click().perform()

driver.find_element_by_class_name('select2-search__field').send_keys(hotel_location)

time.sleep(3)
driver.find_element_by_class_name('select2-search__field').send_keys(Keys.ENTER*1)

driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.find_element_by_xpath('//*[@id="caucasus hotel"]/div/div[2]/div/div[2]/div/a/span[1]').click()

driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('//*[@id="SearchBoxContainer"]/div/div/button/span').click()


try:
    driver.find_element_by_xpath('/html/body/div[16]/div/div/i').click()
except NoSuchElementException:
    try:
        driver.find_element_by_xpath('/html/body/div[15]/div/div/i').click()
    except NoSuchElementException:
      pass


driver.find_element_by_xpath('//*[@id="contentContainer"]/div[3]/ol/li[1]/div[2]/a/div/div[3]/div/div[3]/button/div/div/div/span').click()
driver.switch_to.window(driver.window_handles[2])

driver.find_element_by_xpath("//*[contains(@id,'BGgQoBjAB')]/div/div[5]/div[1]/div/div[1]/div/button/div/div/span").click()
driver.find_element_by_xpath('//*[@id="roomGrid"]/div[5]/div[2]/div[1]/div[4]/button/div/div/span').click()



driver.find_element_by_xpath('//*[@id="firstName_lastName"]').send_keys(first_name+" "+last_name)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="retypeEmail"]').send_keys(email)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="SiteContent"]/div/div[1]/div[5]/div/button/div/div/span').click()

url = driver.current_url


print(url)
true_url = "https://www.agoda.com/book/payment/"
false_url = "https://www.agoda.com/book/not_payment/"
print(true_url in url)
print(false_url in url)
