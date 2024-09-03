from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Replace these with your LinkedIn credentials


# LINKEDIN_USERNAME = 'abcz38@gmail.com'
# LINKEDIN_PASSWORD = 'ibmwugnwungwgwg'

LINKEDIN_USERNAME = 'abcz38@gmail.com'
LINKEDIN_PASSWORD = 'ibmbst@112'

RECIPIENT_PROFILE_URL1 = 'https://www.linkedin.com/in/vineet-kumar-/'
RECIPIENT_PROFILE_URL2 ='https://www.linkedin.com/in//'

RECIPIENT_PROFILE_URL3 = 'https://www.linkedin.com/in/r-d-s/' 
# for invalid user profile 3 is given



MESSAGE_TEXT = 'Hello, this is a test message from Selenium! We welcome you.'

def send_linkedin_message():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    
    try:
        # Open LinkedIn login page
        driver.get('https://www.linkedin.com/login')
        
        # Wait for the page to load
        time.sleep(2)
        
        # Enter the username
        username_input = driver.find_element(By.ID, 'username')
        username_input.send_keys(LINKEDIN_USERNAME)
        
        # Enter the password
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(LINKEDIN_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        
        # Wait for the login process to complete
        time.sleep(3)
        
        # Navigate to the recipient's profile
        driver.get(RECIPIENT_PROFILE_URL1)
        time.sleep(3)
        driver.get(RECIPIENT_PROFILE_URL2)
        time.sleep(2)
        driver.get(RECIPIENT_PROFILE_URL3)
        
        # Wait for the profile page to load
        time.sleep(2)

        # Click on the "Message" button
        message_button = driver.find_element(By.XPATH, '//button[contains(@class, "message-anywhere-button")]')
        message_button.click()

        driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=%3AaZ")
        time.sleep(2)
        all_buttons=driver.find_element_by_tag_name("button")
        # Wait for the message window to appear
        connect_buttons=[btn for btn in all_buttons if btn.text=="connect"]
        for btn in connect_buttons:
            driver.execute_script("arguments[0].click();",btn)

        
        # Enter the message text
        message_input = driver.find_element(By.XPATH, '//div[contains(@class, "msg-form__contenteditable")]')
        message_input.send_keys(MESSAGE_TEXT)
        
        # Send the message
        send_button = driver.find_element(By.XPATH, '//button[contains(@class, "msg-form__send-button")]')
        send_button.click()
        
        # Wait for the message to be sent
        time.sleep(2)
        print('Message sent successfully!')
    
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == '__main__':
    send_linkedin_message()