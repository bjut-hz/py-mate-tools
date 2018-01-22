from __future__ import unicode_literals

import tempfile
import os
from subprocess import PIPE
from internals import find_jar, find_jar_iter, config_java, java, _java_options
import nltk


class DataFormat:
    def __init__(self):
        pass

    def dataFormat( self, _sentence ):
        """
        format the input data and save it in the tmp file
        :param _sentence: str or []
        :return:
        """
        if isinstance( _sentence, list ):
            result = []
            for sentence in _sentence:
                result.extend( self.__dataFormat( sentence) )
                result.append( '\n' )
            return result
        elif isinstance( _sentence, str ):
            result = self.__dataFormat( _sentence )
            return result
        else:
            return  None

    def __dataFormat( self, sentence ):
        result = []
        words = nltk.word_tokenize( sentence )
        for word in words:
            word = ' ' + word + '\n'
            result.append( word.encode('utf-8') )
        return result



class MateTools():

    MAIN_CLASS = r'se.lth.cs.srl.CompletePipeline'
    JARS = r'srl.jar;lib/anna-3.3.jar;lib/liblinear-1.51-with-deps.jar;lib/opennlp-tools-1.5.2-incubating.jar;lib/opennlp-maxent-3.0.2-incubating.jar;lib/seg.jar'
    LEMMA_MODEL = r'models/CoNLL2009-ST-English-ALL.anna-3.3.lemmatizer.model'
    TAGGER_MODEL = r'models/CoNLL2009-ST-English-ALL.anna-3.3.postagger.model'
    PARSER_MODEL = r'models/CoNLL2009-ST-English-ALL.anna-3.3.parser.model'
    SRL_MODEL = r'models/CoNLL2009-ST-English-ALL.anna-3.3.srl-4.1.srl.model'
    OUTPUT_FORMAT = r"conll2009"


    def __init__(self,  encoding = 'utf8', java_options = '-Xmx4g' ):
        self.java_options = java_options
        self.encoding = encoding
        self.classpath = ( r'srl.jar', r'lib/anna-3.3.jar', r'lib/liblinear-1.51-with-deps.jar',
                           r'lib/opennlp-tools-1.5.2-incubating.jar', r'lib/opennlp-maxent-3.0.2-incubating.jar',
                           r'lib/seg.jar' )

    def SRL( self, sentence, result_file_path = r"./", file_name = r"result.out", verbose = False ):
        cmd = [
            self.MAIN_CLASS,
            'eng',
            '-lemma', self.LEMMA_MODEL,
            '-tagger', self.TAGGER_MODEL,
            '-parser', self.PARSER_MODEL,
            '-srl', self.SRL_MODEL,
        ]
        self._execute( cmd, sentence, verbose, result_file_path, file_name )

    def _execute(self, cmd, input_, verbose=False, result_file_path = r'./', result_file_name = 'result.out' ):
        """

        :param cmd:
        :param input_: input sentence(s) []type
        :param verbose:
        :return:
        """
        # # change the work directory
        # dir =  os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir) )
        dir = os.path.dirname(__file__)
        cwd=os.getcwd()
        os.chdir(dir)

        encoding = self.encoding
        default_options = ' '.join( _java_options )

        # Configure java.
        config_java( options = self.java_options, verbose = verbose )

        data_format = DataFormat()

        input_ = data_format.dataFormat( input_ )
        if None == input_:
            raise ValueError( 'data format failed: input param format error.' )

        # Windows is incompatible with NamedTemporaryFile() without passing in delete=False.
        # create the file with mode w+,
        with tempfile.NamedTemporaryFile( mode = 'w+', delete = False ) as input_file:
            input_file.writelines( input_ )
            input_file.flush()


            cmd.extend( [ '-test', input_file.name ] )
            cmd.extend( [ '-out', result_file_path + r'/' + result_file_name ] )
            stdout, stderr = java( cmd, classpath = self.classpath, stdout = PIPE, stderr = PIPE )

            if verbose:
                print( 'stdout:' )
                print( stdout )
                print( 'stderr:' )
                print( stderr )

        os.unlink( input_file.name )

        # Return java configurations to their default values.
        config_java( options = default_options, verbose = False )

        os.chdir( cwd )
