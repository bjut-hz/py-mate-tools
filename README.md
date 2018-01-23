## PyMateTools
Python interface for mate-tools written by Java.

## install
* download the install package
* thanks to the limit of file size uploading to GitHub, you should download the models first and put the four models in "PyMateTools/models/" directory. ([can be found here](https://code.google.com/archive/p/mate-tools/downloads?page=2)*)
	* download url: [mate-tools](https://code.google.com/p/mate-tools/), or [百度网盘](http://pan.baidu.com/s/1dDr0qrv)
* python setup.py install


 Links to individual model files:
 * [CoNLL2009-ST-English-ALL.anna-3.3.srl-4.1.srl.model](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mate-tools/CoNLL2009-ST-English-ALL.anna-3.3.srl-4.1.srl.model)
 * [CoNLL2009-ST-English-ALL.anna-3.3.parser.model](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mate-tools/CoNLL2009-ST-English-ALL.anna-3.3.parser.model)
* [CoNLL2009-ST-English-ALL.anna-3.3.postagger.model](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mate-tools/CoNLL2009-ST-English-ALL.anna-3.3.postagger.model)
* [CoNLL2009-ST-English-ALL.anna-3.3.lemmatizer.model](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mate-tools/CoNLL2009-ST-English-ALL.anna-3.3.lemmatizer.model)
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
