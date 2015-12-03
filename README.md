## PyMateTools
Python interface for mate-tools written by Java.

## install
* download the install package
* thanks to the limit of file size uploading to GitHub, you should download the models first and put the four models in "PyMateTools/models/" directory.
	* download url: [mate-tools](https://code.google.com/p/mate-tools/), or [百度网盘](http://pan.baidu.com/s/1dDr0qrv)
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

## demo website
[mate-tools demo](http://barbar.cs.lth.se:8081/parse)