__author__ = 'hz'

import subprocess
import os
# args:java -cp srl.jar;lib\anna-3.3.jar;lib\liblinear-1.51-with-deps.jar;
# lib\opennlp-tools-1.5.2-incubating.jar;lib\opennlp-maxent-3.0.2-incubating.jar;lib\seg.jar
# -Xmx4g
# se.lth.cs.srl.CompletePipeline
# eng -lemma models\CoNLL2009-ST-English-ALL.anna-3.3.lemmatizer.model
# -tagger models\CoNLL2009-ST-English-ALL.anna-3.3.postagger.model
# -parser models\CoNLL2009-ST-English-ALL.anna-3.3.parser.model
# -srl models\CoNLL2009-ST-English-ALL.anna-3.3.srl-4.1.srl.model
# -test data\test.txt -out eng-val.out

cmd = [r'C:\Program Files\Java\jdk1.8.0_60\bin\java.exe',
       r'-cp', r'srl.jar;lib\anna-3.3.jar;lib\liblinear-1.51-with-deps.jar;lib\opennlp-tools-1.5.2-incubating.jar;lib\opennlp-maxent-3.0.2-incubating.jar;lib\seg.jar',
       u'-Xmx4g',
       u'se.lth.cs.srl.CompletePipeline',
       u'eng',
       u'-lemma', u'models\CoNLL2009-ST-English-ALL.anna-3.3.lemmatizer.model',
       u'-tagger', u'models\CoNLL2009-ST-English-ALL.anna-3.3.postagger.model',
       u'-parser', u'models\CoNLL2009-ST-English-ALL.anna-3.3.parser.model',
       u'-srl', u'models\CoNLL2009-ST-English-ALL.anna-3.3.srl-4.1.srl.model',
       u'-test', r'data\test.txt',
       u'-out', u'eng-test.out']

package_directory = os.path.dirname(os.path.abspath(__file__))
dir =  os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir) )
cwd=os.getcwd()
os.chdir(dir)

#cmd = ['java', 'test']

p = subprocess.Popen( cmd, stdin = None, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(stdout, stderr) = p.communicate()
print( stderr )
print( stdout )
p.wait()

print("test")

