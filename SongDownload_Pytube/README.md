#Song Downloaded using Pytube library
## Introduction 
* Pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.

## Features 
* Support for Both Progressive & DASH Streams
* Easily Register on_download_progress & on_download_complete callbacks
* Command-line Interfaced Included
* Caption Track Support
* Outputs Caption Tracks to .srt format (SubRip Subtitle)
* Ability to Capture Thumbnail URL.
* Extensively Documented Source Code
* No Third-Party Dependencies

##Installation Guidelines
* Pytube library =>
```pip install pytube```

## Steps
* Enter any Youtube Video URL to download in mp3 format.
* Choose destination, leave empty to download in the present directory.

## Note
>If you wish to download a youtube video insted of audio

* Copy paste the following code to Line 10:

```video = audio_object.streams.filter(only_video=True).first()```


