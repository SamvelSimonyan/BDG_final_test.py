from defs import *

driver.get(base_url)
to_english()
driver.get(base_url)
sign_up()
login()
click_a_hotel(hotel_location, 0)
room_list = get_room_list()

for room in room_list:
    try:
        room.click()
        add_to_card()
    except NoSuchElementException:
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        continue
    else:
        break

customer_info_filler()
url = driver.current_url
