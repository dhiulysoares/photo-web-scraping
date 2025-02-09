import time
from selenium.webdriver.common.by import By


def open_page(driver, url):
    driver.get(url)
    time.sleep(10)

def click_color_buttons(driver):
    image_elements = []
    try:
        color_buttons = driver.find_elements(By.CLASS_NAME, "liz-liz-store-7-x-skuSelectorButton")
        for button in color_buttons:
            if 'skuSelectorItem' in button.get_attribute("class"):
                truncated_class_color = ''.join([i for i in button.get_attribute("class").split('skuSelectorItem')[1] if not i.isdigit()])
                if len(truncated_class_color) > 0:
                    button.click()
                    time.sleep(5)
                    image_elements.append(driver.find_elements(By.TAG_NAME, "img"))
    except Exception as e:
        print("Error selecting color:", e)
        driver.quit()
        exit()
    return image_elements
