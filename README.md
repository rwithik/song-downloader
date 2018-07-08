# song-downloader
A Python Script to download songs in the best available format from Youtube.

### Dependancies
* `urllib`: Install `urllib` module with `pip3` with this command  
`pip3 install urllib`
* BeautifulSoup: Install BeautifulSoup4 with  
`pip3 install beautifulsoup4`
* youtube-dl: Use `pip3 install youtube_dl` to install youtube-dl

### How to Use  
* First time users please check the next section.
* Download the downloader.py file to your system.
* Open the terminal and into the directory where the you saved the file.
* Run this command:  
`python3 downloader.py`
* It will ask you the name of the song. Enter the name.
* Wait and it will download the song. Enjoy. ;-)

### First Time Use
* Before using the program, open it with a text editor.
* Change `PATH GOES HERE` to the path where you want the downloaded songs to be saved. And do leave a trailing '\' character. 
* Example: If you want them to be saved at `~/Music` folder, then line 6 shpuld look like this:  
`pathToSave = "~/Music/"`  
and not  
`pathToSave = "~/Music"`
* You're good to go. Refer How to Use if there's any issue.
