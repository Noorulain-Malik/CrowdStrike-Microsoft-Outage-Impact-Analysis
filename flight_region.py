from bs4 import BeautifulSoup
import requests

url ="https://en.wikipedia.org/wiki/2024_CrowdStrike_incident"
page = requests.get(url)
print(page)
soup=BeautifulSoup(page.text,'html.parser')

flights= soup.find_all( "div" , class_ ="mw-heading mw-heading4" ) 
# print(flights)
                                            # Extracting Air transport information of the continent #######

for flights in flights:
    print("Continent name", flights.get_text())

                                            ######################  End ####################################
                                            ## Send a Request and Parse the Page:
                                            #Find the Section Heading for "North America":
                                            #Extract All <a> Tags Within the "North America"########
    north_America = flights.find_all( "Air lines","div" , class_ ="mw-heading mw-heading4")
    for north_America in north_America:
        print("this is the title", north_America.get_text(href = "https://en.wikipedia.org/wiki/United_Airlines"))
