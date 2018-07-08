import urllib
import urllib.request
from bs4 import BeautifulSoup
from os import system

def getSongID(song, URL):
    
    search = song + ' lyrics'
    searchQuery = '+'.join(search.split())
    searchURL = URL + searchQuery
    
    response = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(response.read(), "lxml")

    vidID = soup.body.find_all(class_="yt-uix-tile-link")[0]['href']
    return vidID

song = input("Enter the name of the song: ")
print("Downloading " + song.title())
URL = 'https://www.youtube.com/results?search_query='

vidID = getSongID(song, URL)
link = 'https://www.youtube.com' + vidID

system("youtube-dl -x -q -o \'~/Music/" + song.title() + ".%(ext)s\' \'" + link + "\'")
print("Downloaded " + song.title())
