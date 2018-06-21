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

Thanks,  <br>
Enjoy...
