__author__ = 'hz'

import os
import tempfile
#�Զ�ɾ��ʱ������with as��䷶Χ�ļ����Զ�ɾ����
with tempfile.NamedTemporaryFile( mode = "wb", delete = False ) as input_file:
    input_file.write( "test data" )
    input_file.flush()

#the temp file has already deleted
print( input_file.name )
input_file.close()

