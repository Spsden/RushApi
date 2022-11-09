# RushApi

## How to use ?

1. Create a virtual environment using venv or conda.
2. activate the venv and clone the repo inside it.
4. run command 
    ```
    pip install -r requirements.txt
    ```
5. after installing all the required packages run command
   ```
   python main.py
   ```


### Features

- To search apps 

      https://rushy.vercel.app/rush/app/{app_name}`
	  
	  //eg https://rushy.vercel.app/rush/app/whatsapp  `
	  
	  
    
   Returns
   ```JSON

  {
    "name_and_version": "WhatsApp Messenger 2.22.16.16 beta",
    "icon_url": "https://www.apkmirror.com//wp-content/themes/APKMirror/ap_resize/ap_resize.php?src=https%3A%2F%2Fwww.apkmirror.com%2Fwp-content%2Fuploads%2F2022%2F07%2F12%2F62daf2dad641b.png&w=32&h=32&q=100",
    "download_link_tag": "https://www.apkmirror.com//apk/whatsapp-inc/whatsapp/whatsapp-2-22-16-16-release/"
  },
  {
    "name_and_version": "WhatsApp Business 2.22.16.13 beta",
    "icon_url": "https://www.apkmirror.com//wp-content/themes/APKMirror/ap_resize/ap_resize.php?src=https%3A%2F%2Fwww.apkmirror.com%2Fwp-content%2Fuploads%2F2022%2F07%2F95%2F62d9cd6e33d4a.png&w=32&h=32&q=100",
    "download_link_tag": "https://www.apkmirror.com//apk/whatsapp-inc/whatsapp-business/whatsapp-business-2-22-16-13-release/"
  },

  {
    "name_and_version": "WhatsApp Messenger 2.22.16.14 beta",
    "icon_url": "https://www.apkmirror.com//wp-content/themes/APKMirror/ap_resize/ap_resize.php?src=https%3A%2F%2Fwww.apkmirror.com%2Fwp-content%2Fuploads%2F2022%2F07%2F67%2F62d9b3124d005.png&w=32&h=32&q=100",
    "download_link_tag": "https://www.apkmirror.com//apk/whatsapp-inc/whatsapp/whatsapp-2-22-16-14-release/"
  },


   ```
   
 - To get variants
 
   ```
   https://rushy.vercel.app/rush/variants/?varianturl={download_link_tag returned from previous request}'
   
   eg https://rushy.vercel.app/rush/variants/?varianturl=https://www.apkmirror.com//apk/whatsapp-inc/whatsapp/whatsapp-2-22-16-14-release/
   
   ```
   
   Returns
   



  ```JSON
  {
    "variant": "APK",
    "download_page_url": "https://www.apkmirror.com//apk/whatsapp-inc/whatsapp/whatsapp-2-22-16-14-release/whatsapp-messenger-2-22-16-14-2-android-apk-download/",
    "arch": "armeabi-v7a",
    "version": "Android 4.1+"
  },
  {
    "variant": "APK",
    "download_page_url": "https://www.apkmirror.com//apk/whatsapp-inc/whatsapp/whatsapp-2-22-16-14-release/whatsapp-messenger-2-22-16-14-android-apk-download/",
    "arch": "arm64-v8a",
    "version": "Android 4.1+"
  },
  
  ```
   
