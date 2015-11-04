__author__ = 'hz'

from src.matetools import MateTools
import os
mate_tools = MateTools()

testdata = ['I saw a dog chasing a cat.', 'I love you.']

cwd=os.getcwd()

mate_tools.SRL( testdata, verbose = True, result_file_path = cwd )

print("done!")
