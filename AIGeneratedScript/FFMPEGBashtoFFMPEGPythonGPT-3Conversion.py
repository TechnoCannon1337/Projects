import os
import time

def run_command(command):

try:

os.system(command)

except:

pass

def main():

source_directory = "."

song_directory = source_directory + "/"

video_directory = source_directory + "/EnterNameofVideoFileHere"

ffmpeg = "ffmpeg"

song_artist = "Unknown Artist"

song_title = "Unknown Title"

video_file = "EnterNameofVideoFileHere.mp4"

rtmp_server = "rtmp://a.rtmp.youtube.com/live2/"

rtmp_key = "EnterSecretKeyHere"

while True:

run_command("ffmpeg -thread_queue_size 1024 -re -nostdin -err_detect ignore_err -i $video_file -thread_queue_size 1024 -re -stream_loop -1 -nostdin -err_detect ignore_err -i $song_file -c:v libx264 -pix_fmt yuv420p -preset ultrafast -g 60 -b:v 2500k -bufsize 512k -shortest -acodec aac -ar 44100 -threads 8 -q:v 5 -q:a 0 -b:a 196k -r 24 -s 1280x720 -filter_complex drawtext="fontfile=monofonto.ttf: fontsize=36: box=1: boxcolor=black@0.75: boxborderw=5: fontcolor=yellow: x=w-tw-10:y=h-th-10: text='This Song is called $(echo "$(echo ${song_title#/EnterFullPathofSourceDirectoryHere/} | tr -s '_' | tr '_' ' ')" | sed -e 's/\(.mp3\)*$//g') by Song Artist $song_artist'" -f flv rtmp://rtmp_server/$rtmp_key
time.sleep(1)
except KeyboardInterrupt:

print("Error running command")

time.sleep(1)

main()

#The Above Script was generated with OpenAi's GPT-3 Model by converting this original script minus the comments: https://github.com/TechnoCannon1337/Projects/blob/76e4c47d80f392a70ef8146dad0a49f4ce985fb2/YouTube/FFMPEG/BASH/GenerativePretrainedTransformer-J-6BGeneratedFFMpegYouTubeMusic247LiveStreamer