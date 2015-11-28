## py-mate-tools
Python interface for mate-tools written by Java.

## install
* download the install package
* python setup.py install


## usage

	import sys, os
	from PyMateTools import matetools

	mate_tools = matetools.MateTools()
	testdata = ['I saw a dog chasing a cat.', 'I love you.']
	cwd=os.getcwd()

	mate_tools.SRL( testdata, verbose = True, result_file_path = cwd )
	print ("done")
when you do above, you can get a result file ("result.out") in your working directory. 
