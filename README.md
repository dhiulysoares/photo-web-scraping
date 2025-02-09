# Photo Scraper

Photo Scraper is a Python-based project designed to scrape and download images from websites.

## Features

- Scrape images from a given URL
- Download images to a specified directory
- Supports multiple image formats (JPEG, PNG, etc.)

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library
- Selenium library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dhiulysoares/photo-web-scraping.git
    ```
2. Navigate to the project directory:
    ```bash
    cd photo-web-scraping
    ```
3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script with the target URL:
    ```bash
    python main.py <URL> <output_directory>
    ```
    Replace `<URL>` with the website URL you want to scrape and `<output_directory>` with the directory where you want to save the images.

## Example

```bash
python scraper.py https://example.com/images /home/user/images
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/documentation/en/)
```
