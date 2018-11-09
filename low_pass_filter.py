#This program accepts wav files as inputs, and outputs wav files with their higher frequencies filtered
#by taking the height of a mass on a spring, pushed by the original sound file.

#The input file should to be a single channel wav with a bit depth of 16.
#example: python low_pass_filter.py input.wav output.wav

import sys
import scipy.io.wavfile
import numpy
import math

def low_pass_filter_model(position, velocity, signal):
    frequency_cutoff = 0.00000005
    springConstant = 1
    viscosity = math.sqrt(2*springConstant*frequency_cutoff)
    return (signal - springConstant*position - viscosity*velocity)/frequency_cutoff

def integrate(signal, dt):
    output = [0.0]*len(signal)
    velocity = 0.0
    
    for i in range(len(signal) - 1): #last sample will be thrown away to avoid index access error.
       acceleration = low_pass_filter_model(output[i], velocity, signal[i])
       velocity = acceleration*dt + velocity
       output[i+1] = velocity*dt + output[i]

    return output


(sampling_rate, data) = scipy.io.wavfile.read(sys.argv[1])
dt = 1/sampling_rate

muffled = integrate(data, dt)

output = numpy.array(muffled)
output = numpy.around(output)
output = output.astype(numpy.int16)
scipy.io.wavfile.write(sys.argv[2], sampling_rate, output)
