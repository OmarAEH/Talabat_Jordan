"""
This script coded by github.com/OmarAEH
Feel free to contact me at anytime.
"""

from selenium import webdriver
import time
import winsound
driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.talabat.com/jordan")
Correct_Location = True

# Trying the user provided information if the correct input"in this case is a correct location"
# it will continue  except it will loop again until it does

while Correct_Location:  # Setting up a while loop while the condition is True
    try:
        # Navigating the location search bar and sending in the input which the user is typing
        driver.find_element_by_name("mapFirstSearch").send_keys(input("Enter the area, street name , landmark : "))
        First_Option = driver.find_elements_by_xpath("//li[@class='ng-scope']")  # Navigating the restaurants rusults
        First_Option[0].click()  # Clicking on the first option which is the correct one
        time.sleep(3)  # Sleep for 3 second
        driver.find_element_by_xpath("//*[contains(text(),'Deliver Here')]").click()  # Clicking on deliver here button
        Correct_Location = False  # While loop condition is False thus exiting the while loop
    except:
        print("Invalid Location")
        driver.refresh()    # Refresh the opened page
Correct_Restaurant = True   # While loop condition
# Trying the user provided information if it's correct input"in this case it is a correct Restaurant"
# it will continue  except it will loop again
while Correct_Restaurant:  # Setting up a while loop while the condition is True
    try:
        time.sleep(1)
        # Navigating the restaurant search bar and sending in the input which the user is typing
        driver.find_element_by_xpath('//input[@placeholder="Search Restaurants"]').send_keys(input("Enter the restaurant's name : "))
        time.sleep(1)
        Results = driver.find_elements_by_xpath('//div[@class="d-flex"]')  # Navigating the search results
        Results[0].click()  # Clicking on the first one which is the correct one
        Correct_Restaurant = False  # While loop condition is False thus exiting the while loop
    except:
        print("Invalid Restaurant")
        driver.refresh()  # Refresh the opened page
Busy = True  # While loop condition
while Busy:  # While the restaurant is busy
    # Trying to find a specific element which indicate that the restaurant is busy and keep refreshing the page
    try:
        driver.find_element_by_xpath("//span[@class='h5 menu-open f-14 Busy f-400 red-text']")  # Busy restaurant element
        time.sleep(10)  # Sleep for 10 sec
        driver.refresh()  # Refresh the page
        print("The restaurant is busy now, Please hold on....")
    except:  # When the restaurant service is available
        Busy = False  # While loop condition is False thus exiting the while loop
        duration = 3000  # milliseconds
        freq = 1500  # Hz
        winsound.Beep(freq, duration)  # Beep sound with a specific frequency and duration
        print("You can order now,The Restaurant service is available")
