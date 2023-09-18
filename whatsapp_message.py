from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import logging
import time

# Set up logging
logging.basicConfig(filename='whatsapp.log', level=logging.INFO)

# Set the phone number and message
phone_number = input("Enter the phone number of the recipient (with country code): ")
message = input("Enter the message: ")

# Open WhatsApp Web in Chrome
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code
input("Scan the QR code and press enter to continue...")

# Keep sending the message every 10 seconds
while True:
    try:
        # Find the search box and enter the phone number
        search_box = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')))
        search_box.send_keys(phone_number + Keys.ENTER)

        # Wait for the chat to load
        chat_box = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))

        # Send the message
        chat_box.send_keys(message + Keys.ENTER)
        logging.info(f"Message sent to {phone_number}: {message}")
        print(f"Message sent to {phone_number}: {message}")
    except Exception as e:
        logging.error(f"An error occurred while sending the message to {phone_number}: {e}")
        print(f"An error occurred while sending the message to {phone_number}: {e}")

    time.sleep(2)
