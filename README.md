# Lecturio-Crawling-English-Vietnamese

This project contains scripts for crawling and extracting lecture transcripts from Lecturio, including both English and Vietnamese versions.

## Scripts

- **get_links.py**: Used for retrieving the links to all lectures. The script handles nested courses, hence the need for running it three times to ensure all lecture links are captured. The links are stored in `links/lectures3.txt`.

- **get_transcripts.py**: Fetches the English and Vietnamese transcripts for each lecture and saves them to JSON files. The script has two main sections:
  - Normal crawling: Fetches transcripts for all lectures.
  - Crawling uncrawled indices: Specifically fetches transcripts for lectures that were missed or had errors in previous runs.

- **get_uncrawled.py**: Identifies the indices of lectures that were not successfully crawled in the initial runs, due to errors like Selenium's `StaleElement`. The uncrawled indices are saved to `uncrawled_index.txt`.

- **filter.py**: Cleans the JSON files by removing timestamps (like "00:00") and other noise (like "\n").

## Usage

1. **get_links.py**: 
   - Run the script to collect lecture links (you don't need to run this since the lectures link are already in `links/lectures3.txt`).
   - Ensure you update the script to input your email and password for login.

2. **get_transcripts.py**: 
   - Run the script to fetch transcripts.
   - Adjust the output folder path as needed.
   - Use the normal crawling section for the first run.
   - Use the uncrawled indices section if there are any uncrawled lectures.

3. **get_uncrawled.py**: 
   - Run this script to identify uncrawled indices.
   - Ensure the folder path to the JSON files is correctly specified.

4. **filter.py**: 
   - Run the script to clean the JSON files of any noise.

## Notes

- Ensure you have the necessary libraries (Selenium, BeautifulSoup) installed.
- Update paths and credentials as required.
- Be prepared to handle occasional errors from Selenium and rerun the scripts as needed.
