import string



#from .urlresponse import *
from urlresponse import *


class SearchApp:

    baseUrl = Fetcher.base_url

    listOfArchs = ["armeabi-v7a", "arm64-v8a + armeabi-v7a",
                   "x86", "x86 + x86_64", "arm64-v8a", "mips", "mips64"]
    listOfVersion = ["Android 6.0+", "Android 7.0+",
                     "Android 8.0+", "Android 9.0+", ]

    def searchApp(self, query: str):

       # baseUrl = Fetcher.base_url
        search_result = []

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
            search_result.append(app_details)

        return search_result

        print(url)

    def searchDownloadOptions(self, url_of: str):

        souped_data = Fetcher.souper(url_of)

        result_list = []
        error = "not parsed yet"
        allTableRowHeaderFont = souped_data.find_all(
            "div", class_='table-row headerFont')

        for tableRows in allTableRowHeaderFont[1:]:
            download_page_url = tableRows.find(
                "a", class_='accent_color')['href']

            variant = tableRows.find(True, 'span', class_=[
                                     'apkm-badge success', 'apkm-badge'])

            # arch = tableRows.find(
            #     'div', class_="table-cell rowheight addseparator expand pad dowrap", string=self.listOfArchs)
            allTableCells = tableRows.find_all(
                'div', class_="table-cell rowheight addseparator expand pad dowrap")
            # print(allTableCells)
            arch = allTableCells[1]
            version = allTableCells[2]

            app_versions = {
                "variant": variant.text if variant is not None else error,
                "download_page_url": self.baseUrl + download_page_url,
                "arch": arch.text if arch is not None else error,
                "version": version.text if arch is not None else error
            }

            result_list.append(app_versions)

        return result_list

    def appInfo(self, url_of: str):

        soup_of_file = Fetcher.souper(url_of)

        app_details = soup_of_file.find_all(
            'div', class_='appspec-row', limit=2)
        app_size = app_details[1].find('div', class_='appspec-value').text

        apk_download_page = self.baseUrl + \
            soup_of_file.find(
                "svg", class_="icon download-button-icon").parent['href']
        

        soup = Fetcher.souper(apk_download_page)

        final_download_link = soup.find_all(
            'span', attrs={'style': 'font-weight: 500;'})[1].find('a')['href']

        # header = {
        #     #'authority' : 'www.apkmirror.com',
        #     #'path' : x[8:],
        #     #'scheme' : 'https',
        #     'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        #     'referer': 'https://www.apkmirror.com/apk/amazingbyte/ip-tools-network-utilities/ip-tools-network-utilities-8-33-release/ip-tools-wifi-analyzer-8-33-2-android-apk-download/download/?key=aad8581465ee240d8499ea2fdd64527ae5b3d171',
        #     #'sec-ch-ua-platform' : "Windows",
        #     #'upgrade-insecure-requests': '1'

        # }

        # """
        # The referer in the header must have key and always put allow_redirects to false to stop
        # requests from getting redirected to next page.

        # the download link is in the Location tag of the response header file.
        # """

        # r = requests.get('https://www.apkmirror.com/wp-content/themes/APKMirror/download.php?id=3731190&key=643c830ea6e9fccebca820a4cca7e9a6c2d29061',headers=header,allow_redirects=False)
        # print(r.headers)

        # print(x)

        result = {
            "app_details": app_details[0].text.strip('\n'),
            "app_size": app_size,
            "apk_download_page": apk_download_page,
            "ak_download_url": final_download_link
        }

        return result


search = SearchApp()

print(search.searchApp('whatsapp'))
# print(search.searchDownloadOptions(
#     'https://www.apkmirror.com/apk/google-inc/chrome/chrome-103-0-5060-129-release/'))

# print(search.searchDownloadOptions(
#     'https://www.apkmirror.com/apk/whatsapp-inc/whatsapp-business/whatsapp-business-2-22-15-74-release/'))

# searchresults = search.searchApp("google chrome")[0]["download_link_tag"]
# downloadoptions = search.searchDownloadOptions(searchresults)[0]["download_page_url"]
# appdownloadpagelink = search.appInfo(downloadoptions)["apk_download_url"]

# print(appdownloadpagelink)

#print(search.appInfo('https://www.apkmirror.com/apk/whatsapp-inc/whatsapp-business/whatsapp-business-2-22-15-74-release/whatsapp-business-2-22-15-74-4-android-apk-download/'))


# lol = search.appInfo(
#     'https://www.apkmirror.com/apk/google-inc/chrome/chrome-103-0-5060-129-release/google-chrome-fast-secure-103-0-5060-129-14-android-apk-download')
# print(lol)

# for appRow in apk_download_page:
#     with open('output.txt', 'w') as f:
#         for line in appRow:
#             f.write(str(line))
#             f.write('\n')

# print(app_details[0].text)
# print(app_size)
# print(apk_download_page)
