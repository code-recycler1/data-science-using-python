from parse_the_html import soup

# Extract the Data
cards = soup.find_all("div", class_='card-content')
for card in cards:
    title_element = card.find("h2", class_="title")
    company_element = card.find("h3", class_="company")
    location_element = card.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text.strip())
    print()
