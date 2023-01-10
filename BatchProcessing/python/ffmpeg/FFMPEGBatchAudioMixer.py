import os
import subprocess
#This Python Script uses FFMPeg on Linux to mix background music to multiple mp3 audio files.
#The script should be run from a directory sepearate from your source files to avoid source files.
backGroundMP3File = '/EnterFullDirectoryPathHere/EnterBacgroundSoundFileNameHere.mp3'
batchFileDirectory = '/EnterFullDirectoryPathtoBatchofAudioFilesHere/'
batchDirectoryList = os.listdir(batchFileDirectory)
primaryFilter = '-filter_complex'
primaryEngine = '[0:a]volume=0.75[a0];[1:a]volume=1.0[a1];[a0][a1]amix=inputs=2:duration=longest[a]'
audioMap = '-map'
mapSettings ='[a]'

def runAudioMixer():
    for sourceFileName in batchDirectoryList:
        secondInput = os.path.join(batchFileDirectory, sourceFileName)
        ffCommand = ['ffmpeg', '-i', backGroundMP3File, '-i', secondInput, primaryFilter, primaryEngine, audioMap, mapSettings, sourceFileName]
        subprocess.run(ffCommand)
runAudioMixer()
