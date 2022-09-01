from pytube import  YouTube  
import pytube as yt   
import os


yt_url = ''   #video url
path = 'C:\\Users\\Downloads'    #my folder, where the video will be donwloaded

#define some resolutions
high = "720p"
ultra = "1080p"
mp4 = '.mp4'
mp3 = '.mp3'


def download_video(url,folder,quality):
    try:   
        youtube = yt.YouTube(url)  
        #video = youtube.streams.first()  
        video = youtube.streams.filter(res=quality).first()
        video.download(path)  
        print("Download Video Successfull !!")
    except:
        print("Something Went Wrong  with video!!")


def download_only_sound(url,folder):
    try:   
        youtube = yt.YouTube(url)  
        video = youtube.streams.filter(only_audio=True).first()
        file = video.download(path)  
        base, ext = os.path.splitext(file)
        new_file = base + mp3
        os.rename(file,new_file)
        print("Download Successfull only sound!!")
    except:
        print("Something Went Wrong with sound!!"
)

#download_video(yt_url,path,high)
download_only_sound(yt_url,path)