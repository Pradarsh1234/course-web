from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def highlight_parent_element(driver, word):
    elements_with_word = driver.find_elements(By.XPATH, f"//*[contains(text(), '{word}')]")

    for element in elements_with_word:
        parent_element = element.find_element(By.XPATH, "./..")
        driver.execute_script("arguments[0].style.backgroundColor='#41A945'", parent_element)

def highlight_words(driver, words_to_highlight):
    for word in words_to_highlight:
        highlight_parent_element(driver, word)

def main():
    # Set up the Chrome driver
    driver = webdriver.Chrome()
    words_to_highlight = ["Special Offer!", "Explore"] #Datasets sample inputes

    try:
        while True:
            highlight_words(driver, words_to_highlight)
            time.sleep(2)

    except KeyboardInterrupt:        
        print("Stopping the script.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
