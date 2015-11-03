__author__ = 'hz'

import os
import tempfile
#when set delete = True£¬the file will be deleted when out of with as scope
with tempfile.NamedTemporaryFile( mode = "wb", delete = False ) as input_file:
    input_file.writelines( [ 'i saw a dog.', 'I love you' ] )
    input_file.flush()

#the temp file has already deleted
print( input_file.name )
os.unlink( input_file.name )

