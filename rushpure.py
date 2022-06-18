
from bs4 import BeautifulSoup
import requests

# HEADERS
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
    }

base_url = "https://www.apkmirror.com/"


# def responseChecker(response):
#     if response.status_code != 200:
#         print("Error fetching page")
#         exit()
#     else:
#         print("success")
#         return response.content

# TO REQUEST TO SERVER
def fetch_data(link = base_url):
    try:
        response = requests.get(link, headers=headers)
        if (response.status_code != 200):
            raise Exception(f"Error occurred" + response.status_code)
        return response.content
    except Exception:
        return "Error " + Exception 
        




def getApk_url(app_name = "whatsapp"):
    url = base_url + "/?s=" + app_name;
    page_response = fetch_data(url)

    try:
        soup = BeautifulSoup(page_response,'html.parser')
        z = soup.find("div", class_="appRow")
        d = z.find("a", class_="fontBlack")
        print(d.string)
        downloadPage = d.get('href')
        page_link = base_url + downloadPage
        page_content = fetch_data(page_link)
        page_content = BeautifulSoup(page_content, "html.parser")
        links_container = page_content.findAll("div", class_="table-cell rowheight addseparator expand pad dowrap")

        final_data = []
        for links in links_container:
            b = links.text

            if(links.a != None):
                a = links.a["href"]

            data = {
                "description": b.replace("\n", ""),
                "link": base_url + a + 'download'
            }

            final_data.append(data)

        print(final_data)


            
        

    except:
        print('error occurred')
    
    
    
getApk_url('facebook')
