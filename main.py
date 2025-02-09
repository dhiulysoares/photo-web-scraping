def color():
    driver = setup_driver()
    url = "https://www.liz.com.br/sutia-com-bojo-com-aro-sutop-sport-deluxe-51304/p?skuId=31739"
    open_page(driver, url)
    image_elements = click_color_buttons(driver)
    save_images(image_elements, "liz_images")
    driver.quit()

if __name__ == "__main__":
    color()