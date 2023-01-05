import os
from firebase_admin import credentials, initialize_app, storage



cred = credentials.Certificate("YOUR DOWNLOADED CREDENTIALS FILE (JSON)")
initialize_app(cred, {'storageBucket': 'YOUR FIREBASE STORAGE PATH (without gs://)'})

 
fileitem = form['filename']
 
# check if the file has been uploaded
if fileitem.filename:
    # strip the leading path from the file name
    fn = os.path.basename(fileitem.filename)
     
   # open read and write the file into the server
    open(fn, 'wb').write(fileitem.file.read())