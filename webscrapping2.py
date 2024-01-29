from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_and_detect_dark_pattern(url):
    try:
        # Set up a Chrome browser using ChromeDriverManager
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # Use ChromeDriverManager to automatically download and manage chromedriver
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

        # Navigate to the URL
        driver.get(url)

        # Wait for the page to fully load (you may need to adjust the wait time)
        driver.implicitly_wait(10)

        # Get the page source after JavaScript execution
        page_source = driver.page_source

        # Close the browser
        driver.quit()

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract text content using BeautifulSoup functions
        paragraphs = soup.find_all('p')

        dark_pattern_keywords = ['trick', 'deceptive', 'misleading', 'hidden cost', 'forced subscription', 'spam']

        # Check for dark pattern keywords in the text
        dark_pattern_detected = any(keyword in paragraphs.text.lower() for keyword in dark_pattern_keywords)

        if dark_pattern_detected:
            print("Dark pattern detected! Be cautious.")
        else:
            print("No dark pattern detected. Proceed with caution.")

    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
try:
    url_to_scrape = "https://content.timesjobs.com/"
    scrape_and_detect_dark_pattern(url_to_scrape)
except KeyboardInterrupt:
    print("\nScript interrupted by user.")
