import string

from urlresponse import *

#fetcher = Fetcher()


class SearchApp:
    search_result = []
    baseUrl = Fetcher.base_url

    listOfArchs = ["armeabi-v7a","arm64-v8a + armeabi-v7a","x86","x86 + x86_64","arm64-v8a","mips","mips64"]
    listOfVersion = ["Android 6.0+","Android 7.0+","Android 8.0+","Android 9.0+",]

    def searchApp(self, query: str):

       # baseUrl = Fetcher.base_url

        url = self.baseUrl + "?s=" + query
        soupedData = Fetcher.souper(url)
        allAppRows = soupedData.findAll("div", class_='appRow')
        # print(allAppRows)

        for appRow in allAppRows[:10]:
            icon_tag = appRow.find('img')
            app_details = {
                "name_and_version": icon_tag['alt'],
                "icon_url": self.baseUrl + icon_tag['src'],
                "download_link_tag": self.baseUrl + appRow.find("a", class_='downloadLink')['href']

            }
            self.search_result.append(app_details)

        return self.search_result

        print(url)


    def searchDownloadOptions(self, url_of:str):

        souped_data = Fetcher.souper(url_of)
        #print(souped_data.prettify)
        result_list = []
        error = "not parsed yet"
        allTableRowHeaderFont = souped_data.find_all("div", class_='table-row headerFont')

        for tableRows in allTableRowHeaderFont[1:]:
            download_page_url = tableRows.find("a",class_= 'accent_color')['href']

            variant = tableRows.find(True,'span',class_ = ['apkm-badge success','apkm-badge'])

            # if download_type is not None:
            #    print(download_type.text)
            #arminfo = tableRows.find_next_sibling('div')
            
            arch = tableRows.find('div', class_= "table-cell rowheight addseparator expand pad dowrap", string = self.listOfArchs)
            version = arch.find_next_sibling()
            #print(arch.find_next_sibling())
            #print(arminfo)

            app_versions = {
                "variant": variant.text if variant is not None else error,
                "download_page_url": self.baseUrl + download_page_url,
                "arch": arch.text if arch is not None else error,
                "version" : version.text if arch is not None else error
            }

            result_list.append(app_versions)
        

        return result_list
            #print('/////////////////////////////////////////////////////')


            

search = SearchApp()

#print(search.searchApp('whatsapp'))
print(search.searchDownloadOptions('https://www.apkmirror.com/apk/google-inc/chrome/chrome-103-0-5060-129-release/'))
