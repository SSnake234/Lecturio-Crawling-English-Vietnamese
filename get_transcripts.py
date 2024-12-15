# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep
# import os
# import json
# from concurrent.futures import ProcessPoolExecutor

### Used for normal crawling

# def init_webdriver():
#     """Initialize a new WebDriver instance."""
#     options = Options()
#     options.add_argument("start-maximized")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     driver = webdriver.Chrome(options=options)
#     return driver

# def write_to_file(output_folder_path, lecture_link, eng_transcript, vi_transcript, file_count):
#     """Write the transcript data to a JSON file."""
#     data = {
#         "url": lecture_link,
#         "en": eng_transcript,
#         "vi": vi_transcript
#     }
#     file_path = f"{output_folder_path}/lecturio_{file_count:05d}.json"
#     os.makedirs(output_folder_path, exist_ok=True)
#     with open(file_path, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)

# def get_transcript(driver, language):
#     """Get the transcript text for the given language."""
#     try:
#         dropdown = driver.find_element(By.XPATH, '//div[@role="combobox" and @aria-expanded="false"]')
#         dropdown.click()
#         sleep(0.1)

#         language_lists = driver.find_elements(By.CSS_SELECTOR, 'li[role="option"]')
#         for lang in language_lists:
#             if language in lang.text:
#                 lang.click()
#                 sleep(0.1)
#                 break

#         timers = driver.find_elements(By.TAG_NAME, 'span')
#         for timer in timers:
#             if '00:' in timer.text.strip() or ':00' in timer.text.strip():
#                 transcript = timer.find_element(By.XPATH, './ancestor::div[3]')
#                 return transcript.text
#     except Exception as e:
#         print(f"Error fetching {language} transcript: {e}")
#     return None

# def process_lecture(lecture_links, output_folder_path, worker_id):
#     """Process a set of lecture links."""
#     driver = init_webdriver()
#     try:
#         driver.get("https://vin.lecturio.com")
#         sleep(1)
#         # Login
        # driver.find_element(By.ID, "login_email").send_keys("")             #input your email here
        # driver.find_element(By.ID, "login_password").send_keys("")        #input your password here
        # driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#         sleep(5)

#         for i in range(12000, len(lecture_links)):
#             if i % 5 != worker_id:
#                 continue
#             try:
#                 lecture_link = lecture_links[i]
#                 driver.get(lecture_link.strip())
#                 sleep(10)
#                 print(f"Processing: {lecture_link.strip()}")

#                 # Click transcript button
#                 paragraphs = driver.find_elements(By.TAG_NAME, 'p')
#                 for p in paragraphs:
#                     if p.text.strip() == 'Transcript':
#                         p.find_element(By.XPATH, './ancestor::button').click()
#                         sleep(1)
#                         break

#                 # Fetch transcripts
#                 eng_transcript = get_transcript(driver, 'English')
#                 vi_transcript = get_transcript(driver, 'Vietnamese')

#                 # Write transcripts to file
#                 if eng_transcript and vi_transcript:
#                     write_to_file(output_folder_path, lecture_link, eng_transcript, vi_transcript, i + 1)
#                     print(f"Written transcript {i + 1}")
#                 else:
#                     print("Transcripts not found.")
#             except Exception as e:
#                 print(f"Error processing {lecture_link}: {e}")
#     except Exception as e:
#         print(f"Error initializing driver: {e}")
#     finally:
#         driver.quit()

# def parallel_crawl(lecture_file_path, output_folder_path):
#     """Run the crawler in parallel."""
#     with open(lecture_file_path, 'r') as f:
#         lecture_links = f.readlines()

#     # Split work across multiple processes
#     with ProcessPoolExecutor(max_workers=5) as executor:
#         for worker_id in range(5):
#             executor.submit(process_lecture, lecture_links, output_folder_path, worker_id)

# # Entry point
# if _name_ == "_main_":
#     lecture_file_path = 'links/lectures3.txt'
#     output_folder_path = ''   # Output folder path
#     parallel_crawl(lecture_file_path, output_folder_path)

### Used when crawling uncrawled indices

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os
import json
from concurrent.futures import ProcessPoolExecutor

def init_webdriver():
    """Initialize a new WebDriver instance."""
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    return driver

def write_to_file(output_folder_path, lecture_link, eng_transcript, vi_transcript, file_count):
    """Write the transcript data to a JSON file."""
    data = {
        "url": lecture_link,
        "en": eng_transcript,
        "vi": vi_transcript
    }
    file_path = f"{output_folder_path}/lecturio_{file_count:05d}.json"
    os.makedirs(output_folder_path, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_transcript(driver, language):
    """Get the transcript text for the given language."""
    try:
        dropdown = driver.find_element(By.XPATH, '//div[@role="combobox" and @aria-expanded="false"]')
        dropdown.click()
        sleep(0.5)

        language_lists = driver.find_elements(By.CSS_SELECTOR, 'li[role="option"]')
        for lang in language_lists:
            if language in lang.text:
                lang.click()
                sleep(0.5)
                break

        timers = driver.find_elements(By.TAG_NAME, 'span')
        for timer in timers:
            if '00:' in timer.text.strip() or ':00' in timer.text.strip():
                transcript = timer.find_element(By.XPATH, './ancestor::div[3]')
                return transcript.text
    except Exception as e:
        print(f"Error fetching {language} transcript: {e}")
    return None

def process_lecture(lecture_links, output_folder_path, worker_id, uncrawled_indices):
    """Process a set of lecture links."""
    driver = init_webdriver()
    try:
        driver.get("https://vin.lecturio.com")
        sleep(1)
        # Login
        driver.find_element(By.ID, "login_email").send_keys("")             #input your email here
        driver.find_element(By.ID, "login_password").send_keys("")        #input your password here
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        sleep(5)

        for index in uncrawled_indices:
            i = int(index.strip())
            if i % 5 != worker_id:
                continue
            try:
                lecture_link = lecture_links[i - 1]
                driver.get(lecture_link)
                sleep(10)
                print(f"Processing: {lecture_link}")

                # Click transcript button
                paragraphs = driver.find_elements(By.TAG_NAME, 'p')
                for p in paragraphs:
                    if p.text.strip() == 'Transcript':
                        p.find_element(By.XPATH, './ancestor::button').click()
                        sleep(0.5)
                        break

                # Fetch transcripts
                eng_transcript = get_transcript(driver, 'English')
                vi_transcript = get_transcript(driver, 'Vietnamese')

                # Write transcripts to file
                if eng_transcript and vi_transcript:
                    write_to_file(output_folder_path, lecture_link, eng_transcript, vi_transcript, i)
                    print(f"Written transcript {i}")
                else:
                    print("Transcripts not found.")
            except Exception as e:
                print(f"Error processing {lecture_link}: {e}")
    except Exception as e:
        print(f"Error initializing driver: {e}")
    finally:
        driver.quit()

def parallel_crawl(lecture_file_path, output_folder_path, uncrawled_indices):
    """Run the crawler in parallel."""
    with open(uncrawled_indices, 'r') as f:
        uncrawled_indices = f.readlines()
    with open(lecture_file_path, 'r') as f:
        lecture_links = f.readlines()

    # Split work across multiple processes
    with ProcessPoolExecutor(max_workers=5) as executor:
        for worker_id in range(5):
            executor.submit(process_lecture, lecture_links, output_folder_path, worker_id, uncrawled_indices)

# Entry point
if __name__ == "__main__":
    lecture_file_path = 'links/lectures3.txt'
    output_folder_path = '' # Output folder path
    uncrawled_indices = 'uncrawled_index.txt'
    parallel_crawl(lecture_file_path, output_folder_path, uncrawled_indices)