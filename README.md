# Youtube Downloader

### Python , youtube-dl

## Description

I've written a script in python that will allow you to download videos from YouTube: <br>
     whether it's a single video,  <br>
     or an entire playlist. <br>

All you need to do is : <br>
    1. open YouTube web site , <br>
    2. copy the link of the page,  <br>
    3. click on the script, <br>
    4. and wait for the download to complete. <br> <br>

note: The file is downloaded where the script is located <br> <br>


* Operating requirements: <br><br>

Installing the youtube-dl you need to unzip the file youtube-dl-master.zip and enter into the folder and then install the setup.py by the command in cmd there: <br>

```python
python setup.py install
```
<br>
Installing the following packages using the pip <br>

```python
pip install pyperclip
pip install pprint
```

<br>
* Install Windows PowerShell, and place his path in the script

See my video in [youtube](https://youtu.be/M6Xf87ZN0aw)

* Weaknesses <br>
1. When there is a playlist with a private video in it, then downloading the playlist will download all videos to that private video in the playlist.<br>
2. When the name of a single video or playlist has special markers, then the folder will not open automatically, but the video will not be downloaded. <br><br>

* Example
I copied the link: https://www.youtube.com/watch?v=Mp9Jg7NX2Vo&list=PL0lNJEnwfVVObxfHDVMTZProttL1EHuGZ&ab_channel=DesignCourse <br>
Then I ran the file (double-clicking the file) <br>
The output: <br>
```
Please wait until the program will finished
Then you see the result, or Error showed up if this happened...

Runs the following command in Powershell:

   youtube-dl -o 'C:\Users\Hadriel\Desktop/Youtube Downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/watch?v=Mp9Jg7NX2Vo"&"list=PL0lNJEnwfVVObxfHDVMTZProttL1EHuGZ"&"ab_channel=DesignCourse

...

Playlist: THIS WEEK
----------------------------------------------------------------------------------------------------

[download] Downloading video 1 of 2 |  (24.26MiB) 1 - THIS WEEK - Electron Desktop Apps, and what is SmashingMag thinking.mp4
[download] Downloading video 2 of 2 |  (30.77MiB) 2 - THIS WEEK - Angular_Electron. And why you need to start your own biz, ASAP!.mp4

----------------------------------------------------------------------------------------------------

Placed in folder: C:\Users\Hadriel\Desktop\Youtube Downloads\THIS WEEK

Opens a folder that contains the files



Press any key to continue . . .
```
<br>
<br>
Thanks,  <br>
Enjoy...
