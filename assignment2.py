
import chromedriver_autoinstaller #For auto installing a web driver
from selenium import webdriver #importing web driver
from selenium.webdriver.common.by import By # to specify attribute or tagname for searching element
from selenium.webdriver.support.ui import WebDriverWait #package for initialize and wait till element(link) became clickable or displayed
from selenium.webdriver.support import expected_conditions as EC # just for expected_conditions
from selenium.webdriver.common.keys import Keys # To perform keyboard keys
import time # To add delay
from loguru import logger # For logging
logger.add("debug.log",format="{time} {level} {message}") #configuration of logger
opt = webdriver.ChromeOptions() #configuration web driver
opt.add_argument("--start-maximized") # adding argument to maximize the screen of tab
chromedriver_autoinstaller.install() # to auto install web driver
driver = webdriver.Chrome(options=opt) #also onfiguration web driver
wait = WebDriverWait(driver, 10) # adding waiting time to web driver


'''Send message to support'''
def send_msg_to_support(name=None,phone_number=None,email=None,msg=None): # None is default value
    logger.info('Send message to support started inputs:' + 
                f'name = {name} \n phone_number = {phone_number}'+
                f'emai = {email} \n msg = {msg}'          
    ) # to write about test in log file
    if name is None or phone_number is None or email is None or msg is None: #to terminate if some data is None
        logger.error("Please add all necessary informations")
        return None
    try:
        driver.get('https://shop.kz/') # to get the web page of Shop.kz 
        support_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa.fa-commenting-o"))) #find element with css selector
        support_button.click() #click()
        name_field = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
        name_field.send_keys(name)
        phone_field = wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
        phone_field.send_keys(phone_number)
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_field.send_keys(email)
        message = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        message.send_keys(msg)
        try: #This webpage used popup when page loaded and this try expect block for this reason
            time.sleep(5) #to wait
            if no_btn := driver.find_element(By.ID,"onesignal-slidedown-cancel-button"):
                no_btn.click()
        except:
            logger.info("Popup not found")
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "button"))).click() #find by tag name 
        logger.info("Test ended")
    except Exception as e:
        logger.error(str(e)) #adding exception to log file if it occurred

'''Language switcher test'''
def language_change(lan = None):

    logger.info(f'Language test started language for testing:{lan}')
    if lan is None:
        logger.error("Please add all necessary informations")
        return None
    driver.get('https://shop.kz/') # to get the web page of Shop.kz 
    try:
        try:
            time.sleep(5)
            if no_btn := driver.find_element(By.ID,"onesignal-slidedown-cancel-button"):
                no_btn.click()
        except:
            logger.info("Popup not found")


        language_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "language_selector")))
        if language_button.text == lan:
            logger.info("Language which you send already choosed")
            return None
        else:
            language_button.click()
        logger.info("Test ended")
    except Exception as e:
        logger.error(str(e)) #adding exception to log file if it occurred

'''Social media buttons test button'''
def check_social_media_buttons(social_media=None):
    if social_media is None:
        logger.error("Please add all necessary informations")
        return None
    logger.info(f'Social media test started:{social_media}')
    try:
        try:
            time.sleep(5)
            if no_btn := driver.find_element(By.ID,"onesignal-slidedown-cancel-button"):
                no_btn.click()
        except:
            logger.info("Popup not found")
        dict = {  #because its easy to use in situation dictionary because in tradion way it takes a lot if else statements it means a bad code
            'Instagram':".in.bx-socialfooter-icon",
            'VK':".vk.bx-socialfooter-icon",
            "Facebook":".fb.bx-socialfooter-icon",
            "Telegram":".tg.bx-socialfooter-icon",
            "YouTube":".yt.bx-socialfooter-icon"
        }
        language_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, dict.get(social_media))))
        language_button.click()
        if driver.current_url == "https://shop.kz/": #to check the url of tab
            logger.error("Button not works")
            return None
        logger.info("Test ended")
    except Exception as e:
        logger.error(str(e)) #adding exception to log file if it occurred
    
'''Add item to wishlist'''
def add_to_wishlist():
    logger.info('Adding item to wishlist')
    try:
        driver.get('https://shop.kz/') # to get the web page of FlyArystan 
        try:
            time.sleep(5)
            if no_btn := driver.find_element(By.ID,"onesignal-slidedown-cancel-button"):
                no_btn.click()
        except:
            logger.info("Popup not found")
        driver.execute_script("window.scrollTo(0, 1200)")  #to scroll 1200 for Y direction
        for i in driver.find_elements(By.CSS_SELECTOR,".g-wishlist"):
            if i.is_displayed() and i.is_enabled(): #to check if button enabled and displayed
                i.click()
                break
            else:
                logger.error("Element nof found")
                return None
        logger.info("Test ended")
    except Exception as e:
        logger.error(str(e)) #adding exception to log file if it occurred

'''Search engine test'''
def search_test(search_text = None):
    logger.info(f"Test of search engine text message:{search_text}")
    if search_text is None:
        logger.error("Please add all necessary informations")
        return None
    try:# try block to catch errors because adding after each line messages is time and memory consuming
        try:
            time.sleep(5)
            if no_btn := driver.find_element(By.ID,"onesignal-slidedown-cancel-button"):
                no_btn.click()
        except:
            logger.info("Popup not found")
        driver.get('https://shop.kz/') # to get the web page of Shop.kz(Белый Ветер)
        driver.maximize_window() # also maximize the window
        search_editor = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-hover__field")))
        search_editor.click()
        time.sleep(3)
        search_editor = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "multi-input")))
        search_editor.send_keys(search_text)
        search_editor.send_keys(Keys.ENTER)
        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-hover__field")))
        search_button.click()
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sprite.g-wishlist-icon")))
        search_button.click()
        logger.info("Test ended")
    except Exception as e:
        logger.error(str(e)) #adding exception to log file if it occurred
'''Call methods'''
search_test("Iphone 14")
send_msg_to_support("Test","877077272","example.b@gmail.com","Hey")
add_to_wishlist()
language_change("ҚАЗ")


 