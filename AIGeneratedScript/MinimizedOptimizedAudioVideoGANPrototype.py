#A Minimized and Optimized Generative Adversarial Network Training Model for Generating Audio Encoded MP4 Video Files
import os,sys,time,datetime,getopt,argparse
import tensorflow as tf
import numpy as np
import scipy.io as sio
from scipy.io import wavfile
import glob
import numpy as np

def read_audio(filename):
    f = open(filename, "r")
    a = []
    for line in f:
        line = line.rstrip("\n")
        a.append(line.split(",")[0])
    return a

def read_wav(filename):
    f = open(filename, "r")
    sio.wavfile.read(f, "float")
    f.close()

def parse_args():
    parser = argparse.ArgumentParser(description = "Generate video with audio")
    parser.add_argument("-i", "--input", type=str, default="", help="input file")
    parser.add_argument("-o", "--output", type=str, default="", help="output file")
    parser.add_argument("-s", "--sample", type=int, default=44100, help="sample rate")
    parser.add_argument("-t", "--target", type=int, default=5, help="target bitrate (kbps)")
    parser.add_argument("-b", "--bitrate", type=int, default=96, help="bitrate (kbps)")
    parser.add_argument("-d", "--delay", type=int, default=0, help="delay (seconds)")
    parser.add_argument("-r", "--rate", type=int, default=44100, help="rate (kbps)")
    parser.add_argument("-f", "--framerate", type=int, default=15, help="framerate (fps)")
    parser.add_argument("-c", "--compression", type=int, default=2, help="compression ratio (0-2)")
    parser.add_argument("-b", "--bit", type=int, default=1, help="bit")
    parser.add_argument("-m", "--mono", type=int, default=1, help="mono")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose")
    return parser.parse_args()

def convert_audio(a):
    b = []
    for i in range(len(a)):
        if a[i] == "":
            b.append("0")
        else:
            b.append(int(a[i]))
    return np.array(b)

def main():
    args = parse_args()
    #print args
    input_file = args.input
    output_file = args.output
    sample_rate = args.sample
    target_bitrate = args.target
    bitrate = args.bitrate
    delay = args.delay
    rate = args.rate
    framerate = args.framerate
    compression = args.compression
    bit = args.bit
    mono = args.mono
    verbose = args.verbose
    audio = read_audio(input_file)
    wav = read_wav(input_file)
    audio = convert_audio(audio)
    wav = convert_audio(wav)
    print("Input file is %s, and output file is %s" % (input_file, output_file))
    print("Sample rate is %s, target bitrate is %s" % (sample_rate, target_bitrate))
    print("Bitrate is %s, delay is %s" % (bitrate, delay))
    print("Rate is %s, framerate is %s" % (rate, framerate))
    print("Compression is %s, mono is %s" % (compression, mono))
    print("bit is %s" % (bit))
    print("wav is %s" % (wav))
    print("audio is %s" % (audio))
    # create model
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(wav.shape[1], wav.shape[2], 1)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(128, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(256, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])

    # create optimizer
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
    # define loss function
    loss = tf.keras.losses.MeanSquaredError()

    # create metrics
    accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="accuracy")

    # create train function
    train = tf.function(model.compile(loss=loss, optimizer=optimizer))

    # create valid function
    valid = tf.function(model.evaluate(input_data=[wav], output_data=[audio]))

    # create testing function
    test = tf.function(model.evaluate(input_data=[wav], output_data=[audio]))

    # create audio data generator
    #generator = tf.keras.Sequential([
    #    tf.keras.layers.Flatten(),
    #    tf.keras.layers.Dense(64, activation="relu"),
    #    tf.keras.layers.Dense(64, activation="relu"),
    #    tf.keras.layers.Dense(1, activation="sigmoid")
    #])

    #create audio data generator
    #generator = tf.keras.Sequential([
    #    tf.keras.layers.Flatten(),
    #    tf.keras.layers.Dense(64, activation="relu"),
    #    tf.keras.layers.Dense(64, activation="relu"),
    #    tf.keras.layers.Dense(1, activation="sigmoid")
    #])

    #create audio data generator
    #generato
