'''
### WORKFLOW

'''

# Importing the libraries
from bs4 import BeautifulSoup
import requests

# Fetch the pages
result = requests.get("www.google.com")
result.status_code  # get status code
result.headers  # get the headers

# Page content
content = result.text

# Create soup
soup = BeautifulSoup(content, "lxml")

# HTML in a readable format
print(soup.prettify())

# Find an element
soup.find(id="specific_id")

# Find elements
soup.find_all("a") / soup.find_all("a", "css_class")
soup.find_all("a", class_="my_class")
soup.find_all("a", attrs={"class": "my_class"})

# Get inner text
sample = element.get_text()
sample = element.get_text(strip=True, separator=' ')

# Get specific attributes
sample = element.get("href")
