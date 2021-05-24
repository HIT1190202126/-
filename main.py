import jpype
from jpype import *
import os.path
# 启动java虚拟机




jarpath = os.path.abspath('.')

startJVM( getDefaultJVMPath(),  "-ea",  "-Djava.class.path=%s" % (jarpath + '/P1.jar'))
test=JPackage("P0").MagicSquare()
a=test.main()



