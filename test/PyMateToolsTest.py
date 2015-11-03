__author__ = 'hz'

from src.matetools import MateTools

mate_tools = MateTools()

testdata = ['I saw a dog chasing a cat.', 'I love you.']

mate_tools.SRL( testdata, verbose = True )

print("done!")
