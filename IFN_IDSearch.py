import os
import re
# Install Cool terminal colors + requests cuz im cool and yeah 
os.system("pip3 install colorama")
os.system("pip3 install requests")
os.system("cls")

import requests
from colorama import init, Fore, Back, Style


def frontpage():
    os.system("cls")
    print(Fore.RED + """
                                                                 
                             ,--.                                
   ,---,     ,---,.        ,--.'|                                
,`--.' |   ,'  .' |    ,--,:  : |                                
|   :  : ,---.'   | ,`--.'`|  ' :                                
:   |  ' |   |   .' |   :  :  | |          ,----._,.   ,----._,. 
|   :  | :   :  :   :   |   \ | :         /   /  ' /  /   /  ' / 
'   '  ; :   |  |-, |   : '  '; |        |   :     | |   :     | 
|   |  | |   :  ;/| '   ' ;.    ;        |   | .\  . |   | .\  . 
'   :  ; |   |   .' |   | | \   |        .   ; ';  | .   ; ';  | 
|   |  ' '   :  '   '   : |  ; .'        '   .   . | '   .   . | 
'   :  | |   |  |   |   | '`--'    ___    `---`-'| |  `---`-'| | 
;   |.'  |   :  \   '   : |       /  .\   .'__/\_: |  .'__/\_: | 
'---'    |   | ,'   ;   |.'       \  ; |  |   :    :  |   :    : 
         `----'     '---'          `--"    \   \  /    \   \  /  
                                            `--`-'      `--`-'   
    """ + Style.RESET_ALL)








frontpage()


def SearchAPI():
    
    api_key = '2CB0F8156B4F7FE29ACF9E5124B60333' # screw encryption

    api_url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'




    steam_url_pattern = re.compile(r'(https?://)?steamcommunity\.com/id/([^/\n]+)|steamcommunity\.com/profiles/(\d+)/?')
    steam_id_pattern = re.compile(r'(STEAM_)?(0|1):([0-9]+):([0-9]+)')

    print(Fore.LIGHTMAGENTA_EX + "Please enter SteamURL / URL_ID")
    steam_url = input()


    steam_username = ''
    steam_id = ''
    match = steam_url_pattern.search(steam_url)
    if match:
        if match.group(2):
            steam_username = match.group(2)

            response = requests.get(api_url, params={'key': api_key, 'vanityurl': steam_username})

            if response.status_code == 200:
                data = response.json()

                if data['response']['success'] == 1:
                    steam_id = data['response']['steamid']
                    print('Steam64 ID for', Fore.RED + steam_username + Style.RESET_ALL, Fore.MAGENTA + 'is' + Style.RESET_ALL, Fore.GREEN + steam_id + Style.RESET_ALL)
                    print(Fore.CYAN + "Press enter to start a new search" + Style.RESET_ALL)
                    input()
                    frontpage()
                    SearchAPI()
                else:
                    print('Error:', data['response']['message'])
                    frontpage()
                    SearchAPI()
            else:
                print('Error:', response.status_code)
                frontpage()
                SearchAPI()


    elif not match:
        steam_username = steam_url

        response = requests.get(api_url, params={'key': api_key, 'vanityurl': steam_username})

        if response.status_code == 200:
            data = response.json()

            if data['response']['success'] == 1:
                steam_id = data['response']['steamid']
                print('Steam64 ID for', Fore.RED + steam_username + Style.RESET_ALL, Fore.MAGENTA + 'is' + Style.RESET_ALL, Fore.GREEN + steam_id + Style.RESET_ALL)
                print(Fore.CYAN + "Press enter to start a new search" + Style.RESET_ALL)
                input()
                frontpage()
                SearchAPI()
            else:
                print('Error:', data['response']['message'])
                frontpage()
                SearchAPI()
        else:
            print('Error:', response.status_code)
            frontpage()
            SearchAPI()


    else:
        print(Fore.RED + "Invalid Steam URL / SteamUrlID" + Style.RESET_ALL)
        print(Fore.CYAN + "Press enter to start a new search" + Style.RESET_ALL)
        input()
        frontpage()
        SearchAPI()
   

SearchAPI()


