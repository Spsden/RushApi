from .urlresponse import *

class SearchPure:

    baseUrl = "https://apkpure.com/"

    def searchApp(self, query:str):

        search_result = []

        url = self.baseUrl + "search?q=" + query

        soupedData = Fetcher.souper(url)
        topResult = soupedData.find("div" ,class_='info')
        otherResults = soupedData.find_all("div",class_="search-dl search-item")

        if topResult != None:
            app_details = {
                "name" : topResult.find("p",class_='p1').text,
                "icon" : topResult.find('img')['src'],
                "dpage" : self.baseUrl + topResult.find_next('a' , class_="da")['href'],
                "dev" : topResult.find('p',class_="p2").text,
                "span" : "NA",
                "source" : "apkpure"


            }
            search_result.append(app_details)
        
        for result in otherResults:
            app_details = {
                "name" : result.find('p').text,
                "icon" : result.find('img')['src'],
                "dpage" : result.find('a',class_='more-down')['href'],
                "dev" : result.find('p',class_='developer').find_next().text,
                "span" : "NA",
                "source" : 'apkpure'
            }
            search_result.append(app_details)
        return search_result
        

# x = SearchPure()
# print(x.searchApp(query='whatsapp'))