from bs4 import BeautifulSoup
import requests
import json

queries = ['Central Michigan University', 'California State University(CSU), East Bay', 'Gannon University', 'Governors State University - Chicago',
           'Iowa State University', 'Learning Links Foundation', 'Marist college - New York', 'New Jersey Institute of Technology', 'Northern Arizona University',
           'Ontario Tech University', 'Pace University', 'Pittsburg State University', 'Rennes School of Business', 'Rochester Institute of Technology', 'Rowan University', 'San Jose State University',
           'State University of New York at Oswego', 'State University of New York Utica & Albany', 'Stony Brook University', 'The University of Alabama in Huntsville', 'Trent University - Peterborough and Durham GTA, Ontario, Canada',
           'University at Buffalo, The State University of New York', 'University of Arizona', 'University of Arkansas', 'University of California, Riverside',
           'University of Canterbury, Christchurch, New Zealand', 'University of Colorado Denver', 'University of Essex', 'The University of Europe for Applied Sciences',
           'University of Kent', 'University of Michigan - Flint', 'University of North Texas', 'University of Southampton',
           'Wayne State University, Detroit(MI)', 'Wright State University - Dayton Campus']
"""for query in queries:    
    query_string = query.replace(" ", "+")
    html_text = requests.get("https://www.google.com/search?q={}".format(query_string)).text
    soup = BeautifulSoup(html_text, 'lxml')
    info = soup.find('div', class_="wwUB2c PZPZlf E75vKf")
    print(info)
"""
college_info = {}

for query in queries:
    query_string = query.replace(" ", "+")
    html_text = requests.get("https://www.google.com/search?q={}".format(query_string)).text
    soup = BeautifulSoup(html_text, 'html.parser')
    intro = soup.find_all('span', class_=False)
    #print(intro[1].div.text)
    rating_location = intro[1].div.text
    college_info[query] = rating_location

with open('Universities.txt', 'a', encoding='utf-8') as f:
    f.write(json.dumps(college_info, indent=2))

f = open('Universities.txt', 'r')
print(f.read())