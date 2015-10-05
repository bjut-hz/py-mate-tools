__author__ = 'hz'
import nltk

class DataFormat:
    def __init__(self):
        pass

    def dataFormat( self, _sentence ):

        if isinstance( _sentence, list ):
            for sentence in _sentence:
                words = nltk.word_tokenize( sentence )
                for word in words:
                    pass
                pass
        elif isinstance( _sentence, str ):
            pass
        else:
            return  None


if __name__ == '__main__':
    f = file( 'hell.txt', 'w+')
    data = [' hello world\n', ' hello python\n']
    f.writelines( data )
    f.close()