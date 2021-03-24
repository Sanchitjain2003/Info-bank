from bs4 import BeautifulSoup
import requests
import json

query = input("Enter topic to be searched: ")
query_string = query.replace(" ", "_")
page = requests.get("https://en.wikipedia.org/wiki/{}".format(query_string)).text
soup = BeautifulSoup(page, 'lxml')
intro = soup.find('div', class_='mw-parser-output')

p_list = intro.find_all('p', class_ = False)
count = 0
for i in range(len(p_list)):
    if count != 4:
        if p_list[i].text != ' ':
            print(p_list[i].text)
            count += 1

links = intro.find_all('a', href= True)
references = {}
for link in links:
    if link['href'][:2] == '//':
        word = 'https:'
        new_link = word + link['href']
        references[link.text] = new_link
    elif link['href'][:1] == '/':
        word = "https://en.wikipedia.org"
        new_link = word + link['href']
        references[link.text.strip()] = new_link
    else:
        references[link.text] = link['href']

#print(json.dumps(references, indent = 2))

with open("References.txt", 'a', encoding='utf-8') as f:
    f.write(query)
    f.write("\n")
    f.write(json.dumps(references, indent=2))