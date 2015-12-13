
# Imports #
from Application import *
import sys

# ========================================
#   This is the entrance of the 
# application where users can input name
# of two stations of Shanghai subway and
# find the shortest path between them.
# ========================================

reload(sys)
sys.setdefaultencoding('gbk')
app = Application()
app.run()
