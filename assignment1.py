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
def ticket(): # function for testing booking system
    logger.info("Ticket booking testing started")
    try: # try block to catch errors because adding after each line messages is time and memory consuming
        driver.get('https://flyarystan.com/') # to get the web page of FlyArystan
        driver.maximize_window() # also maximize the window
        depPortInput = wait.until(EC.visibility_of_element_located((By.ID, "depPortInput"))) #find element by ID 
        depPortInput.send_keys("Нур-Султан") #write a dep city 
        depPortInput.send_keys(Keys.ENTER) #perform enter
        arrPortInput = wait.until(EC.visibility_of_element_located((By.ID, "arrPortInput")))
        arrPortInput.send_keys("Семей")
        arrPortInput.send_keys(Keys.ENTER)
        depDate = wait.until(EC.visibility_of_element_located((By.ID, "depDate")))
        depDate.click() #for open date picker
        time.sleep(5) #waiting if connection poor
        for i  in    driver.find_elements(By.CLASS_NAME, "datepicker--cell"): # looping through elements with common class datepicker--cell
            if "-disabled-" in i.get_dom_attribute("class"): #ignore disabled cells
                continue 
            else:
                if i.is_enabled() and i.is_displayed(): #is date is_enabled and displayed try to click
                    try:
                        i.click() # click
                        break # to break the loop
                    except Exception as e: # for exceptions
                        logger.error(str(e)) #adding exception to log file if it occurred
        driver.find_element(By.CSS_SELECTOR,('[value="Найти"]')).click() #to find a flights
        time.sleep(7) #waiting if connection poor
        for  i in  driver.find_elements(By.CLASS_NAME, "cabin-name-PROMO"): #same logic like in datepicker
            if i.is_enabled() and i.is_displayed():
                i.click()
                break
        
        '''
        HERE YOU CAN SEE MOST OF LINES COMMON I WROTE ABOUT THIS METHODS IN 24 LINE / depPortInput
        '''
        wait.until(EC.visibility_of_element_located((By.ID, "PROMO_KZKZ"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "continueButton"))).click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "male"))).click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "filter-option"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "bs-select-1-1"))).click()
        name = wait.until(EC.visibility_of_element_located((By.ID, "passenger_form_validate__name_0")))
        name.send_keys("Bekarys")
        name.send_keys(Keys.ENTER)
        surname = wait.until(EC.visibility_of_element_located((By.ID, "passenger_form_validate__surname_0")))
        surname.send_keys("Magauiya")
        surname.send_keys(Keys.ENTER)
        bhday = wait.until(EC.visibility_of_element_located((By.ID, "passenger_form_birthday0")))
        bhday.send_keys("08")
        time.sleep(1)
        bhday.send_keys("01")
        time.sleep(1)
        bhday.send_keys("2003")
        time.sleep(1)
        bhday.send_keys(Keys.ENTER)
        driver.find_element(By.CSS_SELECTOR,('[value="Выберите из списка"]')).click()
        wait.until(EC.visibility_of_element_located((By.ID, "bs-select-2-1"))).click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "passenger-continue-btn"))).click()
        doc = wait.until(EC.visibility_of_element_located((By.ID, "passenger_form_validate__docId_0")))
        doc.send_keys("03040404")
        logger.info("End of test")
        doc.send_keys(Keys.ENTER)
    except Exception as e:
        logger.error(str(e))

def just_search(text=None):
    logger.info("Google search testing started")
    try:
        driver.get('https://google.com/')
        driver.maximize_window()
        search = driver.find_element(By.NAME,"q")
        search.send_keys(text)
        logger.info("End of test")
        
        search.send_keys(Keys.ENTER)
        
    except Exception as e:
        logger.error("Ticket booking testing started")


def login(username=None,password=None):
    logger.info("Moodle login testing started")
    try:
        driver.get('https://moodle.astanait.edu.kz/login/index.php')
        driver.maximize_window()
        username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username.send_keys(username)
        password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password.send_keys(password)
        btn = wait.until(EC.visibility_of_element_located((By.ID, "loginbtn")))
        logger.info("End of test")
        btn.click()
    except Exception as e:
        logger.error(str(e))






    