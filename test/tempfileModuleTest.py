__author__ = 'hz'

import os
import tempfile
#自动删除时，除了with as语句范围文件就自动删除了
with tempfile.NamedTemporaryFile( mode = "wb", delete = False ) as input_file:
    input_file.write( "test data" )
    input_file.flush()

#the temp file has already deleted
print( input_file.name )
input_file.close()

