from ast import Try
import requests
import traceback
from bs4 import BeautifulSoup


class Fetcher():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
    }
    
    base_url = "https://www.apkmirror.com/"

    # TO REQUEST TO SERVER
    def fetch_data(link = base_url):
        try:
            response = requests.get(link, headers=Fetcher.headers)
            if (response.status_code != 200):
                raise Exception(f"Error occurred" + response.status_code)
            return response.content
        except:
            traceback.print_exc()

    def souper(page_link):
        response = Fetcher.fetch_data(page_link)
        try:
            soup = BeautifulSoup(response,'lxml')
            return soup
        except:
            traceback.print_exc
         

    

# HEADERS






# # TO REQUEST TO SERVER
# def fetch_data(link = base_url):
#     try:
#         response = requests.get(link, headers=headers)
#         if (response.status_code != 200):
#             raise Exception(f"Error occurred" + response.status_code)
#         return response.content
#     except Exception:
#         return "Error " + Exception 
        