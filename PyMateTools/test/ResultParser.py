__author__ = 'hz'
import re

class Parser():
    def __init__(self):
        pass

    def parser(self, file_name = r"result.out" ):
        file = open( file_name, "r" )
        # contents dataformat:[ [[], [], []], [[], [], []] ]
        contents = []
        tmp = []
        content = file.readline()
        while content:
            if "\n" != content:
                content = content.split()
                tmp.append( content )
            else:
                contents.append( tmp )
                tmp = []

            content = file.readline()
        file.close()

        # start parsing to get the SAO struct
        SAOS = []
        for item in contents:
            # one sentence's sao struct, data format[ [A, [S], O], [] ]
            saos = []
            # to get the Args's subscript
            index = 0
            for _item in item:
                if '_' != _item[13]:
                    index += 1
                    pattern = 'VB\w*'
                    if None != re.match( pattern, _item[5] ):
                        sao = []
                        sao.append( _item[1] )
                        PHead = int( _item[9] )
                        A_index = int( _item[0] ) - 1
                        # we can get the sao struct according to th Args
                        # get the S
                        S_index = 0
                        for element in item :
                            if None != re.match( 'A\w*', element[ 13+index ] ):
                                S = []
                                pre_S = []
                                post_S = []
                                S_index = int( element[0] ) - 1
                                # should be rewrited
                                if 0 < S_index:
                                    for i in range( S_index ):
                                        if i != A_index:
                                            if 3 >= abs( int( item[i][9] ) - PHead ):
                                                if 'DT' == item[i][5] or 'P' == item[i][11]:
                                                    continue
                                                else:
                                                    pre_S.append( element[1] )
                                    for i in range( S_index + 1, len( item ) ):
                                        if i != A_index:
                                            if 3 >= abs( int( item[i][9] ) - PHead ):
                                                if 'DT' == item[i][5] or 'P' == item[i][11]:
                                                    continue
                                                else:
                                                    post_S.append( element[1] )
                                else:
                                    for i in range( S_index + 1, len( item ) ):
                                        if i != A_index:
                                            if 3 >= abs( int( item[i][9] ) - PHead ):
                                                if 'DT' == item[i][5] or 'P' == item[i][11]:
                                                    continue
                                                else:
                                                    post_S.append( item[i][1] )
                                pre_S.extend( S )
                                S = pre_S
                                S.extend( post_S )
                                # get one sao struct
                                sao.append( S )
                                saos.append( sao )
            SAOS.append( saos )
        return  SAOS







if __name__ == '__main__':

    parser = Parser()
    result = parser.parser()
    print( result )
    # file = open( r"result.out", "r")
    # result = []
    #
    # while True:
    #     content = file.readline()
    #     if content:
    #         content = content.split()
    #         result.append( content )
    #     else:
    #         break
    #
    # print result
    #
    # print len( result[0] )
    # print len( result[1] )