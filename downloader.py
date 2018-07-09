import urllib
import urllib.request
from bs4 import BeautifulSoup
from os import system

pathToSave = "~/Music/"

def getSongID(song, URL):
    
    search = song + ' lyrics'
    searchQuery = '+'.join(search.split())
    searchURL = URL + searchQuery
    
    response = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(response.read(), "lxml")

    vidID = soup.body.find_all(class_="yt-uix-tile-link")[0]['href']
    return vidID


n = int(input("Enter the number of Songs: "))
songList = []
print("Enter the name of the songs: ")
for i in range(n):
    songName = input(str(i+1)+". ")
    songList += [songName]

for song in songList:
    try:
        # song = input("Enter the name of the song: ")
        print("Downloading " + song.title())
        URL = 'https://www.youtube.com/results?search_query='
    
        vidID = getSongID(song, URL)
        link = 'https://www.youtube.com' + vidID
        system("youtube-dl -x -q -o \'" + pathToSave + song.title() + ".%(ext)s\' \'" + link + "\'")
        print("Downloaded " + song.title() + "\n")
    
    except:
        print("AN ERROR OCCURED!!\nAre you connected to the internet?\nIf you are, try reading the README and see if it helps.")

