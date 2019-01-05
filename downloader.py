import urllib
import urllib.request
from bs4 import BeautifulSoup
from os import system
import sys

def titleCase(s):
    '''
    A function to convert the given song name to title case.
    The default function in Python convert the words 'the', 'and', 'of', etc.
    And I find that annoying
    '''

    l = s.split()
    str = l[0][0].upper() + l[0][1:]
    
    for word in l[1:]:
        if word not in ['in', 'the', 'for', 'of', 'a', 'at', 'an', 'is', 'and']:
            str += ' ' + word[0].upper() + word[1:]
        else:
            str += ' ' + word
    
    return str

pathToSave = "~/Music/"

def getVidID(song, URL):
    '''
    This function gets the ID of the Video you have to download.
    '''
    search = song + ' lyrics'
    searchQuery = '+'.join(search.split())
    searchURL = URL + searchQuery
    
    response = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(response.read(), "lxml")

    vidID = soup.body.find_all(class_="yt-uix-tile-link")[0]['href']
    return vidID

def doStuff(song):
    print("Downloading " + titleCase(song))
    URL = 'https://www.youtube.com/results?search_query='
    vidID = getVidID(song, URL)
    link = 'https://www.youtube.com' + vidID
    system("youtube-dl -x -q -o \'" + pathToSave + titleCase(song) + ".%(ext)s\' \'" + link + "\'")
    print("Downloaded " + titleCase(song) + "\n") 

def main():
    print('-------------------------------------------------------------')
    if (len(sys.argv) == 3 and (sys.argv[1] == '-i' or sys.argv[1] == '-I')):
        for song in open(sys.argv[2]).readlines():
            doStuff(song)

    else:
        for song in sys.argv[1:]:
            doStuff(song)
# except:
#     print("AN ERROR OCCURED!!\nAre you connected to the internet?\nIf you are, try reading the README and see if it helps.")

if __name__ == '__main__':
    main();
