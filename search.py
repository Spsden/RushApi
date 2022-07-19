from urlresponse import *

#fetcher = Fetcher()

class SearchApp:
    search_result = []

    

    def __init__(self,query:str):
        self.query = query
    
    def searchApp(self):
         
        baseUrl = Fetcher.base_url
        
        url = baseUrl + "?s=" + self.query
        soupedData = Fetcher.souper(url)
        allAppRows = soupedData.findAll("div", class_='appRow')
        #print(allAppRows)

        


        for appRow in allAppRows[:10]:
            icon_tag = appRow.find('img')
            app_details = {
                "name_and_version" : icon_tag['alt'],
                "icon_url" : baseUrl + icon_tag['src'],
                "download_link_tag" : baseUrl + appRow.find("a",class_='downloadLink')['href']

            }
            self.search_result.append(app_details)
            # app_details["name_and_version"] = icon_tag['alt']
            # app_details["icon_url"] = icon_tag['src']
            # app_details["download_link_tag"] = appRow.find("a",class_='downloadLink')['href']
            
            # download_link_tag = appRow.find("a",class_='downloadLink')['href']
            # name_and_version = icon_tag['alt']
            # icon_url = icon_tag['src']
            # print(name_and_version)
            # #print(icon_url)
            # #print(download_link_tag)

        # for appRow in allAppRows:
        #         with open('output.txt', 'w') as f:
        #          for line in appRow:
        #           f.write(str(line))
        #           f.write('\n')


       # print(search_result)

        return self.search_result

        
        
        print(url)

    


search = SearchApp('whatsapp')

print(search.searchApp())

