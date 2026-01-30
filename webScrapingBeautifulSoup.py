# Topic of the Day: Web Scraping (BeautifulSoup)
#
# Explanation: Sometimes data isn't in a nice CSV or API; it's stuck on a website. Web Scraping is the act of downloading a webpage's HTML and extracting specific information (like prices or headlines).
#
# Library: BeautifulSoup (for parsing) and requests (for downloading).
#
# Code: Note: Run pip install beautifulsoup4 requests first.

import requests
from bs4 import BeautifulSoup

# 1. Download the page
url = "https://example.com"
response = requests.get(url)

# 2. Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# 3. Extract Data
# Find the first <h1> tag (usually the title)
title = soup.find("h1").text
print(f"Page Title: {title}")

# Find all links (<a> tags)
links = soup.find_all("a")
print(f"Found {len(links)} links.")
for link in links:
    print(link.get("href"))