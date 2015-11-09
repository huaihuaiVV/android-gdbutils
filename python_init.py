import gdb
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)) ,"python"))
import adbparams
import feninit, tracebt, fastload, adblog, updater
gdb.execute('source ' + os.path.dirname(__file__) + "/gdbinit")
