import os
import io
import subprocess
import ffmpeg
import glob
import random
MediaDirectory = "/home/pi/Programs/NTWatch/"
PlayList = random.choice(os.listdir(glob.glob('{MediaDirectory}*.mp3')))
ThreadQueueSize = "-thread_queue_size 1024"
StreamLoop = "stream_loop -1"
RealTime = "-re"
AudioInput = "-f concat -safe 0 -i {InPut}"
VideoInput = "{MediaDirectory}BeatCops.mp4"
StreamFeed = "-shortest"
VideoCodec = "-c:v libx264"
PixelFormat = "-pix_fmt yuv420p"
Preset = "-preset ultrafast"
GroupOfPictures = "-g 60"
VideoBitRate = "-b:v 5000k"
BufferSize = "-bufsize 512k"
AudioCodec = "-acodec aac"
AudioRate = "-ar 44100"
StreamThread = "-threads 8"
VideoQuality = "-q:v 5"
AudioQuality = "-q:a 0"
AudioBitrate = "-b:a 196k"
FrameRate = "-r 24"
SreenSize = "-s 1280x720"
FilterComplex = "-filter_complex"
FontFile = "fontfile=monofonto.ttf"
FontColor = "fontcolor=yellow"
FontSize = "fontsize=36"
Box = "box=1"
BoxColor = "boxcolor=black@0.75"
Border = "boxborderw=5"
x = "x=w-tw-10"
y = "y=h-th-10"
SongText = "text='Song Title\: ${name%.*}'"
VideoFormat = "-f flv"
OutPutStream = "rtmp://a.rtmp.youtube.com/live3/0123-4567-8901-2345-6789"
def OverLay(TitleFontFile,TitleFontColor,TitleFontSize,TitleBox,TitleBoxColor,TitleBorder,Titlex,Titley,TitleSongText):
	print('drawtext="TitleFontFile:TitleFontColor:TitleFontSize:TitleBox:TitleBoxColor:TitleBorder:Titlex:Titley:TitleSongText"')
TitleWave = "OverLay(FontFile,FontColor,FontSize,Box,BoxColor,Border,x,y,SongText)"
def BeatCops():
        for name in PlayList:
                InPut = "File '{MediaDirectory}{name}'"
                cmd = ['ffmpeg', '{ThreadQueueSize}', '{StreamLoop}', '{RealTime}', '{AudioInput}', '{VideoInput}', '{StreamFeed}', '{VideoCodec}', '{PixelFormat}', '{Preset}', '{GroupOfPictures}', '{VideoBitRate}', '{BufferSize}', '{AudioCodec}', '{AudioRate}', '{StreamThread}', '{VideoQuality}', '{AudioQuality}', '{AudioBitrate}', '{FrameRate}', '{SreenSize}', '{TitleWave}', '{VideoFormat}', '{OutPutStream}']
                proc = subprocess.Popen(cmd)
                sleep(1)
                return proc


while True:
        BeatCops()
        if condition():
                break
