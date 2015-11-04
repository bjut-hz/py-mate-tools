__author__ = 'hz'
import sys
import os
sys.path.append( '..' )

from matetools import MateTools

mate_tools = MateTools()

testdata = ['I saw a dog chasing a cat.', 'I love you.']

cwd=os.getcwd()

mate_tools.SRL( testdata, verbose = True, result_file_path = cwd )

print("done!")
