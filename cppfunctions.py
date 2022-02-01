import requests
from bs4 import BeautifulSoup

URL = "https://en.cppreference.com/w/cpp/header"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mw-content-text")

the_list_of_all_the_functions = []

functs = results.find_all("div", class_="t-dsc-member-div")



for func in functs:
    func_link = func.find('a')
    sub_URL = "https://en.cppreference.com/w/" + func_link.get('title')
    print(sub_URL, end="\n"*2)
    
    sub_page = requests.get(sub_URL)

    sub_soup = BeautifulSoup(sub_page.content, "html.parser")

    sub_results = sub_soup.find(id="mw-content-text")

    sub_functs = sub_results.find_all("span", class_="mw-headline", id="Functions")

    if sub_functs:

        table_data = sub_results.find('table', class_='t-dsc-begin') 

        table_data = table_data.find_all('tr',class_='t-dsc')

        for i in table_data:
            fonk = i.find_all('span',class_='t-lines')          #Function names
            type_list = i.find_all('span',class_='t-mark')
            for a,k in zip(fonk,type_list):
                if "function" in k.text:
                    b = a.find_all('span')
                    for c in b:
                        the_list_of_all_the_functions.append(c.text)

print(the_list_of_all_the_functions)
