from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep

curriculum_file_path = 'curriculum.txt'
courses_file_path = 'courses.txt'
sub_topics_file_path = 'sub_topics_and_videos.txt'
lectures_file_path = 'link/lectures2.txt'
lectures2_file_path = 'link/lectures3.txt'

# Initialize the WebDriver
options = Options()
options.add_argument("start-maximized")
#options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

lecture_counter = 0

def login_lecturio():
    global lecture_counter
    
    driver.get("https://vin.lecturio.com")
    print('starting')
    email=driver.find_element(By.ID, "login_email")
    password=driver.find_element(By.ID, "login_password")
    login_button=driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    email.send_keys("")         #input your email here
    password.send_keys("")    #input your password here
    print('inputted')
    login_button.click()
    
    sleep(5)
    
    with open (lectures_file_path, 'r') as f:
        topic_links = f.readlines()
    for topic_link in topic_links:
        if('https://vin.lecturio.com/#/course' in topic_link):
            driver.get(topic_link)
            sleep(7)
            print(driver.current_url)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            libraries = soup.find('ul', class_='MuiList-root MuiList-dense css-11fhglq')
            if not libraries: libraries = soup.find('ul', class_='MuiTypography-root MuiTypography-body1 css-1mhhezc')
            
            libraries_link = libraries.find_all('a', class_='MuiButtonBase-root MuiListItemButton-root MuiListItemButton-dense MuiListItemButton-root MuiListItemButton-dense css-v40715')
            
            with open(lectures2_file_path, 'a') as f:
                for link in libraries_link:
                    f.write(f'https://vin.lecturio.com/{link["href"]}\n')
                    lecture_counter += 1
                    print(f"Lecture {lecture_counter} added")
        else:
            with open(lectures2_file_path, 'a') as f:
                f.write(topic_link)
                lecture_counter += 1
                print(f"Lecture {lecture_counter} added")
                
login_lecturio()

driver.quit()