# importing packages
from pytube import YouTube
import os

# url input from user
audio_object = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = audio_object.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(audio_object.title + " has been successfully downloaded.")
