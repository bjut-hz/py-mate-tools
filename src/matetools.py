__author__ = 'hz'

class MateTools():
    JARS = r'srl.jar;lib\anna-3.3.jar;lib\liblinear-1.51-with-deps.jar;lib\opennlp-tools-1.5.2-incubating.jar;lib\opennlp-maxent-3.0.2-incubating.jar;lib\seg.jar'
    LEMMA_MODEL = r'models\CoNLL2009-ST-English-ALL.anna-3.3.lemmatizer.model'
    TAGGER_MODEL = r'models\CoNLL2009-ST-English-ALL.anna-3.3.postagger.model'
    PARSER_MODEL = r'models\CoNLL2009-ST-English-ALL.anna-3.3.parser.model'
    SRL_MODEL = r'models\CoNLL2009-ST-English-ALL.anna-3.3.srl-4.1.srl.model'
    OUTPUT_FORMAT = r"conll2009"


    def __init__(self):
        pass

    def SRL( self, sentence, cwd = r"./", file_name = r"result" ):
        cmd = []
        self._execute( cmd )

    def _execute(self, cmd ):
        pass
