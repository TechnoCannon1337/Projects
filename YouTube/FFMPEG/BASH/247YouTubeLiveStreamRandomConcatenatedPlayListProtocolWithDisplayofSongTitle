#!/bin/bash
#This script will Stream random MP3 files with the Song Name displayed on a looped video using an FFMPEG Concatenation Protocol on a YouTube Live Stream 24/7 using a Raspberry Pi.
until
while true; do
  until $($(for name in $(shuf -e -n1 /EnterFullDirectoryPathHere/*.mp3); do
    ffmpeg -thread_queue_size 1024 -re -nostdin -err_detect ignore_err -i "concat:$name" -thread_queue_size 1024 -re -stream_loop -1 -nostdin -err_detect ignore_err -i /EnterFullDirectoryPathHere/EnterVideoNameHere.mp4 -shortest -c:v libx264 -pix_fmt yuv420p -preset ultrafast -g 60 -b:v 2500k -bufsize 512k -acodec aac -ar 44100 -threads 8 -q:v 5 -q:a 0 -b:a 196k -r 24 -s 1280x720 -filter_complex drawtext="fontfile=monofonto.ttf: fontsize=36: box=1: boxcolor=black@0.75: boxborderw=5: fontcolor=yellow: x=w-tw-10:y=h-th-10: text='This Song is called $(echo "$(echo ${name#/EnterFullDirectoryPathHere/} | tr -s '_' | tr '_' ' ')" | sed -e 's/\(.mp3\)*$//g')'" -f flv rtmp://a.rtmp.youtube.com/live2/EnterSecretKeyHere
    Sleep 1
  done)); do
  sleep 1
done
done; do
sleep 1
done
#This Bash Script uses an "Until Loop" to restart the script on failure.
#This script uses a "While Loop" to restart the "Until Loop with embedded "For Loop" at the end of its' operation.
#This scripts uses an embedded "For Loop" to randomly select the name of each mp3 file in the referenced Directory
#This script uses an FFMPEG command to play every mp3 shuffled by the "For Loop" with a video that loops for the duration of the song.
#The FFMPEG command takes the filename refrenced from the "Name Variable", stripped of directory name, and displays it on the video.
#Challenges
#Not All Songs have Song Title & Artist Metadata so this method was omitted.
#See alternate Commit for an example of an implementation of using FFProbe Metadata: https://github.com/TechnoCannon1337/Projects/blob/master/YouTube/FFMPEG/BASH/247YouTubeLiveStreamRandomMusicPlayListWithDisplayofTitleandArtistMetadata
##Directories listed in full due to environment complications withen running this scripts on crontabs on reboot as a service. May use Systemd for future implementations.
###############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#Techno Cannon, MPA
#HTTPS://TECHNOCANNON.COM
#HTTPS://TECHNOCANNON.COM/FREELANCE
#
