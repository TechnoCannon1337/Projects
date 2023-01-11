import os
import subprocess
#This Python Script uses FFMPeg on Linux to mix background music to multiple mp3 audio files.
#The script should be run from a directory sepearate from your source files to avoid source files.
backGroundMP3File = '/EnterFullDirectoryPathHere/EnterBackgroundSoundFileNameHere.mp3'
batchFileDirectory = '/EnterFullDirectoryPathtoBatchofAudioFilesHere/'
batchDirectoryList = os.listdir(batchFileDirectory)
primaryFilter = '-filter_complex'
filterSettings = '[0:a]volume=-14dB[a0];[1:a]volume=6dB[a1];[a0][a1]amix=inputs=2:duration=longest[a]'
audioMap = '-map'
mapSettings ='[a]'

def runAudioMixer():
    for sourceFileName in batchDirectoryList:
        secondInput = os.path.join(batchFileDirectory, sourceFileName)
        ffCommand = ['ffmpeg', '-i', backGroundMP3File, '-i', secondInput, primaryFilter, filterSettings, audioMap, mapSettings, 'mixed_'+sourceFileName]
        subprocess.run(ffCommand)
runAudioMixer()
