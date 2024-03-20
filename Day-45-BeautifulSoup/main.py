from bs4 import BeautifulSoup

# Constants
FILE_NAME = './website.html'

# Open the file and get the constents of it.
with open(FILE_NAME) as file:
    contents = file.read()
    
# Create the soup object using the file contents and html parser.
soup = BeautifulSoup(contents, 'html.parser')

# Show different attibutes of soup.

# result = soup.prettify()
# result = soup.title
# result = soup.title.name
# result = soup.title.string
# result = soup.h1.string
# result = soup.a

# print(result)

heading = soup.find(name='h1', id='name')
print(heading)
print(heading.get_text())

section_heading = soup.find(name='h3', class_='heading')
print(section_heading)

all_links = soup.find_all(name='a')
# print(all_links)

for link in all_links:
    # print(link.getText())
    # print(link.get('href'))
    print(f'{link.get_text()} - {link.get('href')}')

company_url = soup.select_one(selector='p a').get('href')
print(f'\nCompany Url - {company_url}')

class_heading = soup.select('.heading')
print(class_heading)

name = soup.select_one('#name')
print(name)