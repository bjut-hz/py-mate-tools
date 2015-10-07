__author__ = 'hz'
import nltk

class DataFormat:
    def __init__(self):
        pass

    def dataFormat( self, _sentence ):
        """
        format the input data and save it in the tmp file
        :param _sentence:
        :return:
        """
        if isinstance( _sentence, list ):
            result = []
            for sentence in _sentence:
                result.extend( self.__dataFormat( sentence) )
                result.append( '\n' )
            self.__save( result)
            return result
        elif isinstance( _sentence, str ):
            result = self.__dataFormat( _sentence )
            self.__save( result )
            return result
        else:
            return  None

    def __dataFormat( self, sentence ):
        result = []
        words = nltk.word_tokenize( sentence )
        for word in words:
            word = ' ' + word + '\n'
            result.append( word )
        return result

    def __save( self, data ):
        f = file( 'tmp', 'w+' )
        f.writelines( data )
        f.close()


if __name__ == '__main__':
    testdata = ['I saw a dog chasing a cat.', 'I love you.']
    data_format = DataFormat()
    data_format.dataFormat( testdata )
    print( "test" )