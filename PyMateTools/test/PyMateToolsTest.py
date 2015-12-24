__author__ = 'hz'
import sys
import os
#import nltk
sys.path.append( '..' )

from matetools import MateTools

mate_tools = MateTools()


# str = 'Disclosed is an organic light-emitting diode (OLED) display panel. An OLED display panel includes a plurality of signal lines and a thin film transistor formed on a substrate, an interlayer insulating layer, a first electrode, a bank, an organic light-emitting layer, a second electrode, a first passivation layer, an organic layer, a second passivation layer and a barrier film, wherein the bank is formed to completely cover the interlayer insulating layer, and an inclination formed by side surfaces of the bank and the interlayer insulating layer is made to be gradual.'
#
# testdata = nltk.sent_tokenize( str )
testdata = ['Disclosed is an organic light-emitting diode (OLED) display panel.']
testdata = ['I saw a dog chasing a cat.']
cwd=os.getcwd()

mate_tools.SRL( testdata, verbose = True, result_file_path = cwd )

print("done!")
