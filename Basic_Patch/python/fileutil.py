import nt

#####################
#  Add Mods support #
#####################

import sys
try: sys.moddir
except AttributeError:
	 sys.moddir = "vampire"
from sys import moddir

######################
#  File Utility v1.0 #
######################

"""

Provides basic file traversal and manipulation functions extracted from full 
python 2.1.2 shell source. To help mitigate possibility of damaging non-game 
related files, all WRITE operations will fail if "Vampire" (or 'moddir') is 
not found in directory path

"""

S_IFDIR  = 0040000
S_IFREG  = 0100000

def getcwd():
    """ Return Current Working Directory """
    cwd=""
    try: cwd=nt.getcwd()
    except: 
      print "[Error] fileutil : getcwd - Unable to retrieve Current Working Directory"
      pass
    return cwd

def exists(path):
    """Test whether a path exists"""
    # (extracted from python 2.1.2 : ntpath.py)
    try: st = nt.stat(path)
    except nt.error: return 0
    return 1

def isDir(path):
    """ Returns true if file path is a directory """
    # (extracted from python 2.1.2 : stat.py, ntpath.py)
    try: st = nt.stat(path)
    except nt.error: return 0
    return ((st[0] & 0170000) == S_IFDIR)

def isFile(path):
    """ Returns true if file path is a File """
    # (extracted from python 2.1.2 : stat.py, ntpath.py)
    try: st = nt.stat(path)
    except nt.error: return 0
    return ((st[0] & 0170000) == S_IFREG)

def list(path):
    """ Returns list of all items within directory """
    alllist=[]
    try: alllist=nt.listdir(path)
    except: pass
    return alllist

def listdir(path):
    """ Returns list of subdirectories of a given directory """
    dirlist=[]
    try: dirlist=[f for f in nt.listdir(path) if not f.startswith(".") and isDir(path+"\\"+f)]
    except: pass
    return dirlist

def listfiles(path):
    """ Returns list of files of a given directory """
    filelist=[]
    try: filelist=[f for f in nt.listdir(path) if isFile(path+"\\"+f)]
    except: pass
    return filelist

def mkdir(path):
    if -1 == path.find("\\"+moddir+"\\"): return 0
    try: nt.mkdir(path)
    except: pass
    return exists(path)

def readlines(path,numlines=-1):
    if not exists(path): return []
    result=[]
    fin = None
    try:
      fin = open(path,"r")
      line = fin.readline()
      while line and numlines != 0:
        result.append(line.rstrip())
        line=fin.readline()
        numlines=numlines-1
    finally:
      if fin: fin.close()
    return result

def writetofile(path,str):
    if -1 == path.find("\\"+moddir+"\\"): 
       print "fileutil : writetofile - Invalid Directory"
       return
    fptr = None
    try:
      fptr = open(path, 'w')
      fptr.write(str)
    finally:
      if fptr: fptr.close()

def appendtofile(path,str):
    if -1 == path.find("\\"+moddir+"\\"): 
       print "fileutil : appendtofile - Invalid Directory"
       return
    fptr = None
    try:
      fptr = open(path, 'a')
      fptr.write(str)
    finally:
      if fptr: fptr.close()

def copyfile(src, dst):
    """Copy data from src to dst"""
    # (extracted from python 2.1.2 : shutil.py)

    if -1 == src.find("\\"+moddir+"\\"): 
       print "fileutil : copyfile - source directory Invalid"
       return

    if -1 == dst.find("\\"+moddir+"\\"): 
       print "fileutil : copyfile - destination directory Invalid"
       return

    fsrc = None
    fdst = None
    try:
        fsrc = open(src, 'rb')
        fdst = open(dst, 'wb')
        length=16*1024
        while 1:
            buf = fsrc.read(length)
            if not buf:
                break
            fdst.write(buf)
    finally:
        if fdst:
            fdst.close()
        if fsrc:
            fsrc.close()

def removefile(path):
    # checks that file is a FILE (not a directory) and the path contains "\\Vampire\\", 
    # (or "\\"+moddir+"\\") otherwise it fails. 
    if isFile(path) and path.find("\\"+moddir+"\\") > -1:
      nt.unlink(path)
    else:
      print "[Error] fileutil: removeFile called on invalid path: [%s]" % path     
