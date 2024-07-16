from load_the_html import page
from bs4 import BeautifulSoup

# Parse the HTML
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())
