
from bs4 import BeautifulSoup
import requests
import traceback

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
        




def getApk_url(app_name = "whatsapp messenger",arch = "all"):
    url = base_url + "/?s=" + app_name;
    #testblock
    print(url)
    page_response = fetch_data(url)

    try:
        soup = BeautifulSoup(page_response,'html.parser')
        z = soup.find("div", class_="appRow")
        d = z.find("a", class_="fontBlack")
        downloadPage = d.get('href')
        page_link = base_url + downloadPage
        

        #test block
        print(page_link)
        page_content = fetch_data(page_link)
        page_content = BeautifulSoup(page_content, "html.parser")

        final_data = []
  
        link_container = page_content.findAll("div", class_="table-row headerFont")
        final_data = []
        fin = {}
        app_link =""
        arm_version = ""
        android_version = ""
        for links in link_container:
            o = links.findAll("div")
            if (o[1].string != None):
                arm_version = o[1].string;
                android_version = o[2].string;
  
            if (links.a != None):
                app_link = base_url +  links.a["href"] + "download"
            if (app_link != None and arm_version != None and android_version != None):
                # pass
                fin = {
                    "link": app_link,
                    "arm" : arm_version,
                    "android_version": android_version
                }

                final_data.append(fin)

        finaldict = {}
        

        for data in final_data:
            if (data['arm'] == arch):
                
                print(data['arm'])
                finaldict = data
                break
        
        linkOfDownloadPage = finaldict['link']
        print(linkOfDownloadPage)

        

        if(arch == 'all'):
            return final_data[1:]

        else:
            return finaldict    
            

        #return final_data[1:]
              

    except:
        traceback.print_exc()
    
print(getApk_url('whatsapp','armeabi-v7a'))
    
    