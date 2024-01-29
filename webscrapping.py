import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text content using BeautifulSoup functions
            # Example: Get all the text content inside <p> tags
            paragraphs = soup.find_all('div')

            if paragraphs:
                # Print the text content
                for paragraph in paragraphs:
                    print(paragraph.text.strip())
            else:
                # If no paragraphs are found, print the entire HTML content
                print(soup.prettify())

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
url_to_scrape = "file:///C:/Users/Lenovo/Desktop/pradarsh%20html/hackathon/hackthon2.html?"
scrape_website(url_to_scrape)
