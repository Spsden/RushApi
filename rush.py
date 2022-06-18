
from bs4 import BeautifulSoup
import requests
from sys import exit
import re


def responseChecker(response):
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        print("success")
        return response.content




def getapkurl(app_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
    }
    base_url = "https://www.apkmirror.com/"
    response = requests.get(base_url + "/?s=" + app_name ,headers = headers)
    content = responseChecker(response=response)
    

    soup = BeautifulSoup(content,'html.parser')
    z = soup.find("div", class_="appRow")
    # print(z)
    d = z.find("a", class_="fontBlack")
    print(d.string)
    downloadPage = d.get('href')
    
    print(base_url + downloadPage)

    response2 = requests.get(base_url + downloadPage,headers=headers)
    contentOfDownloadListPage = responseChecker(response=response2)

    soupOfDownloadListPage = BeautifulSoup(contentOfDownloadListPage,'html.parser')
    listOfKeys = []
    listOfValues = []
    testvar = soupOfDownloadListPage.findAll("div",class_="table-cell rowheight addseparator expand pad dowrap")

 
    for tests in testvar:

        
        listOfKeys.append(tests.text)

        if(tests.a != None):
            listOfValues.append(tests.a["href"] )
        

       
        
    #print(listOfKeys)
    # for links in listOfKeys:
    #     print(links)
    #     print("\n")
    list2 = [x.replace('\n', '') for x in listOfKeys]
    print(list2)

    print("\n")
    for links in listOfValues:
        print(links)
        print("\n")

    #print(listOfValues)
    

    


   
    
    #print(soup.prettify())
    print(soup.title)
    
getapkurl('Whatsapp')