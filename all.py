from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('kalangala')
    password_field.send_keys('Kalangala@hub')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()

##############################################################################
# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('lwengo')
    password_field.send_keys('lwengo8910')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()


###################################################################################################

# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('lyantonde')
    password_field.send_keys('lyantonde8910')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()
    #####################################################################

# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('gombe')
    password_field.send_keys('gombe8910')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()
###################################################################
# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('maddu')
    password_field.send_keys('maddu8910')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()

####################################################################
# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('mpigi')
    password_field.send_keys('mpigi8910')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()
############################################################################
# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('masaka')
    password_field.send_keys('masaka201')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()

























# Set up the WebDriver (e.g., Chrome)
driver_path = r"C:\Users\Desire Lumisa\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe"  # Change this to the path where you have your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get('https://vldash.cphluganda.org/auth/login')

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Input the credentials
    username_field.send_keys('Sembabule')
    password_field.send_keys('sembabule8910')

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Click on the REPORTS link
    reports_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'REPORTS'))
    )
    reports_link.click()

    # Wait for the REPORTS page to load
    time.sleep(5)

    # Click on the "Valid Patients' Results" section
    valid_results_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#v-patients' and text()=\"Valid Patients' Results\"]"))
    )
    valid_results_link.click()

    # Wait for the data to load (e.g., wait for a specific table row or loading indicator)
    WebDriverWait(driver, 120).until(  # Increased wait time to 120 seconds
        EC.presence_of_element_located((By.XPATH, "//tr[@ng-repeat='validPatientResults_object in validPatientResults']"))
    )

    # Click on the "Download CSV" button
    download_csv_button = driver.find_element(By.ID, "exportValidPatientResults")
    download_csv_button.click()

    # Wait for some time to ensure the download starts (optional)
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()