from interactive import click_color_buttons, open_page
from scraper import save_images
from setup import setup_driver
import sys


def run_scraper(url, output_directory):
    driver = setup_driver()
    open_page(driver, url)
    image_elements = click_color_buttons(driver)
    save_images(image_elements, output_directory)
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://www.liz.com.br/sutia-com-bojo-com-aro-sutop-sport-deluxe-51304/p?skuId=31739"

    if len(sys.argv) > 2:
        output_directory = sys.argv[2]
    else:
        output_directory = "images"

    run_scraper(url, output_directory)