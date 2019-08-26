import config
from selenium import webdriver
import time
import pyautogui

browser = webdriver.Chrome()                                    # Creates instance of Chrome
browser.get("https://facebook.com")                             # Opens FB

allowButton = "Allow.PNG"                                       # Represents the "Allow" button in the msg "Allow FB to send notifications"
user_Name = "username.PNG"                                      # Represents the person we are sending the message to.
messenger_button = "MessengerIcon.PNG"                          # Represents the messenger icon.


signin_link = browser.find_element_by_link_text("Log In")       # returns a web element that represents the "Log In" button
signin_link.click()                                             # clicks on the "Log In" button


username_box = browser.find_element_by_id("email")              # id that identifies the username button
username_box.send_keys(config.user_name)                        # types in username

password_box = browser.find_element_by_id("pass")               # id that identifies the password button
password_box.send_keys(config.password)                         # types in password


password_box.submit()                                           # clicks the sign in button

time.sleep(3)                                                   # Pauses execution for 3 seconds
pyautogui.click(pyautogui.locateOnScreen(allowButton))          # locates and clicks on the "Allow" button.

time.sleep(1)                                                   # Pauses execution for 1 second
pyautogui.click(pyautogui.locateOnScreen(messenger_button))     # Locates and clicks on the messenger icon.


time.sleep(1)
pyautogui.click(pyautogui.locateOnScreen(user_Name))            # Locates and clicks on the user we want to message.
time.sleep(1)

pyautogui.moveTo(572,959,duration=5)                            # Moves mouse towards text box (Coordinates may vary b/ machines).
pyautogui.click()                                               # Clicks on text box, allowing us to type.

pyautogui.write(config.msg)                                     # Types specified message to user.
pyautogui.press("enter")                                        # Sends message to user.







