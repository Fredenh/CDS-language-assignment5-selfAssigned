import os
import requests
from bs4 import BeautifulSoup
import zipfile

# Creating function that unzips the zip filde in the "in" folder
def unzip_file(zip_file_path, target_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(target_folder)

# Making correct path for where the zip should unzip
zip_file_path = os.path.join(".", "in", "LOTR", "archive.zip")
target_folder = os.path.join(".", "in", "LOTR")

# Change the current working directory to the parent directory of the "in" folder
os.chdir(os.path.join(".", "in", ".."))

# Calling the function to unzip the file
unzip_file(zip_file_path, target_folder)

# Defining the URL of the story's first chapter
first_chapter_url = "https://archiveofourown.org/works/2064171/chapters/4487058"

# Creating a directory to store the chapter files
folder_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "in")
os.makedirs(folder_path, exist_ok=True)

# Function to save chapter content as a .txt file
def save_chapter_content(chapter_content, chapter_index):
    file_path = os.path.join(folder_path, f"chapter_{chapter_index}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(chapter_content)
    print(f"Chapter {chapter_index} has been saved.")

# Function to concatenate all chapter contents
def concatenate_chapters():
    ult_data = ""
    chapter_index = 1

    while True:
        file_path = os.path.join(folder_path, f"chapter_{chapter_index}.txt")
        if not os.path.exists(file_path):
            break

        with open(file_path, "r", encoding="utf-8") as file:
            chapter_content = file.read()

        ult_data += chapter_content + "\n"
        chapter_index += 1

    return ult_data

# Function to scrape and save each chapter
def scrape_chapters(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    chapter_content = soup.find("div", {"class": "userstuff"}).get_text(strip=True)
    save_chapter_content(chapter_content, 1)

    next_link = soup.find("li", {"class": "chapter next"})
    chapter_index = 2

    while next_link:
        next_url = "https://archiveofourown.org" + next_link.a["href"]
        response = requests.get(next_url)
        soup = BeautifulSoup(response.content, "html.parser")
        chapter_content = soup.find("div", {"class": "userstuff"}).get_text(strip=True)
        save_chapter_content(chapter_content, chapter_index)

        next_link = soup.find("li", {"class": "chapter next"})
        chapter_index += 1

# Scraping and save all chapters
scrape_chapters(first_chapter_url)

# Concatenating all chapter contents into a single string
ult_data = concatenate_chapters()

# Defining the file path for the concatenated data file
file_path = os.path.join(folder_path, "ult_data.txt")

# Writing the concatetenated data to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(ult_data)

print("Chapters have been saved and concatenated")
