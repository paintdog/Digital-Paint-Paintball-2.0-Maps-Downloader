# A script to download all Digital Paint Paintball 2 maps, currently available on the server.
# It's a quick and dirty tool and you will have to do some more work on your own.

from bs4 import BeautifulSoup
import os
import requests
import shutil


def download_maps(url):
    # The tool downloads all maps (.bsp)
    # from a given url
    html_webpage = requests.get(url).text
    soup_webpage = BeautifulSoup(html_webpage)
    files = soup_webpage.find_all("a")

    if "beta" in url:
        PATH = os.curdir + "/beta/"
        os.mkdir(PATH)
    else:
        PATH = os.curdir
        
    for file in files:

        filename = file["href"]
        
        if filename.endswith(".bsp"):
            
            print(filename)
            file_url = url + filename
            response = requests.get(file_url, stream=True)

            with open(PATH + filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)


def main():
    
    url = "http://dplogin.com/files/maps/"
    download_maps(url)

    url = "http://dplogin.com/files/maps/beta/"
    download_maps(url)


if __name__ == "__main__":

    main()
