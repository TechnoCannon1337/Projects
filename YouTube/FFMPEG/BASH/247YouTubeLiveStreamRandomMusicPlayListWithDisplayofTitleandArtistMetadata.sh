#!/bin/bash
#This script will play random mp3 files with the Song Name & Artist displayed on a looped video on a YouTube Live Stream 24/7 using a Raspberry Pi.
until
while true; do
  for name in $(shuf -e /EnterFullPathofSourceDirectoryHere/*.mp3); do
  SongArtist="$(ffprobe -v error -show_entries format=artist -of default=noprint_wrappers=1:nokey=1 $name)"
  SongTitle="$(ffprobe -v error -show_entries format_tags=filename -of default=noprint_wrappers=1:nokey=1 $name)"
  ffmpeg -thread_queue_size 1024 -re -nostdin -err_detect ignore_err -i $name -thread_queue_size 1024 -re -stream_loop -1 -nostdin -err_detect ignore_err -i /EnterFullPathofSourceDirectoryHere/EnterNameofVideoFileHere.mp4 -c:v libx264 -pix_fmt yuv420p -preset ultrafast -g 60 -b:v 2500k -bufsize 512k -shortest -acodec aac -ar 44100 -threads 8 -q:v 5 -q:a 0 -b:a 196k -r 24 -s 1280x720 -filter_complex drawtext="fontfile=monofonto.ttf: fontsize=36: box=1: boxcolor=black@0.75: boxborderw=5: fontcolor=yellow: x=w-tw-10:y=h-th-10: text='This Song is called $(echo "$(echo ${SongTitle#/EnterFullPathofSourceDirectoryHere/} | tr -s '_' | tr '_' ' ')" | sed -e 's/\(.mp3\)*$//g') by Song Artist $SongArtist'" -f flv rtmp://a.rtmp.youtube.com/live2/EnterSecretKeyHere
done
done; do
  sleep 1
done
#This Bash Script uses an "Until Loop" to restart the script on failure.
#This script uses a "While Loop" to restart the "For Loop" at the end of its' operation.
#This scripts uses a "For Loop" to randomly select the name of each mp3 file in the referenced Directory
#This script assigns two variables to an FFProbe command that grabs the metadata for the Song Artist & Song Title when available for each file shuffled by the "For Loop".
#This script uses an FFMPEG command to play every mp3 shuffled by the "For Loop" with a video that loops for the duration of the song.
#The FFMPEG command takes the filename refrenced from the "Name Variable", stripped of directory name, and displays it on the video with the MetaData Artist Name, if any, collected by the FFProbe command.
#
#Challenges
#Not All Songs have Song Title & Artist Metadata
#Directories listed in full due to environment complications with running this scripts on crontabs on reboot as a service. May use Systemd for future implementations.
#"For Loop" designed to restart FFMPEG command once finished with new song and this sometimes causes a noticible skip during livestream for at least 1 second...
#...Looking for a way to use FFMPEG Concatenate on a randomly created input list songs instead, which I've found works better with no noticiple interuptions, and display the Song Information simultaneously.
#...to be continued.
#
#Techno Cannon, MPA
# HTTPS://TECHNOCANNON.COM
# HTTPS://TECHNOCANNON.COM/FREELANCE
#
