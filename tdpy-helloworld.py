def doGET(params = {}, addargs = {}):
    return 'The following arguments were passed to tdpy-helloworld.py: '+str(params)
    
def doPOST(posted = {}, addargs = {}):
    return 'The following arguments were POSTed to tdpy-helloworld.py:'+ str(posted)