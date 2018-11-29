import urllib
import urllib.request
from bs4 import BeautifulSoup
from os import system
import sys

def titleCase(s):
    l = s.split()
    str = l[0][0].upper() + l[0][1:]
    list = ['in', 'the', 'for', 'of', 'a', 'at', 'an', 'is', 'and', 'to']
    for word in l[1:]:
        if word not in list:
            str += ' ' + word[0].upper() + word[1:]
        else:
            str += ' ' + word

    return str

def getVidID(song, URL):
    search = song + ' lyrics'
    searchQuery = '+'.join(search.split())
    searchURL = URL + searchQuery

    response = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(response.read(), "lxml")

    vidID = soup.body.find_all(class_="yt-uix-tile-link")[0]['href']
    return vidID

print('-------------------------------------------------------------')
pathToSave = "Music/"
for song in sys.argv[1:]:
    # song = input("Enter the name of the song: ")
    print("Downloading " + titleCase(song))
    URL = 'https://www.youtube.com/results?search_query='
    vidID = getVidID(song, URL)
    link = 'https://www.youtube.com' + vidID
    system("youtube-dl -q -x -o \'" + pathToSave + titleCase(song) + ".%(ext)s\' \'" + link + "\'")
    print("Downloaded " + titleCase(song) + "\n")
    # print(link)
