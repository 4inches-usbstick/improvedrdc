import os
import os.path

dirtemplate = """ 
<a style="color: blue;" href="treewalker.dpy?path=$ndir">$dir</a><br>
"""
def doGET(params = {}, addargs = {}):

    if not os.path.isdir(params['path']):
        f = open(params['path'], 'r')
        try: c = f.read()
        except:
            f.close()
            return 'Tree Helper<h1>' + params['path']+'</h1><br><br>This file is binary encoded and cannot be transmitted.'
        f.close()
        try: return '<h1>' + params['path'] + '/'  + '</h1><br><textarea rows="450" cols="50" style="width: 1162px; height: 340px;">'+str(c)+'</textarea>'
        except: return '<h1>' + params['path'] + '/'  + ''+str(c)+'</h1><br><br>This file is binary encoded and cannot be transmitted.'
    
    things = os.listdir(params['path'])
    leadingup = params['path'].rsplit('/', 1)[0]
    subs = []
    for i in things:
        if os.path.isdir(params['path'] + '/' + i):
            np = params['path'] + '/' + i + ''
            subs.append(dirtemplate.replace('$dir', "'"+i+"'").replace('$ndir', np) )
        else:
            subs.append('<a href="treewalker.dpy?path='+params['path'] + '/' + i+'">'+i+'</a><br>')
        
        print(params['path'] + '/' + i)
            
    tr = ''
    for i in subs:
        tr = tr + i
    return 'Tree Helper <h1>' + params['path'] + '/' + '</h1>' + tr