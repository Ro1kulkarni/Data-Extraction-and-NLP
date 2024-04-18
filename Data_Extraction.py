import requests    # Library for making HTTP requests
from bs4 import BeautifulSoup   # Library for parsing HTML documents
import pandas as pd     # Library for data manipulation and analysis

# Function to extract article title and text from a given URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the article title
        title = soup.find('title').get_text().strip()
        # Find the article text
        article_text = ""
        for paragraph in soup.find_all('p'):
            article_text += paragraph.get_text().strip() + "\n"
        return title, article_text
    except Exception as e:
        print(f"Error extracting text from {url}: {e}")
        return None, None

# Load URLs from input Excel file
input_data = pd.read_excel("C:/Users/Hrishikesh/Desktop/rohan/Blackcoffer/Input.xlsx")

# Specify the saving path
saving_path = "C:/Users/Hrishikesh/Desktop/rohan/Blackcoffer/Data_Extraction"

# Extract text and save to text files
for index, row in input_data.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    title, text = extract_text_from_url(url)
    if text:
        # Save text to file
        with open(f"{saving_path}/{url_id}.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\nURL: {url}\n\n{text}")
            print(f"Text extracted from URL_ID {url_id} and saved to {saving_path}/{url_id}.txt")
    else:
        print(f"No text extracted from URL_ID {url_id}")

