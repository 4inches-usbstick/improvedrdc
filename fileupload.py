import base64
import os
from urllib.parse import unquote


def doGET(get = {}, addargs = {}):
    return '<h1>No HTTP GET for this location.'
    
def doUPLOADPOST(posted, f):
    print('Called doUPLOADPOST')
    print(type(f))
    return str(f)